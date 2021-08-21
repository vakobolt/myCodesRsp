car = {
    "mark": "mercedes",
    "model": "c-class",
    "year": 2017
}
car['year']= 2012
car['fuelType']= "super"
car.pop('model') #cut delete

print(car["year"])
print(len(car))