from imports import *
from Project_DanHotel.RESERVATION.page_room_booking_process.hotel_room_search import *

hotel_room_search_url = "https://www.danhotels.co.il/Booking/SearchResults?fr=htl&com=box&ttl=ChooseYourRoom&Lang=heb&editMode=true"


#בדיקת לחיצה על כפתור מלון ובחירה מהרשימה
def test_room_calculator_1(driver):
    driver.get(hotel_room_search_url)
    # Wait for the page to load and the dropdown to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "selectHotel"))
    )
    choosing = choose_room(driver)
    # Ensure the dropdown is clickable and all elements are visible
    choosing.fill_room_Search_Calculator()


def test_room_calculator_2(driver):
    driver.get(hotel_room_search_url)
    choose_hotel_dropdown_element = driver.find_element(By.ID, "selectHotel-label")
    choose_hotel_text = choose_hotel_dropdown_element.text
    assert choose_hotel_text == "בחרו מלון"
    print(choose_hotel_text)


#בדיקת לחיצה על כפתור תאריך הגעה
def test_room_calculator_3(driver):
    driver.get(hotel_room_search_url)
    choosing = choose_room(driver)
    choosing.fill_date_Search_Calculator()