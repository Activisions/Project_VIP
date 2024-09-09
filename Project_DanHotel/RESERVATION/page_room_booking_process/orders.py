from imports import *



class Orders:
    def __init__(self, driver: WebDriver):
        self.driver = driver


    price = (By.XPATH,"//div[@class='price-item regular']/div[1]/span/text()")
    club_price = (By.XPATH,"//div[@class='price-item club']/div[1]/span/text()")





