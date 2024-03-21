def month_to_season():
    m = int(input('Месяц: '))
    if (m == 12) or  (m == 1) or (m == 2):
        print('"Зима"')
    elif (m == 3) or  (m == 4) or (m == 5):
        print('"Весна')
    elif (m == 6) or  (m == 7) or (m == 8):
        print('"Лето')
    elif(m == 9) or  (m == 10) or (m == 11):
        print('"Осень')
    else:
        print("Такого сезона нет!")
month_to_season()

    
    




