import time

from imports import *


class Menu:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    menu_links = (By.XPATH, "//nav[@class='about-menu he']//ul//li/a")
    # page_text = (By.XPATH, "//article/div/div/div/div/div/span")


    def get_menu_and_page_text(self):
        menu_items = self.driver.find_elements(*self.menu_links)
        for runner in range(len(menu_items)):
            if runner == 11:
                continue
            menu_items = self.driver.find_elements(*self.menu_links)
            menu_items[runner].click()

