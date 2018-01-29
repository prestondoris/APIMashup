from geocode import getGeocodeLocation
import json
import httplib2
import requests

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "JAL1UGFNFEMLAWL4TZXUFQYTPHDDMUB3AND4OETDSEFFC1M4"
foursquare_client_secret = "M0UPWFB0MPWC5UR5H51K3WDUXZJACCIVYX4ENUNOAOLUYYSL"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latLon = '%s, %s' % getGeocodeLocation(location)

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    url_FS = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=foursquare_client_id,
        client_secret=foursquare_client_secret,
        v='20170801',
        ll=latLon,
        query=mealType,
        intent='browse',
        radius=16000,
        limit=1
    )
    resp = requests.get(url=url_FS, params=params)
    data = json.loads(resp.text)

	#3. Grab the first restaurant
    restaurant = data['response']['venues'][0]
    venue_id = restaurant['id']
    name = restaurant['name']
    restaurant_address = restaurant['location']['formattedAddress']
    address = ""

    for i in restaurant_address:
        address += i + " "
        restaurant_address = address

	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    #5. Grab the first image
    #6. If no image is available, insert default a image url
    url_photo = 'https://api.foursquare.com/v2/venues/%s/photos' % venue_id
    photoParams = dict(
        client_id=foursquare_client_id,
        client_secret=foursquare_client_secret,
        v='20170801',
        limit=1
    )
    photoResp = requests.get(url=url_photo, params=photoParams)
    photoData = json.loads(photoResp.text)
    if photoData['response']['photos']['items']:
        photoLink = photoData['response']['photos']['items'][0]['prefix'] + '300x300' + photoData['response']['photos']['items'][0]['suffix']
    else:
        photoLink = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"

	#7. Return a dictionary containing the restaurant name, address, and image url
    restaurantInfo = {
        'name':name,
        'address':restaurant_address,
        'photo':photoLink
    }
    print restaurantInfo['name']
    print restaurantInfo['address']
    print restaurantInfo['photo']
    print
    return restaurantInfo

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
