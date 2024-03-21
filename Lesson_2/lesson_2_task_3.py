import math

def square():
    s = (float(input('Сторона квадрата:')))
    square = (s * s)
    print('Площадь =',(math.ceil(square)))
    
square()