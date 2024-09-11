import allure

from imports import *
from Project_DanHotel.A_SITE.page_site.links import Links


def test_homepage_hebrew(driver):
    driver.get("https://www.danhotels.co.il/")
    checklinks = Links(driver)
    checklink = checklinks.home_page_links()
    assert checklink == True


def test_hotels(driver):
    driver.get("https://www.danhotels.co.il/IsraelHotels")
    checklinks = Links(driver)
    checklink2 = checklinks.home_page_links()
    assert checklink2 == True


def test_Accessibility(driver):
    driver.get("https://www.danhotels.co.il/AccessibilityStatement")
    checklinks = Links(driver)
    checklink3 = checklinks.home_page_links()
    assert checklink3 == True

@allure.description("קיים באג אחד הלינקים לא תקינים")
def test_contacts(driver):
    driver.get("https://www.danhotels.co.il/AboutDanhotels/Contactus")
    checklinks = Links(driver)
    checklink4 = checklinks.home_page_links()
    assert checklink4 == True
