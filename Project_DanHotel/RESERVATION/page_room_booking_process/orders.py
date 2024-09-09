import time

from imports import *



class Orders:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    price = (By.XPATH,"//div[@class='price-item regular']/div[1]/span")
    club_price = (By.XPATH,"//div[@class='price-item club']/div[1]/span")

    # def match_price(self):
    #     price = self.driver.find_elements(*self.price)
    #     for matches in range(len(price)):
    #         price = self.driver.find_elements(*self.price)
    #         print(price[matches].text)


    # def match_price(self):
    #     price = self.driver.find_elements(*self.price)
    #     club_price = self.driver.find_elements(*self.club_price)
    #     checker = True
    #     for matches in price:
    #         price = matches.text
    #         for matches2 in club_price:
    #             club_price = matches2.text
    #             if price < club_price:
    #                 checker = False
    #                 print("מחיר מועדון גדול ממחיר אתר")
    #             else:
    #                 print("הבדיקה עברה בהצלחה")
    #     return checker

    def match_price(self):
        prices = self.driver.find_elements(*self.price)
        club_prices = self.driver.find_elements(*self.club_price)
        checker = True
        for price_element in prices:
            price_value = int(price_element.text.replace('₪', '').replace(',', '').strip())
            for club_price_element in club_prices:
                club_price_value = int(club_price_element.text.replace('₪', '').replace(',', '').strip())
                if club_price_value > price_value:
                    checker = False
                    print(f"price {price_value} club {club_price_value}")
                    return checker

        print("הבדיקה עברה בהצלחה")
        return checker


def test_match_price(driver):
    driver.get("https://www.danhotels.co.il/Booking/SearchResults?fr=hp&com=box&ttl=ChooseYourRoom&SelectedHotelID=10118&ListHotelIds=10118&CheckIn=19.09.2024&CheckOut=20.09.2024&Pax[0].Adults=2&Pax[0].Children=0&Pax[0].Infants=0&site=dan")
    match = Orders(driver)
    time.sleep(9)
    match.match_price()





