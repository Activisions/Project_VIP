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
        listdate1 = self.driver.find_elements(By.XPATH,"//*[2]/table/tbody/tr/td/*[@class='CalendarDay__button']/div[1]")
        listdate2 = self.driver.find_elements(By.XPATH, "//*[2]/table/tbody/tr/td/*[@class='CalendarDay__button']")
        nextmonth = self.driver.find_element(By.XPATH,"//*[@class='DayPickerNavigation__next DayPickerNavigation__next--rtl']")
        return (listdate1, listdate2, nextmonth)


    AddAnotherRoomButton = (By.CLASS_NAME, "addAnother")
    AddRoomMenu = (By.XPATH,"//div[@class='MuiSelect-select MuiSelect-outlined MuiOutlinedInput-input MuiInputBase-input css-qiwgdb']")
    AddRoomClick = (By.XPATH, "//li[3]/span")
    CheckPriceButton = (By.CLASS_NAME, "updateRates")

    Errorvalidation_CheckPriceButton = (By.XPATH, "//*[@class='small-modal inner_content_text']/div[@class='innerBody']")
    error_hotel_valid = (By.CLASS_NAME, "errors errHotel")
    error_checkin_valid = (By.CLASS_NAME, "errors"[1])
    error_checkout_valid = (By.CLASS_NAME, "errors"[2])




    #################################testlist###############################


    def select_hotel_menu(self,hotel):
        self.element_find_hotel_menu_button()
        selecthotel = self.element_find_hotel_menu_list()
        hotelname = selecthotel[hotel].text
        selecthotel[hotel].click()
        time.sleep(1)
        return hotelname

    def select_date_menu(self, CheckIN, CheckOUT):
        try:
            while True:
                time.sleep(1)
                listdate1, listdate2, nextmonth = self.element_choose_date()
                outdate = "לא זמין"
                checkdate = listdate2[CheckIN - 1].get_attribute("aria-label")
                checkdate2 = listdate2[CheckOUT - 1].get_attribute("aria-label")
                if checkdate.startswith(outdate) and checkdate2.startswith(outdate):
                    nextmonth.click()
                else:
                    break
            print(checkdate, checkdate2)
            listdate1[CheckIN - 1].click()
            listdate1[CheckOUT - 1].click()
        except: return "הוכנס תאריך באופן שגוי"

    def AddAnotherRoom(self):
        self.driver.find_element(*self.AddAnotherRoomButton).click()
        for x in range(0, 7):
            if x == 0:
                continue
            ADDROOM = self.driver.find_elements(*self.AddRoomMenu)
            ADDROOM[x].click()
            self.driver.find_element(*self.AddRoomClick).click()
        self.driver.find_element(*self.CheckPriceButton).click()
        time.sleep(1)
        textvalid = self.driver.find_element(*self.Errorvalidation_CheckPriceButton)
        return textvalid
