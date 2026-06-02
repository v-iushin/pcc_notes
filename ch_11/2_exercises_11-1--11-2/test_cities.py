from city_functions import *

def test_city_country():
    name = city_country("santiago", "chile")
    assert name == "Santiago, Chile"

def test_city_country_population():
    name = city_country("santiago", "chile", "5000000")
    assert name == "Santiago, Chile - population 5000000"
