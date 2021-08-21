basket = {}
trueFalse = True
jami = 0

while trueFalse == True:
    sum = {}
    
    fruit = input("choice fruit: ")
    kg = float(input("choice weight: "))
    price = float(input("enter price: "))

    jami += price * kg

    sum[kg] = price
    basket[fruit] = sum

    print(basket)

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

result = 0
for key,value in basket.items():
    #print(key, value)
    result += kg*price
    print(key, "your amount is", price, "GEL" )
    #result = result + price
print("You have to pay", result, jami, "GEL")
