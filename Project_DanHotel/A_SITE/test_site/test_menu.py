from imports import *
from Project_DanHotel.A_SITE.page_site.menu import Menu

urllinks = "https://www.danhotels.co.il/AboutDanhotels/Contactus"


def test_menu(driver):
    driver.get(urllinks)
    menu = Menu(driver)
    menu_texts = menu.get_menu_and_page_text()
    for menu_item_text, page_text_content in menu_texts:
        assert menu_item_text in page_text_content, f"Menu item {menu_item_text} not found in page text"