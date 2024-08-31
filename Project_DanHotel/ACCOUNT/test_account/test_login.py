from imports import *
from Project_DanHotel.ACCOUNT.page_account.login import *




login_url = "https://www.danhotels.co.il/eDan/Login"

#פונקציית טסט שמבצעת לוג אין בהצלחה

def test_login(driver):
    driver.get(login_url)
    connector = Login(driver)
    connector.login_connect()
    hold()

