import requests
import json
import urllib.parse
import time

address=input('Enter current location:')

#Obtain and print relevant Google Maps API data

google_api='http://maps.googleapis.com/maps/api/geocode/json?'
url=google_api+urllib.parse.urlencode({'address':address})
json_data=requests.get(url).json()
json_status=json_data['status']

print ('API Status: ' + json_status)
#find location type from Google
location_type=json_data['results'][0]['geometry']['location_type']
print ('Location is:',location_type)
# get latitude and longitude parameters
lat=str(json_data['results'][0]['geometry']['location']['lat'])
long=str(json_data['results'][0]['geometry']['location']['lng'])

print ('Latitude:',lat)
print('Longitude:',long)

#Obtain and print relevant ISS data

iss_api = 'http://api.open-notify.org/iss-pass.json?'
iss_url = iss_api+('lat='+lat+'&lon='+long)
iss_data = requests.get(iss_url).json()

#obtain next flyover time and duration
flyover=int(iss_data['response'][0]['risetime'])
duration=int(iss_data['response'][0]['duration'])

print ('Unix timestamp for next risetime of ISS:',flyover)

#print converted data
print('The next time that the ISS will be visible in your region will be:',(time.ctime(flyover)))
print('The ISS will be visible for a total of approximately:',int(duration/60),'minutes and',duration%60,'seconds')



