from imports import *


class Menu:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    menu_links = (By.XPATH, "//nav[@class='about-menu he']/ul[@class='menu']/li[@class='menu-item']/a")
    page_text = (By.XPATH, "//article/div/div/div/div/div/span")

    def get_menu_and_page_text(self):
        menu_items = self.driver.find_elements(*self.menu_links)
        result = []

        for i in range(len(menu_items)):
            # Refetch the menu items in each iteration to avoid stale element references
            menu_items = self.driver.find_elements(*self.menu_links)
            item = menu_items[i]

            # Click each menu item
            item.click()

            # Wait for the page text to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.page_text)
            )

            # Get the text from the page and menu item
            page_text_content = self.driver.find_element(*self.page_text).text
            menu_item_text = item.text

            # Store the menu item text and page text for pytest assertions
            result.append((menu_item_text, page_text_content))

        return result