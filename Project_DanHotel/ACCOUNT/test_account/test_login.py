import time

from imports import *
from Project_DanHotel.ACCOUNT.page_account.login import *




login_url = "https://www.danhotels.co.il/eDan/Login"

#פונקציית טסט שמבצעת לוג אין בהצלחה
@pytest.fixture()
def connector(driver):
    return Login(driver)


def test_login(driver,connector):
    driver.get(login_url)
    connector.login_connect()
    assert connector.error_connect_valid() is None
    print("Login succeeded")



def test_login2(driver,connector):
    driver.get(login_url)
    connector.login_connect("WrongMail.com","wrong")
    assert connector.error_connect_validmail() == 'אנא בדוק תקינות דוא"ל'
    print("Not login: Detail Validation succeeded")



