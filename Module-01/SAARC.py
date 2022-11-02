saarc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Srilanka"]

# print(saarc)
# print(saarc[0])

# print("Number of countries in saarc:",len(saarc))

# "Bangladesh" in saarc

country = input("Enter the name of the country: ")
if country in saarc:
    print(country, "is a member of SAARC")
else:
    print(country, "is not a member of SAARC")