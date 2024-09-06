import time

from imports import *




class MenuLinks():
    def __init__(self, driver):
        self.driver: WebDriver = driver

    # elements_home_page_links = (By.XPATH,"//ul[@class='menu']/li[@class='menu-item']//a")
    elements_home_page_links = (By.TAG_NAME,"a")



    def home_page_links(self):
        link_home = self.driver.find_elements(*self.elements_home_page_links)
        print(f"Number of links: {len(link_home)}")
        for linker in link_home:
            link_url = linker.get_attribute("href")
            if link_home:
                try:
                    response = requests.get(link_url)
                    status_code = response.status_code
                    if status_code == 200:
                        print(f"the link {link_url} status is {status_code}")
                    else:
                         print(f"Link {link_url} returned status code: {status_code}")

                except Exception as e:
                    print(f"error {e}")


def test_sdf(driver):
    driver.get("https://www.danhotels.co.il/")
    menulinks = MenuLinks(driver)
    menulinks.home_page_links()









    # def home_page_links(self):
    #     try:
    #         link_home = self.driver.find_elements(*self.elements_home_page_links)
    #         for cliker in link_home:
    #             argument = cliker.get_attribute('tabindex')
    #             print(argument)
    #             if argument == -1 or argument is None:
    #                 continue
    #             else:
    #                 try:
    #                     cliker.click()
    #                 except: print("not click")
    #                 time.sleep(5)
    #                 get_url = self.driver.current_url
    #                 print(get_url)
    #                 response = requests.get(get_url)
    #                 if response.status_code != 200:
    #                     print(f"The link {get_url} not receive a status code 200.")
    #                 self.driver.back()
    #                 time.sleep(5)
    #     except Exception as e:
    #             print(f"error for link: {e}")
    #
    #
