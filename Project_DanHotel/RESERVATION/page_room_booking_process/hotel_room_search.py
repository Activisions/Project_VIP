from imports import *


class choose_room:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    #פנקציה לזיהוי אלמנטים בעמוד "מחשבון" חיפוש חדר
    def scroll_to_element(self, element):
        """Scrolls to a specific element."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def Room_Search_calculator_locators(self):
        # Wait for the dropdown element to be present and clickable
        select_Hotel_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "selectHotel"))
        )

        # Scroll to the dropdown to make sure it's in view
        self.scroll_to_element(select_Hotel_dropdown)
        select_Hotel_dropdown.click()

        # Waiting for a specific condition
        dan_hotel_jerusalem = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@id='menu-']//div"))
        )
        return select_Hotel_dropdown, dan_hotel_jerusalem

    def fill_room_Search_Calculator(self):
        select_Hotel_dropdown, dan_hotel_jerusalem = self.Room_Search_calculator_locators()
        if len(dan_hotel_jerusalem) > 1:
            # Ensure the element is visible before clicking
            self.scroll_to_element(dan_hotel_jerusalem[1])

            # Click using JavaScript
            self.driver.execute_script("arguments[0].click();", dan_hotel_jerusalem[1])
        else:
            print(f"Error: Not enough elements found. Found {len(dan_hotel_jerusalem)} elements.")


        #פנקציה לזיהוי אלמנטים בעמוד "מחשבון" חיפוש תאריך
    def date_Search_calculator_locators(self):
        check_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "startDate"))
        )
        return check_in_button

    def fill_date_Search_Calculator(self):
        check_in_button = self.date_Search_calculator_locators()
        if check_in_button:
            check_in_button.click()
        else:
            print("Check-in button is not available")

    #    adult_number_dropdown = self.driver.find_element(By.XPATH,
    #                                                     "//*[@id=\"u1st-94239538-45b4-4263-9b53-d2962dfc9e78\"]/div[3]/div[1]/div/div/svg")
    #    num_one_adult_choose = self.driver.find_element(By.XPATH, "//*[@id=\"menu-\"]/div[3]/ul/li[1]")
    #    add_more_room = self.driver.find_element(By.XPATH,
    #                                             "//*[@id=\"u1st-92fc3100-1d4d-4461-a5be-33605be05224\"]/div[3]/div[2]/span")
    #   remove_room_button = self.driver.find_element(By.ID, "u1st-353126a2-5e02-4b2d-b186-69e2658209c6")
    #    adult_add_more_room_dropdown = self.driver.find_element(By.XPATH,
    #                                                            "//*[@id=\"u1st-92fc3100-1d4d-4461-a5be-33605be05224\"]/div[3]/div[2]/div/div[2]/div/div/div/div")
    #    num_two_adult_dropdown_choose = self.driver.find_element(By.XPATH, "//*[@id=\"menu-\"]/div[3]/ul/li[3]")
    #    children_add_more_room_dropdown = self.driver.find_element(By.XPATH,
    #                                                               "//*[@id=\"u1st-5851f6b2-0a8d-4edf-86ac-daf565cb6105\"]/div[3]/div[2]/div/div[3]/div/div/div/div")
    #    num_three_children_dropdown_choose = self.driver.find_element(By.XPATH, "//*[@id=\"menu-\"]/div[3]/ul/li[4]")
    #    baby_add_more_room_dropdown = self.driver.find_element(By.XPATH,
    #                                                           "//*[@id=\"u1st-5851f6b2-0a8d-4edf-86ac-daf565cb6105\"]/div[3]/div[2]/div/div[4]/div/div/div/div")
    #    num_one_baby_dropdown_choose = self.driver.find_element(By.XPATH,
    #                                                            "//*[@id=\"u1st-5851f6b2-0a8d-4edf-86ac-daf565cb6105\"]/div[3]/div[2]/div/div[4]/div/div/div/div")
    #    search_button = self.driver.find_element(By.XPATH,
    #                                             "//*[@id=\"u1st-94239538-45b4-4263-9b53-d2962dfc9e78\"]/div[5]")
