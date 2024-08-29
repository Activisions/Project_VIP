from imports import *


def test_sdf3(driver):
    driver.get("https://www.danhotels.co.il/eDan/Registration")
    driver.find_element(By.XPATH,"(//span[contains(@class,'MuiCheckbox-root MuiCheckbox-colorPrimary')])[2]").click()
    hold()
