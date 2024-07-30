from Project_form.imports import *



class Page1:
    def __init__(self, driver):
        self.driver = driver
        self.driver: WebDriver = driver
    def locators(self):
        f_name = self.driver.find_element(By.ID, 'firstName')
        l_name = self.driver.find_element(By.ID, 'lastName')
        phone_number = self.driver.find_element(By.ID, 'phone')
        email = self.driver.find_element(By.ID, 'email')
        btn_step2 = self.driver.find_element(By.ID, 'btn_step2')
        radio = self.driver.find_element(By.ID,"center")
        return (f_name, l_name, phone_number, email, radio, btn_step2,)

    def fill(self, first_name, last_name, phone, email):
        self.driver.get("https://danielauto.net/practice/sales/sales.html")
        f_name, l_name, phone_number, mail, radio, btn_step2 = self.locators()
        f_name.send_keys(first_name)
        l_name.send_keys(last_name)
        phone_number.send_keys(phone)
        mail.send_keys(email)
        radio.click()
        btn_step2.click()
        time.sleep(1)

