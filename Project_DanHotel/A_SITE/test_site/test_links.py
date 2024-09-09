from imports import *
from Project_DanHotel.A_SITE.page_site.links import Links


def test_homepage_hebrew(driver):
    driver.get("https://www.danhotels.co.il/")
    checklinks = Links(driver)
    checklinks.home_page_links()
    assert checklinks.home_page_links() == True


def test_hotels(driver):
    driver.get("https://www.danhotels.co.il/IsraelHotels")
    checklinks = Links(driver)
    checklinks.home_page_links()
    assert checklinks.home_page_links() == True


def test_Accessibility(driver):
    driver.get("https://www.danhotels.co.il/AccessibilityStatement")
    checklinks = Links(driver)
    checklinks.home_page_links()
    assert checklinks.home_page_links() == True


def test_contact(driver):
    driver.get("https://www.danhotels.co.il/AboutDanhotels/Contactus")
    checklinks = Links(driver)
    checklinks.home_page_links()
    assert checklinks.home_page_links() == True
