from imports import *
from Project_DanHotel.ACCOUNT.page_account.login import *

login_url = "https://www.danhotels.co.il/eDan/Login"


@pytest.fixture()
def connector(driver):
    return Login(driver)

#פונקציה שמבצעת חיבור בהצלחה
def test_login(driver, connector):
    driver.get(login_url)
    connector.login_connect()
    assert connector.error_connect_valid() is None
    print("Login succeeded")

#פונקציה שבודקת שלא ניתן להתחבר עם פרטים שגויים
def test_login2(driver, connector):
    driver.get(login_url)
    connector.login_connect("WrongMail.com", "wrong")
    assert connector.error_connect_validmail() == 'אנא בדוק תקינות דוא"ל'
    print("Not login: Detail Validation succeeded")

#פונקציה שבודקת ולידציה כאשר אין אימייל
def test_login3(driver, connector):
    driver.get(login_url)
    connector.login_connect("", "Wrong@Mail.com")
    assert connector.error_connect_lessMail() == 'אנא הכניסו דוא"ל'
    print("Not login: Less Email Validation succeeded")

#פונקציה שבודקת ולידציה כאשר אין סיסמא
def test_login4(driver, connector):
    driver.get(login_url)
    connector.login_connect("lupatest1@gmail.com", "")
    assert connector.error_connect_lessPass() == 'אנא הכניסו סיסמה'
    print("Not login: Less Password Validation succeeded")



