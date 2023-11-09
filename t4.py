chair_price1 = int(input('введите ценну стула №1: '))
chair_price2 = int(input('введите ценну стула №2: '))
chair_price3 = int(input('введите ценну стула №3: '))
summ = chair_price1 + chair_price3 + chair_price2
if summ >= 10000:
    print(summ - ((summ * 10) / 100))
else:
   print(summ)
