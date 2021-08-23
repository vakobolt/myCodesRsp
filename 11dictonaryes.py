fruit = {}

while True:
    if len(fruit) == 0:
        name = input("enter fruit name: ")
        kg = input("nter fruit weight in kg: ")
        fruit[name] = kg
    else:
        print("this is your cart", fruit)

        ques = input("do you want more? y/n: ")
        if ques == "y":
            name = input("enter fruit name: ")
            kg = input("enter fruit weight: ")
            fruit[name] = kg
        else:
            break
print("this is your cart: ", fruit)