import time

from imports import *


class Menu:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    menu_links = (By.XPATH, "//nav[@class='about-menu he']/ul[@class='menu']/li[@class='menu-item']/a")
    page_text = (By.XPATH, "//article/div/div/div/div/div/span")

    def get_menu_and_page_text(self):
        menu_items = self.driver.find_elements(*self.menu_links)
        for open in range (len(menu_items)):
            menu_items = self.driver.find_elements(*self.menu_links)
            menu_items[open].click()