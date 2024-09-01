import time

from imports import *
from Project_DanHotel.ACCOUNT.page_account.recover import *

recover_url = "https://www.danhotels.co.il/eDan/Login"


@pytest.fixture()
def recovers(driver):
    return Recover(driver)


# בדיקה ששליחת שחזור חשבון עם מייל תקין עוברת
def test_recover1(driver, recovers):
    driver.get(recover_url)
    recovers.recover_fill1("lupatest1@gmail.com")
    actual_mail = recovers.recover_valid()
    recover_msg = actual_mail.get_attribute('class')
    assert recover_msg == "phone disabled"


# בדיקה שקיים ולידציה למייל לא תקין דרך כפתור שחזור בSMS
def test_recover2(driver, recovers):
    driver.get(recover_url)
    recovers.recover_fill1("test@@gmail.com")
    actual_text = recovers.recover_msg_validation_email()
    assert actual_text == 'אנא בדוק תקינות כתובת אימייל'


# בדיקה שקיים ולידציה שאין כתובת מייל דרך כפתור שחזור בSMS
def test_recover3(driver, recovers):
    driver.get(recover_url)
    recovers.recover_fill1("")
    actual_text = recovers.recover_msg_validation_email()
    assert actual_text == "אנא הכניסו כתובת אימייל"


# בדיקה שקיים ולידציה למייל לא תקין דרך כפתור שחזור במייל
def test_recover4(driver, recovers):
    driver.get(recover_url)
    recovers.recover_fill2("test@@gmail.com")
    actual_text = recovers.recover_msg_validation_email()
    assert actual_text == 'אנא בדוק תקינות כתובת אימייל'


# בדיקה שקיים ולידציה שאין כתובת מייל דרך כפתור שחזור במייל
def test_recover5(driver, recovers):
    driver.get(recover_url)
    recovers.recover_fill2("")
    actual_text = recovers.recover_msg_validation_email()
    assert actual_text == "אנא הכניסו כתובת אימייל"
