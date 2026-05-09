# 8-6
def city_country(city, country):
    c_c = f"{city.title()}, {country.title()}"
    return c_c
print(city_country("city1", "country1"))
print(city_country("city2", "country2"))
print(city_country("city3", "country3"))
print()

# 8-7
def make_album(artist, title, song_n=None):
    if song_n:
        album = {"artist": artist, "title": title, "song_n": song_n}
    else:
        album = {"artist": artist, "title": title}
    return album
print(make_album("a1", "t1"))
print(make_album("a2", "t2", song_n=2))
print(make_album("a3", "t3", 3))
print()

# 8-8
def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album
while True:
    print("Please provide information about album:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == "q":
        break
    title = input("Title: ")
    if title == "q":
        break
    print(f"Album: {make_album(artist, title)}\n")
print()
