from YouGileAPI import ProjectsApi
import pytest
from time import sleep

api = ProjectsApi("https://ru.yougile.com/api-v2")

@pytest.fixture(autouse=True)
def add_delay_after_test():
    yield
    sleep(1)

# Позитивная проверка для создания проекта
def test_create_a_project():
    title = "TestPro"
    users = None
    valid_data_project = api.new_project(title, users)
    project_id = valid_data_project.json()["id"]
    get_project = api.get_project_by_id(project_id)
    project = get_project.json()
    assert project["title"] == title
    assert project["id"] == project_id

# Негативная проверка для создания проекта
def test_create_project_without_title():
    title = ""
    users = None
    invalid_data_project = api.new_project(title, users)
    assert invalid_data_project.status_code == 400

# Позитивная проверка для изменения проекта
def test_change_of_project():
    title = "TestPro"
    users = None
    valid_data_project = api.new_project(title, users)
    project_id = valid_data_project.json()["id"]
    change_title = "ProTest"
    change_users = None
    change_project = api.change_of_project(project_id, change_title, change_users)
    check_project = change_project.json()
    assert check_project["id"] == project_id
    get_project = api.get_project_by_id(project_id)
    check_get_project = get_project.json()
    assert check_get_project["title"] == change_title
    assert check_get_project["users"] == {}
    assert check_get_project["id"] == project_id

# Негативная проверка для изменения проекта
def test_change_of_project_without_id():
    new_title = "SkyTest"
    new_users = None
    project_id = None
    resp = api.change_of_project(project_id, new_title, new_users)
    assert resp.status_code == 404

# Позитивная проверка отображения проекта в списке компании
def test_project_display_in_company_list():
    title = "TestSky"
    users = None
    valid_data_project = api.new_project(title, users)
    project = valid_data_project.json()
    get_list_of_projects = api.get_list_of_company_projects()
    project_list = get_list_of_projects.json()
    project_ids = [p["id"] for p in project_list["content"]]
    if project["id"] in project_ids:
        for p in project_list["content"]:
            if p["id"] == project["id"]:
                assert p["title"] == title
                assert p["users"] == {}

# Негативная проверка для получения проекта по несуществующему ID
def test_get_project_by_invalid_id():
    invalid_id = "999999"
    resp = api.get_project_by_id(invalid_id)
    assert resp.status_code == 404
    assert resp.json()["statusCode"] == 404
    assert resp.json()["message"] == "Проект не найден"
    assert resp.json()["error"] == "Not Found"