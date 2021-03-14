'''
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
               "total_visits": 12
               },
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
                "total_visits": 12
               },
}


print(travel_log)
print(travel_log["France"])
print(travel_log["France"]["cities_visited"][1])
print(travel_log["Germany"]["cities_visited"][2])
'''

travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
    },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 12
    },
]

print(travel_log[0]["cities_visited"][1])
