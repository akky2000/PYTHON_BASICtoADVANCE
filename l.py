import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+918235662402")
phone_number2=phonenumbers.parse("+916202578710")
phone_number3=phonenumbers.parse("+91952381953")
phone_number4=phonenumbers.parse("+919060034095")

print("\n Phone Numbers Location\n")


print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))