ticket = int(input("Введите количество билетов:"))
sum  = 0
for i in range(ticket+1):
    if i > 0:
        age = int(input("Введите возраст посетителя:"))
        if age < 18:
              sum += 0
        elif 18 <= age <= 25:
              sum += 990
        else:
              sum += 1390
        print(sum)
if ticket >= 3:
    sum = sum*0.9
    print("Итого за билеты:", sum, 'рублей')
else:
    print("Итого за билеты:", sum, 'рублей')
