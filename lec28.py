letter = "hey my name is {} and I am from{}"
country = "india"
name = "harry"

print(letter.format(country, name))
print(f"hey my name is {name} and I am from {country}")


txt = "for only {price:.2f} dollars!"
price = 49
print(txt)
#print(txt.format(price=price))
print(type(f"{2*8}"))