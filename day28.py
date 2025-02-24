#f-string


letter="my name is {} and i am from {}"

name="akash"
country="INDIA"

print(letter.format(name,country))

#instead of this format method we can use f-string
print(f"hey my name is {name} and i am from {country}")