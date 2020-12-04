from city import City

city_a = City("City A", 987500, 7, 12000)
city_b = City("City B", 100000, 4, 11000 )

print(city_a)
print(city_b)
City.advance_year(city_a, city_b, 30)
City.advance_year(city_b, city_a, 30)
print(city_a)
print(city_b)