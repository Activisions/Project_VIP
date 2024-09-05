from imports import *




class MenuLinks():
    def __init__(self, driver):
        self.driver: WebDriver = driver

    elements_home_page_links = (By.XPATH,"//ul[@class='menu']/li[@class='menu-item']//a")









    def home_page_links(self):
        link_home = self.driver.find_elements(*self.elements_home_page_links)
        for cliker in link_home:
            try:
                if cliker.get_attribute('tabindex') == "-1":
                    continue
                else: cliker.click()
                get_url = self.driver.current_url
                response = requests.get(get_url)
                if response.status_code != 200:
                    print(f"The link {get_url} not receive a status code 200.")
                self.driver.back()
            except Exception as e:
                print(f"error for link {cliker.text} {get_url}: {e}")







def test_sdf(driver):
    driver.get("https://www.danhotels.co.il/")
    menulinks = MenuLinks(driver)
    menulinks.home_page_links()


