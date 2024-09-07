import time

from imports import *




class MenuLinks():
    def __init__(self, driver):
        self.driver: WebDriver = driver

    # elements_home_page_links = (By.XPATH,"//ul[@class='menu']/li[@class='menu-item']//a")
    elements_home_page_links = (By.TAG_NAME,"a")


#
    def home_page_links(self):
        link_home = self.driver.find_elements(*self.elements_home_page_links)
        print(f"Number of links: {len(link_home)}")
        all_links_valid = True
        for linker in link_home:
            link_url = linker.get_attribute("href")
            if link_url:
                try:
                    response = requests.get(link_url)
                    status_code = response.status_code
                    if status_code == 200:
                        1#print(f"the link {link_url} status is {status_code}")      #Turn on if you want see all links
                    else:
                        # print(f"Link {link_url} returned status code: {status_code}")
                        all_links_valid = False


                except Exception as e:
                  1# print(f"error {e}")
        return all_links_valid










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
