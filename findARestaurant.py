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
    url_FS = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
        client_id=foursquare_client_id,
        client_secret=foursquare_client_secret,
        v='20170801',
        ll=latLon,
        query=mealType,
        limit=1
    )
    resp = requests.get(url=url_FS, params=params)
    data = json.loads(resp.text)
    print data

	#3. Grab the first restaurant
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url

if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	#findARestaurant("Tacos", "Jakarta, Indonesia")
	#findARestaurant("Tapas", "Maputo, Mozambique")
	#findARestaurant("Falafel", "Cairo, Egypt")
	#findARestaurant("Spaghetti", "New Delhi, India")
	#findARestaurant("Cappuccino", "Geneva, Switzerland")
	#findARestaurant("Sushi", "Los Angeles, California")
	#findARestaurant("Steak", "La Paz, Bolivia")
	#findARestaurant("Gyros", "Sydney Australia")
