import time

from imports import *



class Orders:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    price = (By.XPATH,"//div[@class='price-item regular']/div[1]/span")
    club_price = (By.XPATH,"//div[@class='price-item club']/div[1]/span")

    def match_price(self):
        price = self.driver.find_elements(*self.price)
        for matches in range(len(price)):
            price = self.driver.find_elements(*self.price)
            print(price[matches].text)


    def match_price(self):
        price = self.driver.find_elements(*self.price)
        for matches in price:
            print(matches.text)



def test_match_price(driver):
    driver.get("https://www.danhotels.co.il/Booking/SearchResults?fr=hp&com=box&ttl=ChooseYourRoom&SelectedHotelID=10118&ListHotelIds=10118&CheckIn=19.09.2024&CheckOut=20.09.2024&Pax[0].Adults=2&Pax[0].Children=0&Pax[0].Infants=0&site=dan")
    match = Orders(driver)
    time.sleep(9)
    match.match_price()





