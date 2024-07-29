

from Project_form.conftest import *
from Project_form.Page_form.page2 import *


@pytest.mark.group2
def test_2():
    s2 = Page2()
    s2.fills(5,"כחול")