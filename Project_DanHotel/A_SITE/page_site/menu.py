import time

from imports import *


class Menu:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    menu_links = (By.XPATH, "//nav[@class='about-menu he']//ul//li/a")
    tagame = (By.XPATH,"//article/div/div/div[1]/div/div/span")


    def get_menu_and_page_text(self):
        menu_items = self.driver.find_elements(*self.menu_links)
        for runner in range(len(menu_items)):
            if runner == 11:
                continue
            menu_items = self.driver.find_elements(*self.menu_links)
            compare = menu_items[runner].text
            menu_items[runner].click()
            tagame = self.driver.find_element(*self.tagame)
            tagame_text = tagame.text
            if compare not in tagame_text:
                print(f"Need fix menu title: {tagame_text}")
        return len(menu_items)

