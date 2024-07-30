from Project_form.imports import *
from Project_form.Page_form.page2 import *


@pytest.mark.group2
def test_2(driver):
    s2 = Page2(driver)
    s2.fills(5,"כחול")