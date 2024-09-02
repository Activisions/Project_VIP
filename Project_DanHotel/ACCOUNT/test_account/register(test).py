import time

from imports import *
from Project_DanHotel.ACCOUNT.page_account.register import *

register_url = "https://www.danhotels.co.il/eDan/Registration"


def test_register1(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL", "TEST", "0221234", "0540000000", "test@gmail.com")
    register_name, register_lastname, register_id, register_phone, register_email, register_country, register_checkbox1, register_checkbox2, register_button = filler.register_locators()
    time.sleep(1)
    assert register_button.get_attribute('class') == "u1st-tabbable-element"
    print("Register succeeded")

def test_register1(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL", "TEST", "0221234", "0540000000", "test@gmail.com")
    register_page = RegisterPage(driver)
    register_button = register_page.get_register_button()
    time.sleep(1)
    assert register_button.get_attribute('class') == "u1st-tabbable-element"
    print("Register succeeded")

def test_register2(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("טסט", "TEST", "0221234", "0540000000", "test@gmail.com")
    register_page = RegisterPage(driver)
    error_wrong_name = register_page.get_error_wrong_name()
    assert error_wrong_name.text == "אנא בדוק תקינות שם פרטי באנגלית"
    print("Name validation succeeded")



def test_register3(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL", "טסט", "0221234", "0540000000", "test@gmail.com")
    register_page = RegisterPage(driver)
    error_wrong_lastname = register_page.get_error_wrong_lastname()
    assert error_wrong_lastname.text == "אנא בדוק תקינות שם משפחה באנגלית"
    print("LastName validation succeeded")


def test_register4(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL", "TEST", "02212345", "0540000000", "test@gmail.com")
    register_page = RegisterPage(driver)
    error_wrong_id = register_page.get_error_wrong_id()
    assert error_wrong_id.text == "אנא בדוק תקינות ת.ז"
    print("ID validation succeeded")




def test_register5(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL", "TEST", "0221234", "0", "test@gmail.com")
    register_page = RegisterPage(driver)
    error_wrong_phone = register_page.get_error_wrong_phone()
    assert error_wrong_phone.text == "אנא בדוק תקינות טלפון נייד"
    print("Phone validation succeeded")



def test_register6(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL", "TEST", "0221234", "0540000000", "testgmail.com")
    register_page = RegisterPage(driver)
    error_wrong_email = register_page.get_error_wrong_email()
    assert error_wrong_email.text == "אנא בדוק תקינות דוא\"ל"
    print("Email validation succeeded")


def test_register7(driver):
    driver.get(register_url)
    filler = Register(driver)
    register_page = RegisterPage(driver)
    country_value = register_page.get_country_value().get_attribute('value')
    assert country_value == "ישראל"
    print(f"The value of register_country is: {country_value}")


def test_register8(driver):
    driver.get(register_url)
    filler = Register(driver)
    register_page = RegisterPage(driver)
    checkbox2 = register_page.get_checkbox2()
    checkbox2.click()
    is_selected = register_page.get_checkbox2().is_selected()
    assert not is_selected
    print("Checkbox state validation succeeded")