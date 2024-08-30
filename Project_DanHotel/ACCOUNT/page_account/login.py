from imports import *




class Login:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    def login_locators(self):
         mailogin_button = self.driver.find_element(By.XPATH, "//*[@class='MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary css-91lsx7']").click()
         login_mail = self.driver.find_element(By.ID,"mui-2")
         login_password = self.driver.find_element(By.ID,"mui-3")
         login_button = self.driver.find_element(By.ID,"progress")
         return login_mail, login_password, login_button


    def login_connect(self, email="lupatest1@gmail.com", password="a123123a"):
        login_mail, login_password, login_button = self.login_locators()
        login_mail.send_keys(email)
        login_password.send_keys(password)
        login_button.click()


