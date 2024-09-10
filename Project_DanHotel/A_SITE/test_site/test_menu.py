from imports import *
from Project_DanHotel.A_SITE.page_site.menu import Menu

about_buttons = "https://www.danhotels.co.il/AboutDanhotels/Overview"
accessibility_buttons = "https://www.danhotels.co.il/AccessibilityStatement"



# בדיקה שעוברת על כל הפתורים בתפריט יצירת קשר
def test_menu(driver):
    driver.get(about_buttons)
    menu = Menu(driver)
    menubutton = menu.get_menu_and_page_text()
    assert menubutton == 17

# בדיקה שעוברת על כל הכפתורים בתפריט הסדרי נגישות
def test_menu2(driver):
    driver.get(accessibility_buttons)
    menu = Menu(driver)
    menubutton = menu.get_menu_and_page_text()
    assert menubutton == 18