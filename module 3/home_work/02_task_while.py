a = int(input("a: "))
b = int(input("b: "))

if a > b:
    a, b = b, a

while b >= a:
    if a % 5 == 0:
        print(a)
    a += 1