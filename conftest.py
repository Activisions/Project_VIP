from imports import *


# driver = webdriver.Chrome()  אם רוצים להריץ בלי פיקסטור
@pytest.fixture(scope="session",autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument(r'--load-extension=C:\Users\ofir\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\cjpalhdlnbpafiamejdnhcphjbkeiagm\1.59.0_0')
    # chrome_options.add_argument('--window-position=-2000,0')           #לא להתייחס מיועד לפתיחת האוטומציה במסך השני
    # chrome_options.add_argument("--window-size=1920,1080")             #מיועד לפתיחת מסך ברזולוציה 24 אינץ
    # chrome_options.add_argument("--window-size=1500,900")              #מיועד לפתיחת מסך בלפטופ
    # chrome_options.add_argument('--headless')                          # אם רוצים להריץ ברקע
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()                                             # פותח את האתר על כל המסך
    # driver = webdriver.Firefox()
    yield driver
    driver.quit()

1