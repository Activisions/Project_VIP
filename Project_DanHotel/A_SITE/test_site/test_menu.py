from imports import *
from Project_DanHotel.A_SITE.page_site.menu import Menu

urllinks = "https://www.danhotels.co.il/AboutDanhotels/Overview"


def test_menu(driver):
    driver.get(urllinks)
    menu = Menu(driver)
    menu.get_menu_and_page_text()
    hold()
