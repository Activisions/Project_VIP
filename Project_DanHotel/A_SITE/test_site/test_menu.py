import time

from imports import *
from Project_DanHotel.A_SITE.page_site.menu import MenuLinks






def test_sdf(driver):
    driver.get("https://www.danhotels.co.il/")
    menulinks = MenuLinks(driver)
    time.sleep(5)
    menulinks.home_page_links()
