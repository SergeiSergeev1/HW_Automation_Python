
def is_year_leap ():
    y = input('Високосный год: ')
    if int(y) % 4 == 0:
        print("Год " + str(y)+":" + "True")
    else:
        print("Год " + str(y)+":" + "False")
is_year_leap()






