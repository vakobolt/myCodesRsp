fruit = {}
trueFalse = True

def main_question ():
    helper = {}
    name = input("enter fruit name: ")
    kg = input("enter weight: ")
    price = input("enter price: ")
    helper["kg"] = kg
    helper["price"] = price
    fruit[name] = helper
    print(fruit)

while trueFalse == True:
    
    main_question()

    ques = ""
    while True:
        ques = input("want more fruit? y/n: ")
        if ques == "y":
            break
        elif ques == "n":
            trueFalse = False
            break
        else:
            print("enter correct character ")

print("its Your basket")
print("***************")

result = int

for key,value in fruit.items():
    kg = int(value['kg'])
    price = int(value['price'])
    result = kg*price
    print(key, "your amount is", result, "GEL" )

print("You entirely have to pay", result, "GEL")