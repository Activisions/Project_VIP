from imports import *


# driver = webdriver.Chrome() אם רוצים להריץ בלי פיקסטור
@pytest.fixture(scope="session",autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument(r'--load-extension=C:\Users\ofir\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.59.0_0')
    # chrome_options.add_argument('--window-position=-2000,0')  #with maximize
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--window-size=1500,900")
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # driver = webdriver.Firefox()
    yield driver
    driver.quit()





#                       @pytest.mark.skip()                                              דילוג טסט
#                       @pytest.mark.dependency()                            תלויות מגדירים בראשון
#                       @pytest.mark.dependency(depends=["test_"])                    מגדירים בשני
#                       @pytest.mark.flaky(reruns=3)                              ניסיוניות חוזרות




# Page Object Model (POM)
# class Name:
#     def __init__(self, driver):
#         self.driver = driver
#         self.driver: WebDriver = driver