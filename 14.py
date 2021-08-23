fruit = {}

def main_question ():
    helper = {}
    name = input("nter fruit name: ")
    kg = input("enter weight: ")
    price = input("enter price: ")
    helper["kg"] = kg
    helper["price"] = price
    fruit[name] = helper

main_question()

for key,value in fruit.items():
    print(kg = int(value['kg']))
    print(price = int(value['price']))