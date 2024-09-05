from imports import *
from Project_DanHotel.A_SITE.page_site.giftcard import *

giftcard_url = "https://www.danhotels.co.il/GiftCard"


# פונקציה שבודקת שסכום הקופון שהוזן הוא הסכום לתשלום, רצה בלולאה ומכפילה את הסכום במאה ואוספת למערך כדי לוודא שהכל נכנס תקין
def test_gift_card(driver):
    results = []
    for i in range(1, 10):
        driver.get(giftcard_url)
        giftcard = Giftcard(driver)
        amount = int(100 * i)
        giftcard.gift_price_fiil(amount)
        counter = giftcard.gift_card_price()
        results.append(counter)
        print(counter)
    assert sum(results) == 4500


# בדיקה שמכניסה סכום בודקת מחיר וממלאת את הטופס ושולחת, מאשרת שמגיעה למסך תשלום
def test_gift_card1(driver):
    driver.get(giftcard_url)
    giftcard = Giftcard(driver)
    giftcard.gift_price_fiil("100")
    send_giftcard = Send_Giftcard(driver)
    send_giftcard.send_gift_fill1()
    creditguard_text = send_giftcard.credit_card_element()
    assert creditguard_text == "תשלום באמצעות כרטיס אשראי"


# בדיקה שבודקת שלא ניתן להכניס סכום שהוא לא כפולות של 100 או לא מספר
def test_gift_card2(driver):
    driver.get(giftcard_url)
    giftcard = Giftcard(driver)
    giftcard.gift_price_fiil("101")
    assert pytest.raises(ValueError)


# פונקציה שבודקת שלא ניתן להתקדם בלי מייל תקין
def test_gift_card3(driver):
    driver.get(giftcard_url)
    giftcard = Giftcard(driver)
    giftcard.gift_price_fiil("100")
    send_giftcard = Send_Giftcard(driver)
    send_giftcard.send_gift_fill1("ofir","test","i want this hotel now !","asdf@sadf")
    send_giftcard.credit_card_element()
    creditguard_text1 = send_giftcard.credit_card_element()
    assert creditguard_text1 == "משלוח וברכה"
