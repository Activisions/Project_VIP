from imports import *
from Project_DanHotel.A_SITE.page_site.language import *

hebrew_url = "https://www.danhotels.co.il"
english_url = "https://www.danhotels.com/"


def test_change_language_to_english(driver):
    driver.get(hebrew_url)
    switch_to_english = language(driver)
    switch_to_english.english_site_mood()


def test_change_language_to_english_Check_url(driver):
    driver.get(hebrew_url)
    switch_to_english = language(driver)
    switch_to_english.url_change()


def test_change_language_to_english_check_element(driver):
    driver.get(hebrew_url)
    switch_to_english = language(driver)
    switch_to_english.check_element()
    assert dan_hotel_eng_logo_text.text == "Dan Hotels", f"The title of the site is {dan_hotel_eng_logo_text.text}"
    assert eng_text_changed.text == "Experience The Best", f"The changed text is {eng_text_changed.text}"


hebrew_url = "https://www.danhotels.co.il"


def test_change_language_to_hebrew(driver):
    driver.get(english_url)


def test_change_language_to_hebrew_check_url(driver):
    driver.get(english_url)


def test_change_language_to_hebrew_check_element(driver):
    driver.get(english_url)
