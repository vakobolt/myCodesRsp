#biggining of first project
array = [-1] * 10

num = 20
count = 0

for i in range(20):
    if (num % 2 == 1):
        array[count] = num
        count = count + 1
    num = num + 1

print(array) 
print("***************************")

#biggining of second projct
list = []

a = int(input("insert first number: "))
b = int(input("insert second number: "))

if a > b:
    a, b = b, a
elif a == b:
    print("Error 404")

while a <= b:
    if a % 2 == 0:
        list.append(a)
        a += 2
    else:
        a += 1

print(list)