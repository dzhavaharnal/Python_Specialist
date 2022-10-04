n = int(input("n: "))
ed = n % 10
des = n // 10 % 10

if des != 1  and ed == 1: 
    print (f"На лугу пасется {n} корова")
elif des != 1 and ed <= 4:
    print (f"На лугу пасется {n} коровы")
else:
    print (f"На лугу пасется {n} коров")