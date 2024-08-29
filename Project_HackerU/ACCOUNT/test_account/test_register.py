import time

from imports import *
from Project_HackerU.ACCOUNT.page_account.register import *



register_url = "https://www.danhotels.co.il/eDan/Registration"



def test_register1(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL","TEST","0221234","0540000000","test@gmail.com")
    print("Register succeeded")

def test_register2(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("טסט","TEST","0221234","0540000000","test@gmail.com")
    error_wrong_name = driver.find_element(By.XPATH,"//*[@id='mui-1-helper-text']")
    assert error_wrong_name.text == "אנא בדוק תקינות שם פרטי באנגלית"
    print("Name validation succeeded")


def test_register3(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL","טסט","0221234","0540000000","test@gmail.com")
    error_wrong_lastname = driver.find_element(By.XPATH,"//*[@id='mui-2-helper-text']")
    assert error_wrong_lastname.text == "אנא בדוק תקינות שם משפחה באנגלית"
    print("LastName validation succeeded")



def test_register4(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL","TEST","02212345","0540000000","test@gmail.com")
    error_wrong_id = driver.find_element(By.XPATH,"//*[3]/p[@id='mui-3-helper-text']")
    assert error_wrong_id.text == "אנא בדוק תקינות ת.ז"
    print("ID validation succeeded")

def test_register5(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL","TEST","0221234","0","test@gmail.com")
    error_wrong_phone = driver.find_element(By.XPATH,"//*[@id='mui-4-helper-text']")
    assert error_wrong_phone.text == "אנא בדוק תקינות טלפון נייד"
    print("Phone validation succeeded")


def test_register6(driver):
    driver.get(register_url)
    filler = Register(driver)
    filler.register_fill("GAL","TEST","0221234","0540000000","testgmail.com")
    error_wrong_email = driver.find_element(By.XPATH,"//*[@id='mui-5-helper-text']")
    assert error_wrong_email.text == "אנא בדוק תקינות דוא\"ל"
    print("Email validation succeeded")


def test_register7(driver):
    driver.get(register_url)
    filler = Register(driver)
    register_name, register_lastname, register_id, register_phone, register_email, register_country, register_checkbox1, register_checkbox2, register_button = filler.register_locators()
    country_value = register_country.get_attribute('value')
    print(f"The value of register_country is: {country_value}")
    assert country_value == "ישראל"

def test_register8(driver):
    driver.get(register_url)
    filler = Register(driver)
    register_name, register_lastname, register_id, register_phone, register_email, register_country, register_checkbox1, register_checkbox2, register_button = filler.register_locators()
    register_checkbox2.click()
    assert driver.find_element(By.XPATH, "(//*[@data-testid='CheckBoxOutlineBlankIcon'])[2]")





