import googlemaps
from pprint import pprint  # 印出排版整齊的 dict 或 JSON 資料

API_KEY = 'YOUR_API_KEY'


if __name__ == '__main__':
    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode(" place ")
    pprint(geocode_result)

    loc = geocode_result[0]['geometry']['location']
    places = gmaps.places_radar(keyword="item", location=loc, radius=r)['results']
    print("the number of item from radius r: " + str(len(places)))
    print("first")
    pprint(places[0])

    print("first detail")
    p = gmaps.place(place_id=places[0]['place_id'], language='zh-TW')#['result']
    pprint(p)
