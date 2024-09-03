import time

from imports import *



class Rooms:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    def element_find_hotel_menu_button(self):
        listHotel = self.driver.find_element(By.ID, "selectHotel")
        return listHotel.click()

    def element_find_hotel_menu_list(self):
        selecthotel = self.driver.find_elements(By.XPATH,"//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']//li")
        return selecthotel


    def element_choose_date(self):
        listdate1 = self.driver.find_element(By.XPATH, "//label[contains(text(), 'בחר חמישי, 26 בספטמבר 2024')]")
        # listdate1 = self.driver.find_elements(By.XPATH,"//*[@class='CalendarDay__button']")
        return listdate1.click()




################################################################


    def select_hotel_menu(self):
        self.element_find_hotel_menu_button()
        selecthotel = self.element_find_hotel_menu_list()
        selecthotel[6].click()
        time.sleep(1)


    def select_date_menu(self):
        listdate1 = self.element_choose_date()



        # checklist1 = listdate1[date1].get_attribute("aria-label")
        # checklist2 = listdate2[date2].get_attribute("aria-label")


        # if checklist1.startswith("לא זמין") or checklist2.startswith("לא זמין"):
        #     nextdate.click()
        # else:
        #     listdate1[date1].click()
        #     listdate2[date2].click()




# nextdate = self.driver.find_element(By.XPATH,"/button[@class='DayPickerNavigation__next DayPickerNavigation__next--rtl']")











