t = int(input("seconds: "))
d = t // (24 * 3600)
t_left = t - d * 24 * 3600
h = t_left // 3600
t_left = t_left - h * 3600
m = t_left // 60
t_left = t_left - m * 60

print(f"{d} дней {h} часов {m} минут {t_left} секунд")
