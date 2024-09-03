from imports import *


class Register:
    def __init__(self, driver):
        self.driver: WebDriver = driver

        # פונקציה שמקבלת את כל האלמנטים בדף ההרשמה

    def register_locators(self):
        register_name = self.driver.find_element(By.NAME, "firstName")
        register_lastname = self.driver.find_element(By.NAME, "lastName")
        register_id = self.driver.find_element(By.NAME, "IDNumber")
        register_phone = self.driver.find_element(By.NAME, "cellphone")
        register_email = self.driver.find_element(By.NAME, "emailAddress")
        register_country = self.driver.find_element(By.XPATH, "//input[@id='mui-7']")
        register_checkbox1 = self.driver.find_element(By.XPATH, "//*[@id='agreeTermsCheckBox']/span")
        register_checkbox2 = self.driver.find_element(By.XPATH,
                                                      "(//span[contains(@class,'MuiCheckbox-root MuiCheckbox-colorPrimary')])[2]")
        register_button = self.driver.find_element(By.ID, "progressWrapper")
        return (register_name, register_lastname, register_id, register_phone, register_email, register_country,
                register_checkbox1, register_checkbox2, register_button)

    def error_wrong_name(self):
        error_wrong_name = self.driver.find_element(By.XPATH, "//*[@id='mui-1-helper-text']")
        return error_wrong_name.text

    def error_wrong_lastname(self):
        error_wrong_lastname = self.driver.find_element(By.XPATH, "//*[@id='mui-2-helper-text']")
        return error_wrong_lastname.text

    def error_wrong_id(self):
        error_wrong_id = self.driver.find_element(By.XPATH, "//*[3]/p[@id='mui-3-helper-text']")
        return error_wrong_id.text

    def error_wrong_phone(self):
        error_wrong_phone = self.driver.find_element(By.XPATH, "//*[@id='mui-4-helper-text']")
        return error_wrong_phone.text

    def error_wrong_email(self):
        error_wrong_email = self.driver.find_element(By.XPATH, "//*[@id='mui-5-helper-text']")
        return error_wrong_email.text

    def CheckBox(self):
        box = self.driver.find_element(By.XPATH, "(//*[@data-testid='CheckBoxOutlineBlankIcon'])[2]")
        return box.is_enabled()

        # פונקציה שממלאת את דף ההרשמה, אם כפתור ההרשמה לא עבד בגלל שגיאת ולידציה היא תדפיס הודעה שלא ניתן להירשם




    def register_fill(self, first_name, last_name, id_number, phone, email):
        register_name, register_lastname, register_id, register_phone, register_email, register_country, register_checkbox1, register_checkbox2, register_button = self.register_locators()
        register_name.send_keys(first_name)
        register_lastname.send_keys(last_name)
        register_id.send_keys(id_number)
        register_phone.send_keys(phone)
        register_email.send_keys(email)
        register_checkbox1.click()
        try:
            register_button.click()
        except Exception as e:
            print("Not Register:")
