import phonenumbers
from myNumber import actualNumber
from phonenumbers import timezone 


# Pass the parsed phone number in below function 
timeZone = timezone.time_zones_for_number(actualNumber) 
  
# It print the timezone of a phonenumber 
print(timeZone) 