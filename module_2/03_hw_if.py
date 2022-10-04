a1 = int(input("a1: "))
b1 = int(input("b1: "))
a2 = int(input("a2: "))
b2 = int(input("b2: "))

if a1 % 2 == a2 % 2:
    if b1 % 2 == b2 % 2:
        print("Да")
    else:
        print("Нет")
else:
    if b1 % 2 != b2 % 2:
        print("Да")
    else:
        print("Нет")
    