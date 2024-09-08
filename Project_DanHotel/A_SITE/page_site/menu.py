import time

from imports import *




class MenuLinks():
    def __init__(self, driver):
        self.driver: WebDriver = driver

    elements_home_page_links = (By.TAG_NAME,"a")



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