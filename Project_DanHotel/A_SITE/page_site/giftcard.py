import time

from imports import *



class Giftcard:
    def __init__(self, driver):
        self.driver: WebDriver = driver


    def gift_price_element(self):
        wait = WebDriverWait(self.driver, 50)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "giftcard-sum-giftcard-text")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        giftprice_number = self.driver.find_element(By.XPATH, "//*[@id='giftcard-sum-input']")
        giftprice_button = self.driver.find_element(By.ID,"giftcard-sum-button")
        return giftprice_number , giftprice_button

    def gift_price_fiil(self,gift):
        try:
            giftprice_number, giftprice_button = self.gift_price_element()
            giftprice_number.send_keys(gift)
            giftprice_button.click()
        except: print("הכנס מספר בלבד / כפולות של 100 בלבד")

    def gift_card_price(self):
        try:
         self.driver.implicitly_wait(5)
         price_for_pay = self.driver.find_element(By.XPATH, "//*[@class='giftcard-item-price-num']").text
         return int(price_for_pay)
        except: None




class Send_Giftcard:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def send_gift_element(self):
        try:
            giftcard_form_send_to = self.driver.find_element(By.ID,"giftcard-form-send-to")
            giftcard_form_given_from = self.driver.find_element(By.ID,"giftcard-form-given-from")
            giftcard_form_send_cong = self.driver.find_element(By.ID,"giftcard-form-send-cong")
            when_sending_button1 = self.driver.find_element(By.XPATH,"(//input[@name='IsImmidiate'])[1]")
            when_sending_button2 = self.driver.find_element(By.XPATH,"(//input[@name='IsImmidiate'])[2]")
            giftcard_form_sender_email = self.driver.find_element(By.ID,"giftcard-form-sender-email")
            regulation_field = self.driver.find_element(By.XPATH,"//*[@class='MuiTypography-root MuiTypography-body1 MuiFormControlLabel-label css-fcvvuz']/span")
            giftcard_form_submit = self.driver.find_element(By.ID,"giftcard-form-submit")
            bymail__button = self.driver.find_element(By.NAME,"showEmail")
            bysms__button = self.driver.find_element(By.NAME,"showSms")
            return giftcard_form_send_to, giftcard_form_given_from, giftcard_form_send_cong, when_sending_button1, when_sending_button2, giftcard_form_sender_email, regulation_field, giftcard_form_submit, bymail__button, bysms__button

        except Exception as e:
            print(f"An error occurred: {e}")
            return giftcard_form_send_to, giftcard_form_given_from, giftcard_form_send_cong, when_sending_button1, when_sending_button2, giftcard_form_sender_email, regulation_field, giftcard_form_submit, bymail__button, bysms__button



    def send_gift_fill1(self,for_w="ofir",from_m="daniel",my_text="Just Gift Just Enjoy",m_mail="test@test.com"):
        giftcard_form_send_to, giftcard_form_given_from, giftcard_form_send_cong, when_sending_button1, when_sending_button2, giftcard_form_sender_email, regulation_field, giftcard_form_submit, bymail__button, bysms__button = self.send_gift_element()
        giftcard_form_send_to.send_keys(for_w)
        giftcard_form_given_from.send_keys(from_m)
        giftcard_form_send_cong.send_keys(my_text)
        when_sending_button1.is_selected()
        giftcard_form_sender_email.send_keys(m_mail)
        regulation_field.click()
        giftcard_form_submit.click()


    def credit_card_element(self):
        textcreditguardt = self.driver.find_element(By.XPATH, "//div[@class='giftcard-title']/h2")
        return textcreditguardt.text

