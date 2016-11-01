import random

while True:
    answer = int(raw_input("Koliko stevil naj zgeneriram? "))

    zgenerirana_stevila = []

    count = 0

    while (count != answer):
       zgenerirana_stevila.append (random.randint(1,100))
       count = count + 1

    print(zgenerirana_stevila)

    konec = raw_input("Naj se generiram stevila? da/ne ")
    if konec == "ne":
        break

print("END")