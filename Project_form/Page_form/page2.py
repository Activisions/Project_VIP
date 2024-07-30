from Project_form.conftest import *


class Page2:
    def __init__(self, driver):
        self.driver = driver
        self.driver: WebDriver = driver

    def locators2(self):
        sharper_number = self.driver.find_element(By.ID,"sharpenerCount")
        sharper_color = self.driver.find_element(By.ID,"sharpenerColor")
        image_selected = self.driver.find_elements(By.TAG_NAME,"img")
        send_key = self.driver.find_element(By.ID,"send")
        return sharper_number,sharper_color,image_selected,send_key

    def fills(self,number,color):
        sharper_number, sharper_color, image_selected, send_key = self.locators2()
        sharper_number.send_keys(number)
        sharper_color.send_keys(color)
        image_selected[2].click()
        send_key.click()


