cost = float(input("cost: "))
n = int(input("n: "))
i = 1

while i <= n:
    print(f"{i} {cost * i} рублей")
    i += 1