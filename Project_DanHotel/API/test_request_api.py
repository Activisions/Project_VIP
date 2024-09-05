from imports import *


def test_dan_post_co_il():
    response = requests.get("https://www.danhotels.co.il")
    assert response.status_code == 200

def test_dan_post_com():
    response = requests.get("https://www.danhotels.com/")
    assert response.status_code == 200

def test_dan_post_gourmet():
    response = requests.get("https://www.dangourmet.co.il/")
    assert response.status_code == 200

