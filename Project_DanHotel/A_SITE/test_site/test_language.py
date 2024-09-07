from imports import *
from Project_DanHotel.A_SITE.page_site.language import *

hebrew_url = "https://www.danhotels.co.il"
english_url = "https://www.danhotels.com/?_gl=1"


def test_change_language_to_english(driver):
    driver.get(hebrew_url)
    switch_to_english = language(driver)
    switch_to_english.english_site_mood()


def test_change_language_to_english_Check_url(driver):
    driver.get(hebrew_url)
    switch_to_english = language(driver)
    switch_to_english.url_change()
    assert switch_to_english.url_change() == english_url


def test_change_language_to_english_check_element(driver):
    driver.get(hebrew_url)
    switch_to_english = language(driver)
    switch_to_english.english_site_mood()
    assert switch_to_english.check_element() == "Dan Hotels"

hebrew_url = "https://www.danhotels.co.il"


def test_change_language_to_hebrew(driver):
    driver.get(english_url)


def test_change_language_to_hebrew_check_url(driver):
    driver.get(english_url)


def test_change_language_to_hebrew_check_element(driver):
    driver.get(english_url)
