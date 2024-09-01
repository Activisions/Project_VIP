from imports import *



class Recover:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def recover_locators(self):
        insert_mail = self.driver.find_element(By.ID,"mui-1")
        by_sms = self.driver.find_element(By.XPATH,"(//*[@id='progress'])[1]")
        by_mail = self.driver.find_element(By.XPATH,"(//*[@id='progress'])[2]")
        return insert_mail , by_sms , by_mail


    def recover_fill1(self,email):
        insert_mail, by_sms, by_mail = self.recover_locators()
        insert_mail.send_keys(email)
        by_sms.click()

    def recover_fill2(self, email):
        insert_mail, by_sms, by_mail = self.recover_locators()
        insert_mail.send_keys(email)
        by_mail.click()


    def recover_msg_validation_email(self):
        msg_validation_email = self.driver.find_element(By.XPATH,"//*[@id='mui-1-helper-text']").text
        return msg_validation_email


    def recover_valid(self):
        # recover_class = self.driver.find_element(By.XPATH,"//*[@class='phone disabled u1st-tabbable-element']")
        recover_class = self.driver.find_element(By.ID,"progressWrapper")
        return recover_class