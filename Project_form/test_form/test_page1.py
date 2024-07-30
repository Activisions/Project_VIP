from imports import *
from Project_form.Page_form.page1 import *


@pytest.mark.group2
def test_1(driver) :
    s1 = Page1(driver)
    s1.fill("daniel","levy","0501234567","a@a.com")
    f_name, l_name, phone_number, email, radio, btn_step2 = s1.locators()
    assert radio.get_attribute("value") == "דרום"

