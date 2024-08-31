from imports import *
from Project_DanHotel.RESERVATION.page_room_booking_process.hotel_room_search import *

hotel_room_search_url = "https://www.danhotels.co.il/"


def test_choose1(driver):
    driver.get(hotel_room_search_url)
    choosing = choose_room(driver)
    choosing.choose_room_select_1()
    print("choosing room succeeded")