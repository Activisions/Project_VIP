from imports import *


def test_sdf3(driver):
    driver.get("https://www.danhotels.co.il/eDan/Login")
    mailogin_button = driver.find_element(By.XPATH, "//*[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-91lsx7']")
    mailogin_button.click()

    hold()
