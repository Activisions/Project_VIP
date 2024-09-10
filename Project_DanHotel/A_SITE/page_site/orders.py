import time

from imports import *



class Orders:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    price = (By.XPATH,"//div[@class='price-item regular']/div[1]/span")
    club_price = (By.XPATH,"//div[@class='price-item club']/div[1]/span")
    def match_price(self):
        prices = self.driver.find_elements(*self.price)
        club_prices = self.driver.find_elements(*self.club_price)
        checker = True
        for price_element, club_price_element in zip(prices, club_prices):
            prices = int(price_element.text.replace('₪','').replace(',','').strip())
            club_prices = int(club_price_element.text.replace('₪','').replace(',','').strip())
            if club_prices > prices:
                checker = False
                print(f"price {prices} is less than club price {club_prices}")
                break

        return checker







