from imports import *
from Project_DanHotel.A_SITE.page_site.language import *




hebrew_url = "https://www.danhotels.co.il"
english_url = "https://www.danhotels.com/"

def test_change_language_to_english(driver):
    driver.get(hebrew_url)

def test_change_language_to_english_Check_url(driver):
    driver.get(hebrew_url)


def test_change_language_to_english_check_element(driver):
    driver.get(hebrew_url)




hebrew_url = "https://www.danhotels.co.il"




def test_change_language_to_hebrew(driver):
    driver.get(english_url)


def test_change_language_to_hebrew_check_url(driver):
    driver.get(english_url)


def test_change_language_to_hebrew_check_element(driver):
    driver.get(english_url)