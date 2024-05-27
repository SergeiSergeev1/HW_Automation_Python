import requests
from EmployeeApi import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com")
    
def test_employee():
    # Создание новой компании
    name = 'SIAN Ltd'
    description = 'Service'
    result = api.new_company(name, description)
    company_id = result["id"]
    new_company = api.get_company(company_id)
    assert new_company['id'] == company_id
    # Получение списка сотруднтков компании
    list_employee_before = api.get_list_employee(company_id)
    assert len(list_employee_before) == 0
    # Создание сотрудника
    id = ""
    first_Name = "Ivan"
    last_Name = "Ivanov"
    middle_Name = "Ivanovich"
    companyId = company_id
    email = "123@test.com"
    url = "http://123@test"
    phone = "+71234567890"
    is_Active = True
    new_employee = api.create_employee(id, first_Name, last_Name, middle_Name, companyId, email, url, phone, is_Active)
    employee_id = new_employee['id']
    list_employee_after = api.get_list_employee(company_id)
    assert len(list_employee_before) < len(list_employee_after)
    assert list_employee_after[-1]['id'] == employee_id
    assert list_employee_after[-1]['firstName'] == first_Name
    assert list_employee_after[-1]['lastName'] == last_Name
    assert list_employee_after[-1]['middleName'] == middle_Name
    assert list_employee_after[-1]['companyId'] == companyId
    #assert list_employee_after[-1]['email'] == email
    assert list_employee_after[-1]['avatar_url'] == url
    assert list_employee_after[-1]['phone'] == phone
    assert list_employee_after[-1]['isActive'] == is_Active
    # Получение сотрудника по ID
    one_employee = api.get_employee_id(employee_id)
    assert one_employee['id'] == employee_id
    assert one_employee['firstName'] == first_Name
    assert one_employee['lastName'] == last_Name
    assert one_employee['middleName'] == middle_Name
    assert one_employee['companyId'] == companyId
    #assert one_employee['email'] == email
    assert one_employee['avatar_url'] == url
    assert one_employee['phone'] == phone
    assert one_employee['isActive'] == is_Active
    # Редактирование сотрудника
    edited_firstName = "Иван"
    edited_lastName = "Иванов"
    edited_middleName = "Иванович"
    edited_company_id = company_id
    edited_email = "12345@test.com"
    edited_url = "http://12345@test"
    edited_phone = "+70987654321"
    edited_isActive = False
    edited_employee = api.edit_employee( employee_id, edited_firstName, edited_lastName, edited_lastName, edited_middleName, edited_company_id, edited_email, edited_url, edited_phone, edited_isActive)
    assert edited_employee["id"] == employee_id
    assert edited_employee["email"] == edited_email
    assert edited_employee["url"] == edited_url
    assert edited_employee["isActive"] == edited_isActive
