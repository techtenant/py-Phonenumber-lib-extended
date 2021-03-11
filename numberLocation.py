import phonenumbers
from myNumber import actualNumber
from phonenumbers import geocoder
from phonenumbers import timezone 



actualLocation = geocoder.description_for_number(actualNumber, "en")
print(actualLocation)

