def city_country(city, country, population=""):
    if population:
        name = f"{city.title()}, {country.title()} - population {population}"
    else:
        name = f"{city}, {country}".title()
    return name
