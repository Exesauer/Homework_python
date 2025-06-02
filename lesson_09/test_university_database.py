import pytest
from UsersTable import UsersTable

@pytest.fixture
def db():
    # Создание подключения к базе данных
    return UsersTable("postgresql://myuser:mypassword@localhost:5432/mydatabase")

@pytest.fixture
def test_user(db):
    # Добавляем тестового пользователя перед тестом
    params = {
        "user_email": "Test@mail.com",
        "subject_id": 1
    }
    db.add_new_user(params)
    user_id = db.get_user_with_max_id()
    yield user_id
    # Удаляем пользователя после теста
    db.delete_user_by_id({"user_id": user_id})

def test_add_new_user(db):
    list_before = db.get_all_users()
    params = {
        "user_email": "Test@gmail.com",
        "subject_id": 2
    }
    db.add_new_user(params)
    list_after = db.get_all_users()
    user_id = db.get_user_with_max_id()
    new_user = db.get_user_by_id({"user_id": user_id})[0]
    db.delete_user_by_id({"user_id": user_id})

    assert len(list_before) == len(list_after) - 1
    assert new_user["user_email"] == params["user_email"]
    assert new_user["subject_id"] == params["subject_id"]
    assert new_user["user_id"] == user_id

def test_change_user_data(db, test_user):
    new_params = {
        "user_email": "Test@yandex.ru",
        "subject_id": 3,
        "user_id": test_user
    }
    db.change_user_data(new_params)
    changed_user = db.get_user_by_id({"user_id": test_user})[0]
    assert changed_user["user_email"] == new_params["user_email"]
    assert changed_user["subject_id"] == new_params["subject_id"]
    assert changed_user["user_id"] == test_user

def test_delete_user(db):
    list_before = db.get_all_users()
    params = {
        "user_email": "Test@mail.com",
        "subject_id": 1
    }
    db.add_new_user(params)
    user_id = db.get_user_with_max_id()
    db.delete_user_by_id({"user_id": user_id})
    list_after = db.get_all_users()
    assert len(list_after) == len(list_before)