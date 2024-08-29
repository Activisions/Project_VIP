from imports import *


class Register:
    def __init__(self, driver):
        self.driver = driver
        self.driver: WebDriver = driver


    def register_locators(self):

        register_name = self.driver.find_element(By.NAME,"firstName")
        register_lastname = self.driver.find_element(By.NAME,"lastName")
        register_id = self.driver.find_element(By.NAME,"IDNumber")
        register_phone = self.driver.find_element(By.NAME,"cellphone")
        register_email = self.driver.find_element(By.NAME,"emailAddress")
        register_country = self.driver.find_element(By.XPATH,"//input[@id='mui-7']")
        register_checkbox1 = self.driver.find_element(By.XPATH,"//*[@id='agreeTermsCheckBox']/span")
        register_checkbox2 = self.driver.find_element(By.XPATH,"(//span[contains(@class,'MuiCheckbox-root MuiCheckbox-colorPrimary')])[2]")
        register_button = self.driver.find_element(By.ID,"progress")
        return register_name,register_lastname,register_id,register_phone,register_email,register_country, register_checkbox1, register_checkbox2, register_button

    def register_fill(self, first_name, last_name, id_number, phone, email):
        register_name,register_lastname,register_id,register_phone,register_email,register_country, register_checkbox1, register_checkbox2, register_button = self.register_locators()
        register_name.send_keys(first_name)
        register_lastname.send_keys(last_name)
        register_id.send_keys(id_number)
        register_phone.send_keys(phone)
        register_email.send_keys(email)
        register_checkbox1.click()
        register_button.click()
