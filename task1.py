import math
#Выполнила Макаренко Александра Александровна, группа 44-22-120, вариант №18
def calc(x):
    if x > 1:
        y = math.sin(math.sqrt(x))
    else:
        y = math.cos(x**2)
    print("Значение y =", y)

x = int(input("Введите значение x: "))
calc(x)
