# import time
# import requests
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
#
#
# class MenuLinks2():
#     def __init__(self, driver):
#         self.driver: WebDriver = driver
#
#     elements_home_page_links = (By.XPATH,"//ul[@class='menu']/li[@class='menu-item']//a")
#
#
#     def home_page_links2(self):
#         try:
#             link_home = self.driver.find_elements(*self.elements_home_page_links)
#             for cliker in link_home:
#                 argument = cliker.get_attribute('tabindex')
#                 print(argument)
#                 if argument == -1 or argument is None:
#                     continue
#                 else:
#                     try:
#                         cliker.click()
#                         time.sleep(5)
#                         get_url = self.driver.current_url
#                         print(get_url)
#                         response = requests.get(get_url)
#                         if response.status_code != 200:
#                             print(f"The link {get_url} not receive a status code 200.")
#                         self.driver.back()
#                         time.sleep(5)
#                     except: print("not click")
#         except Exception as e:
#                 print(f"error for link: {e}")
#
#
# def test_h(driver):
#     driver.get("https://www.danhotels.co.il/IsraelHotels")
#     menulinks2 = MenuLinks2(driver)
#     menulinks2.home_page_links2()
