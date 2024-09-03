from Project_DanHotel.A_SITE.page_site.rooms import Rooms
from imports import *



rooms_url = "https://www.danhotels.co.il/Booking/SearchResults?fr=htl&com=box&ttl=ChooseYourRoom&Lang=heb&editMode=true"


def test_test(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.select_hotel_menu()
    room.select_date_menu()
    hold()

