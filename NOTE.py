from imports import *




class Rooms:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find_hotel_menu_elements_button(self):
        listHotel = self.driver.find_element(By.ID, "selectHotel")
        listHotel.click()

    def find_hotel_menu_elements2_list(self):
        selecthotel = self.driver.find_elements(By.XPATH, "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']//li")
        return selecthotel

    def find_hotel_menu(self):
        self.find_hotel_menu_elements_button()
        selecthotel = self.find_hotel_menu_elements2_list()
        selecthotel[6].click()

    def click_button_if_available(self, xpath):
        buttons = self.driver.find_elements(By.XPATH, xpath)
        for button in buttons:
            aria_label = button.get_attribute("aria-label")
            if aria_label and not aria_label.startswith("לא זמין"):
                button.click()
                return True
        return False

    def process_buttons(self):
        xpath = "(//*/button/div[1])[17]"
        if self.click_button_if_available(xpath):
            daniel_button = self.driver.find_element(By.ID, "daniel")
            aria_label = daniel_button.get_attribute("aria-label")
            if aria_label and not aria_label.startswith("לא זמין"):
                daniel_button.click()
            else:
                print("הכפתור 'daniel' לא זמין")


def test_test(driver):
    rooms_url = "https://example.com"  # החלף עם ה-URL של האתר שלך
    driver.get(rooms_url)

    room = Rooms(driver)
    room.find_hotel_menu()
    room.process_buttons()