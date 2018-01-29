import httplib2
import json

def getGeocodeLocation(inputString):
    googAPIKey = 'AIzaSyDxMT02HL9LLRklV2yA30YmXR8ceTqfDQ0'
    locationString = inputString.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (locationString, googAPIKey)
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)
