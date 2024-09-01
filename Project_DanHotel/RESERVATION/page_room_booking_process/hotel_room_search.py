from imports import *


class choose_room:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    #פנקציה לזיהוי אלמנטים בעמוד חיפוש חדר
    def choose_room_locators(self):
        select_Hotel_dropdown = self.driver.find_element(By.CLASS_NAME, "selectHotel u1st-tabbable-element")
        Dan_Eilat_Hotel = self.driver.find_element(By.ID,"u1st-b0a17e3d-7ae8-4537-b09e-89e451fcef62")
        check_in_button = self.driver.find_element(By.XPATH,"//*[@id=\"startDate\"]")
        check_in_select_date = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-94239538-45b4-4263-9b53-d2962dfc9e78\"]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[3]/td[1]/button")
        check_out_button = self.driver.find_element(By.XPATH,"//*[@id=\"endDate\"]")
        check_out_select_date = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-94239538-45b4-4263-9b53-d2962dfc9e78\"]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr[4]/td[7]/button")
        adult_number_dropdown = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-94239538-45b4-4263-9b53-d2962dfc9e78\"]/div[3]/div[1]/div/div/svg")
        num_one_adult_choose = self.driver.find_element(By.XPATH,"//*[@id=\"menu-\"]/div[3]/ul/li[1]")
        add_more_room = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-92fc3100-1d4d-4461-a5be-33605be05224\"]/div[3]/div[2]/span")
        remove_room_button = self.driver.find_element(By.ID,"u1st-353126a2-5e02-4b2d-b186-69e2658209c6")
        adult_add_more_room_dropdown = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-92fc3100-1d4d-4461-a5be-33605be05224\"]/div[3]/div[2]/div/div[2]/div/div/div/div")
        num_two_adult_dropdown_choose = self.driver.find_element(By.XPATH,"//*[@id=\"menu-\"]/div[3]/ul/li[3]")
        children_add_more_room_dropdown = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-5851f6b2-0a8d-4edf-86ac-daf565cb6105\"]/div[3]/div[2]/div/div[3]/div/div/div/div")
        num_three_children_dropdown_choose = self.driver.find_element(By.XPATH,"//*[@id=\"menu-\"]/div[3]/ul/li[4]")
        baby_add_more_room_dropdown = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-5851f6b2-0a8d-4edf-86ac-daf565cb6105\"]/div[3]/div[2]/div/div[4]/div/div/div/div")
        num_one_baby_dropdown_choose = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-5851f6b2-0a8d-4edf-86ac-daf565cb6105\"]/div[3]/div[2]/div/div[4]/div/div/div/div")
        search_button = self.driver.find_element(By.XPATH,"//*[@id=\"u1st-94239538-45b4-4263-9b53-d2962dfc9e78\"]/div[5]")
        return select_Hotel_dropdown,Dan_Eilat_Hotel,check_in_button,check_in_select_date,check_out_button, check_out_select_date,adult_number_dropdown, num_one_adult_choose,add_more_room,remove_room_button,adult_add_more_room_dropdown,num_two_adult_dropdown_choose,children_add_more_room_dropdown,num_three_children_dropdown_choose,baby_add_more_room_dropdown,num_one_baby_dropdown_choose,search_button


    def choose_room_select_1(self):
        select_Hotel_dropdown, Dan_Eilat_Hotel, check_in_button, check_in_select_date, check_out_button, check_out_select_date, adult_number_dropdown, num_one_adult_choose, add_more_room, remove_room_button, adult_add_more_room_dropdown, num_two_adult_dropdown_choose, children_add_more_room_dropdown, num_three_children_dropdown_choose, baby_add_more_room_dropdown, num_one_baby_dropdown_choose, search_button = self.choose_room_locators()
        select_Hotel_dropdown.click()