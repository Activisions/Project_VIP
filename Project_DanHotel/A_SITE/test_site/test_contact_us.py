import pytest

from Project_DanHotel.A_SITE.page_site.contact_us import *

Contactus_url = "https://www.danhotels.co.il/AboutDanhotels/Contactus"


#@pytest.mark.skip
#@allure.description("קוד בתיקון של גל")
def test_Contactus1(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("גל", "test@gmail.com", "0530000000", "test")
    check_text = contact_filler.contact_us_fill_text()
    expected_message = "צור קשר"
    assert check_text == expected_message
    print("contact succeeded")


#@pytest.mark.skip
#@allure.description("קוד בתיקון של גל")
def test_Contactus2(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("ג", "@.com", "0530000000", "test")
    check_error_name, check_error_email = contact_filler.contact_us_fill_text_errors()
    expected_message = "Please enter at least 2 characters."
    expected_email = "אמייל does not contain a valid email."
    assert check_error_name == expected_message
    assert check_error_email == expected_email
    print("Name and email validation succeeded")


@pytest.mark.skip
@allure.description("קוד בתיקון של גל")
def test_Contactus3(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill("גל", "@.com", "0530000000", "test")
    check_text, check_error_name, check_error_email = contact_filler.contact_us_fill_text()
    expected_message = "אמייל does not contain a valid email."
    assert check_error_email == expected_message
    print("e-mail validation succeeded")


@pytest.mark.skip
@allure.description("קוד בתיקון של גל")
def test_Contactus4(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill_hotel("גל", "test@gmail.com", "0530000000")
    print("choosing hotel succeeded")


@pytest.mark.skip
@allure.description("קוד בתיקון של גל")
def test_Contactus5(driver):
    driver.get(Contactus_url)
    contact_filler = contact_Us(driver)
    contact_filler.contact_us_fill_subject("test", "test@gmail.com", "0530000000")
    print("choosing subject succeeded")


@pytest.mark.skip
@allure.description("קוד בתיקון של גל")
def test_Contactus6(driver):
    driver.get(Contactus_url)
    #operating_Hours = driver.find_element(By.XPATH, "//*[@id=\"block-danhotel-content\"]/div/div[3]/div/div[2]/article/div/div/div[3]/div/div[2]/div/p[1]")
    # operating_Hours = operating_Hours.text
    # assert operating_Hours == "ראשון-חמישי: 8:00 - 19:00"
    # print(operating_Hours)
