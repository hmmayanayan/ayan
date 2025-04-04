import random

data = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunluğu = int(input("Parola uzunluğunu giriniz"))

parola = ""

for i in range(parola_uzunluğu):
    parola += random.choice(data)

print(parola)
