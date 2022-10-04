n = int(input("n: "))

if n % 3 ==0 or n % 5 == 0:
    print ("Да")
elif (n % 5) % 3 == 0 or (n % 3) % 5 == 0:
    print ("Да")
else:
    print("Нет")
    