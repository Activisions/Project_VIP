from imports import *
from Project_DanHotel.A_SITE.page_site.menu import MenuLinks


def test_homepage_hebrew(driver):
    driver.get("https://www.danhotels.co.il/")
    menulinks = MenuLinks(driver)
    menulinks.home_page_links()
    assert menulinks.home_page_links() == True


def test_hotels(driver):
    driver.get("https://www.danhotels.co.il/IsraelHotels")
    menulinks = MenuLinks(driver)
    menulinks.home_page_links()
    assert menulinks.home_page_links() == True


def test_Accessibility(driver):
    driver.get("https://www.danhotels.co.il/AccessibilityStatement")
    menulinks = MenuLinks(driver)
    menulinks.home_page_links()
    assert menulinks.home_page_links() == True


def test_contact(driver):
    driver.get("https://www.danhotels.co.il/AboutDanhotels/Contactus")
    menulinks = MenuLinks(driver)
    menulinks.home_page_links()
    assert menulinks.home_page_links() == True
