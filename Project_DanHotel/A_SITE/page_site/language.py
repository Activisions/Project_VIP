import time

from imports import *


class language:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def language_locators(self):
        english_site_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "select-lang"))
        )
        english_link = self.driver.find_element(By.XPATH, "//*[@id=\"block-language-switcher\"]/ul/li[1]/a")

        dan_hotel_eng_logo_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/header/div/div[1]/div[1]/div/h1/a"))
        )
        eng_text_changed = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/header/div/div[1]/div[1]/div/div[1]/a"))
        )
        return english_site_button, english_link, dan_hotel_eng_logo_text, eng_text_changed

    def english_site_mood(self):
        english_site_button, link, dan_hotel_eng_logo_text, text_changed = self.language_locators()
        english_site_button.click()
        link_text = link.text
        if link_text == "ENGLISH":
            print(f" The text button to switch to the Dan Hotels site in English is: {link_text}")
        else:
            print(f" No matching text found to: {link_text}")
        link.click()

    def url_change(self):
        english_site_button, link, dan_hotel_eng_logo_text, text_changed = self.language_locators()
        original_url = self.driver.current_url
        english_site_button.click()
        link.click()
        time.sleep(3)
        new_url = self.driver.current_url
        if new_url != original_url:
            print(f"Test Passed: URL changed to {new_url}")
        else:
            print(f"Test Failed: URL changed to {original_url}, expected {new_url}")
        return new_url

    def check_element(self):
        english_site_button, english_link, dan_hotel_eng_logo_text, eng_text_changed = self.language_locators()
        return dan_hotel_eng_logo_text.text



        #assert eng_text_changed.text == "Experience The Best", f"The changed text is {eng_text_changed.text}"