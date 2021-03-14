def clear():
    new_line = "\n"
    print(new_line * 100)


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    
    travel_log.append({"country": country, "visits": visits, "cities": cities})


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print(travel_log[2]["country"])
clear()
print(travel_log[2]["visits"])
print(travel_log[2]["cities"][0])
