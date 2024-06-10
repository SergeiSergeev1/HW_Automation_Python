import requests

class EmployeeApi:

    def __init__(self, url):
        self.url = url

    def get_token(self,user = 'raphael', password = 'cool-but-crude'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()['userToken']

    def new_company(self, name, description):
        company = {
            'name': name,
            'description': description
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url+'/company/', json=company, headers = my_headers )
        return resp.json()
    
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()
    
    def get_list_employee(self,company_id):
        my_params = {}
        my_params = {
            'company': company_id
        }
        resp = requests.get(self.url + '/employee',params= my_params)
        return resp.json()
   
    def create_employee(self, id, first_Name, last_Name, middle_Name, companyId, email, url, phone, is_Active ):
        object = {
            "id": id,
            "firstName": first_Name,
            "lastName": last_Name,
            "middleName": middle_Name,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": is_Active
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url+'/employee', json=object, headers=my_headers)
        return resp.json()
    
    def get_employee_id(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
    
    def edit_employee(self, id, first_Name, last_Name, middle_Name, company_id, email, url, phone, is_Active):
        edit_object = {
            "id": id,
            "firstName": first_Name,
            "lastName": last_Name,
            "middleName": middle_Name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": is_Active
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.patch(self.url+'/employee/'+ str(id), json=edit_object, headers=my_headers)
        return resp.json()
