import requests

token = ("NVTrUBIucppGRzmz+cqm6XcGV1phNTeQfLOAC2JFTob0lU-ynS5IYAFymjkEClzh")

class ProjectsApi:

    def __init__(self, url):
        self.url = url

    def new_project(self, title, users=None):
        if users is None:
            users = {}
        json = {
            "title": title,
            "users": users
            }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }
        resp = requests.post(self.url+"/projects", headers=headers, json=json)
        return resp

    def get_project_by_id(self, id):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }
        resp = requests.get(self.url+"/projects/"+id, headers=headers)
        return resp

    def get_list_of_company_projects(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }
        resp = requests.get(self.url+"/projects/", headers=headers)
        return resp

    def change_of_project(self, id, title, users=None):
        if users is None:
            users = {}
        if id is None:
            id = ""

        json = {
            "title": title,
            "users": users
            }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }
        resp = requests.put(self.url+"/projects/"+str(id), headers=headers, json=json)
        print("Status code:", resp.status_code)
        print("Response body:", resp.text)
        try:
            resp.raise_for_status()
        except requests.HTTPError as e:
            print("Request failed:", e)
        return resp
    
    # # Получение ID компании
    # def company_id(self):
    #     json = {
    #         "login": "sacred112rus@gmail.com",
    #         "password": "aGe2a8g4e8",
    #         "name": "SkyPro"
    #         }
    #     headers = {'Content-Type': 'application/json'}
    #     resp = requests.post(self.url+"/auth/companies", headers=headers, json=json)
    #     company_id = resp.json()
    #     return company_id["content"][0]["id"]
    
    # # Генерация нового ключа
    # def new_api_key(self):
    #     company_id = self.company_id()
    #     json = {
    #         "login": "sacred112rus@gmail.com",
    #         "password": "aGe2a8g4e8",
    #         "companyId": company_id
    #         }
    #     headers = {'Content-Type': 'application/json'}
    #     resp = requests.post(self.url+"/auth/keys", headers=headers,json=json)
    #     api_key = resp.json()["key"]
    #     return api_key

    # # Получение списка созданных ключей
    # def get_api_key_list(self):
    #     company_id = self.company_id()
    #     json = {
    #         "login": "sacred112rus@gmail.com",
    #         "password": "aGe2a8g4e8",
    #         "companyId": company_id
    #         }
    #     headers = {'Content-Type': 'application/json'}
    #     resp = requests.post(self.url+"/auth/keys/get", headers=headers,json=json)
    #     api_key_list = resp.json()
    #     return api_key_list