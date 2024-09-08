from imports import *


class contact_Us:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def contact_locators(self):
        contact_name = self.driver.find_element(By.XPATH, "//*[@id=\"edit-name\"]")
        contact_email = self.driver.find_element(By.XPATH, "//*[@id=\"edit-email\"]")
        contact_phone = self.driver.find_element(By.XPATH, "//*[@id=\"edit-phone\"]")
        choose_hotel_dropdown = self.driver.find_element(By.NAME, "hotel_name")
        choose_hotel = self.driver.find_element(By.XPATH, "//*[@id=\"edit-hotel-name\"]/option[3]")
        choose_subject_dropdown = self.driver.find_element(By.ID, "edit-subject")
        choose_subject = self.driver.find_element(By.XPATH, "//*[@id=\"edit-subject\"]/option[5]")
        contact_note = self.driver.find_element(By.ID, "edit-message")
        contact_button = self.driver.find_element(By.NAME, "op")
        self.driver.execute_script("arguments[0].scrollIntoView();",contact_button)
        return contact_name, contact_email, contact_phone, choose_hotel_dropdown, choose_hotel, choose_subject_dropdown, choose_subject, contact_note, contact_button

    #פונקציה למילוי פרטים (טלפון ,אימייל ,טלפון)
    def contact_us_fill(self, name, email, phone, nots):
        contact_name, contact_email, contact_phone, choose_hotel_dropdown, choose_hotel, choose_subject_dropdown, choose_subject, contact_note, contact_button = self.contact_locators()
        contact_name.send_keys(name)
        contact_email.send_keys(email)
        contact_phone.send_keys(phone)
        contact_note.send_keys(nots)
        # contact_button.click()

    #פונקציה למילוי פרטים (עם בחירת מלון בלבד)
    def contact_us_fill_hotel(self, name, email, phone):
        contact_name, contact_email, contact_phone, choose_hotel_dropdown, choose_hotel, choose_subject_dropdown, choose_subject, contact_note, contact_button = self.contact_locators()
        contact_name.send_keys(name)
        contact_email.send_keys(email)
        contact_phone.send_keys(phone)
        choose_hotel_dropdown.click()
        choose_hotel.click()
        # contact_button.click()

    #פונקציה למילוי פרטים (עם בחירת נושא בלבד)
    def contact_us_fill_subject(self, name, email, phone):
        contact_name, contact_email, contact_phone, choose_hotel_dropdown, choose_hotel, choose_subject_dropdown, choose_subject, contact_note, contact_button = self.contact_locators()
        contact_name.send_keys(name)
        contact_email.send_keys(email)
        contact_phone.send_keys(phone)
        choose_subject_dropdown.click()
        choose_subject.click()
        # contact_button.click()
