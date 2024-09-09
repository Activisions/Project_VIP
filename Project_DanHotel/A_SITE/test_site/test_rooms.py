from imports import *
from Project_DanHotel.A_SITE.page_site.rooms import Rooms

rooms_url = "https://www.danhotels.co.il/Booking/SearchResults?fr=htl&com=box&ttl=ChooseYourRoom&Lang=heb&editMode=true"


# בודק שהמלון שוהכנס תקין , וניתן לבחור תאריכי כניסה ויציאה
def test_select_hotel_menu(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.select_hotel_menu(7)
    room.select_date_menu(20, 25)
    assert room.select_hotel_menu(7) == "דן פנורמה תל אביב"


#   טסט שבוחר מלון שהתאריכים בו לא זמינים ומתקדם כל פעם חודש קדימה ובודק אם פנוי
def test_full_booking_hotel(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.select_hotel_menu(21)
    room.select_date_menu(20, 25)
    assert room.select_hotel_menu(21) == "רות צפת"


# פותח אופציה לחדרים נוספים וממלא את כל התפריטים - בודק שיש ולידציה פופ אפ לאחר התקדמות

def test_hotel_with_more_rooms(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.select_hotel_menu(7)
    room.select_date_menu(20, 25)
    assert room.AddAnotherRoom().text == "אורח יקר, התפוסה המבוקשת בחדר הראשון שבחרת אינה מתאימה לשהייה בחדר אחד. אנא פצלו את ההרכב ובצעו חיפוש מחדש."


# בודק שלא ניתן להכניס תאריך שגוי
def test_wrong_date_menu(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.select_hotel_menu(7)
    result = room.select_date_menu(30, 40)
    assert result == "הוכנס תאריך באופן שגוי"


# בודק שלא ניתן להכניס תאריך 31 כאשר אין בחודש הנוכחי תאריך כזה
def test_date31_menu(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.select_hotel_menu(7)
    result = room.select_date_menu(30, 31)
    assert result == "הוכנס תאריך באופן שגוי"


#טסט שבודק ולידציה לשדה בחירת מלון
def test_less_hotel_validation(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.Press_Price_Button()
    assert room.less_hotal_validation() == "אנא בחר מלון"


#טסט שבודק ולידציה לשדה תאריך הגעה
def test_less_chickin_validation(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.Press_Price_Button()
    assert room.less_checkin_validation() == "אנא בחר תאריך צ'ק אין"


#טסט שבודק ולידציה לשדה תאריך עזיבה
def test_less_checkout_validation(driver):
    driver.get(rooms_url)
    room = Rooms(driver)
    room.Press_Price_Button()
    assert room.less_checkout_validation() == "אנא בחר תאריך צ'ק אווט"
