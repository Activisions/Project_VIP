from imports import *
from Project_HackerU.ACCOUNT.page_account.register import *



register_url = "https://www.danhotels.co.il/eDan/Registration"



def test_register1(driver):
    driver.get(register_url)
    filler = Register(driver)
    register_name, register_lastname, register_id, register_phone, register_email, register_country, register_checkbox1, register_checkbox2, register_button = filler.register_locators()
    filler.register_fill("GAL","TEST","0221234","0540000000","test@gmail.com")




# def test_register10(driver):
#     driver.get(register_url)
#     filler = Register(driver)
#     register_name, register_lastname, register_id, register_phone, register_email, register_country, register_checkbox1, register_checkbox2, register_button = filler.register_locators()
#     country_value = register_country.get_attribute('value')
#     print(f"The value of register_country is: {country_value}")
#     assert country_value == "ישראל"






























# input_element = driver.find_element(By.XPATH, "//input[@id='mui-7']")
#
# # קבלת הערך של האלמנט
# value =  register_country.get_attribute('value')
#
# # אסרט שהערך הוא "ישראל"
# assert value == 'ישראל'