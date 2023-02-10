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

def add_new_country(country_name, no_of_visits, cities_visited):
  new_add = {}

  new_add["country"] = country_name
  new_add["visits"] = no_of_visits
  new_add["cities"] = cities_visited
  travel_log.append(new_add)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)

