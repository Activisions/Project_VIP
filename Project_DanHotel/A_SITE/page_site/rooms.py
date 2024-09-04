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
        # listdate1 = self.driver.find_elements(By.XPATH, "//*[2]/table/tbody/tr[4]/td[5]/button/div")
        # listdate1 = self.driver.find_elements(By.XPATH,"//*[@class='CalendarDay__button']")
        listdate1 = self.driver.find_elements(By.XPATH,"//*[2]/table/tbody/tr/td/*[@class='CalendarDay__button']/div[1]")
        listdate2 = self.driver.find_elements(By.XPATH,"//*[2]/table/tbody/tr/td/*[@class='CalendarDay__button']")
        nextdate = self.driver.find_element(By.XPATH,"//*[@class='DayPickerNavigation__next DayPickerNavigation__next--rtl']")
        return (listdate1,listdate2,nextdate)




################################################################


    def select_hotel_menu(self):
        self.element_find_hotel_menu_button()
        selecthotel = self.element_find_hotel_menu_list()
        selecthotel[21].click()
        time.sleep(1)


    def select_date_menu(self,date1=20,date2=22):
        listdate1,listdate2,nextdate = self.element_choose_date()
        checkdate = listdate2[date1-1].get_attribute("aria-label")
        checkdate2 = listdate2[date2-1].get_attribute("aria-label")
        print(checkdate,checkdate2)
        if checkdate.startswith("לא זמין") and checkdate2.startswith("לא זמין"):
            nextdate.click()
        else:
            listdate1[date1-1].click()
            listdate1[date2-1].click()









