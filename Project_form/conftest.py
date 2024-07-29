import pdb
import time
import driver
import pytest
import pyautogui
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller, Key     #keyboard = Controller()
from pynput.mouse import Controller, Button
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from openpyxl import workbook, load_workbook
from selenium.webdriver.chrome.webdriver import WebDriver


# driver = webdriver.Chrome() אם רוצים להריץ בלי פיקסטור
@pytest.fixture(scope="session",autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'--load-extension=C:\Users\ofir\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.58.0_0')
    # chrome_options.add_argument('--window-position=-2000,0')  #with maximize
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--window-size=1500,900")
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # driver = webdriver.Firefox()
    yield driver
    driver.quit()




def hold():
    pdb.set_trace()




#                       @pytest.mark.skip()                                              דילוג טסט
#                       @pytest.mark.dependency()                            תלויות מגדירים בראשון
#                       @pytest.mark.dependency(depends=["test_"])                    מגדירים בשני
#                       @pytest.mark.flaky(reruns=3)                              ניסיוניות חוזרות




# Page Object Model (POM)
# class Name:
#     def __init__(self, driver):
#         self.driver = driver
#         self.driver: WebDriver = driver