from imports import *
from Project_DanHotel.CONTACT.page_contact.contact_Us_page import *

Contactus_url = "https://www.danhotels.co.il/AboutDanhotels/Contactus"


def test_Contactus1(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("גל", "test@gmail.com", "0530000000","test")
    print("contact succeeded")


def test_Contactus2(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("ג", "test@gmail.com", "0530000000","test")
    error_wrong_name = driver.find_element(By.ID, "edit-name-error")
    assert error_wrong_name.text == "Please enter at least 2 characters."
    print("Name validation succeeded")


def test_Contactus3(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("גל", "@.com", "0530000000","test")
    error_wrong_name = driver.find_element(By.ID, "edit-email-error")
    assert error_wrong_name.text == "אמייל does not contain a valid email."
    print("e-mail validation succeeded")


def test_Contactus4(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill_hotel("גל", "test@gmail.com", "0530000000")
    print("choosing hotel succeeded")


def test_Contactus5(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill_subject("test","test@gmail.com","0530000000")
    print("choosing subject succeeded")


def test_Contactus6(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("גל", "test@gmail.com", "0530000000","test")
    operating_Hours = driver.find_element(By.XPATH, "//*[@id=\"block-danhotel-content\"]/div/div[3]/div/div[2]/article/div/div/div[3]/div/div[2]/div/p[1]")
    assert operating_Hours.text == "ראשון-חמישי: 8:00 - 19:00"
    print("operating Hours text succeeded")