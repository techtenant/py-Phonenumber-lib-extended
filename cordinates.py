import phonenumbers
from opencage.geocoder import OpenCageGeocode
from numberLocation import actualLocation

#API Key from OpenCageGeocode
Key = "36aa769420c748bbb122b55f3423d7c3"
geocoder = OpenCageGeocode(Key)

query = str(actualLocation)

output = geocoder.geocode(query)

#print(output)

lat = output[0]['geometry']['lat']
lng = output[0]['geometry']['lng']

print(lat, lng)

