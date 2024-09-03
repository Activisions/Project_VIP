from imports import *


def test_sdf3(driver):
    driver.get('https://www.danhotels.co.il/Booking/SearchResults?fr=htl&com=box&ttl=ChooseYourRoom&Lang=heb&editMode=true')

    wait = WebDriverWait(driver, 10)
    date_picker = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="datePickerInput"]')))
    date_picker.click()

    # Example: Select a specific date from the date picker
    # Adjust the XPath according to the actual structure of the date picker
    desired_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//td[@data-date="2024-09-15"]')))
    desired_date.click()

    # Perform any additional actions, such as selecting a check-out date or submitting the form

    # Close the browser
    driver.quit()
    hold()


