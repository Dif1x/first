print("Выбери действие:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n5 - остаток от деления")
vibor = int(input())
if vibor == 1:
    b = float(input("Введите первое значение: "))
    c = float(input("Введите второе значение: "))
    res = b+c
    print(res)
if vibor == 2:
    b = float(input("Введите первое значение: "))
    c = float(input("Введите второе значение: "))
    res = b-c
    print(res)
if vibor == 3:
    b = float(input("Введите первое значение: "))
    c = float(input("Введите второе значение: "))
    res = b*c
    print(res)
if vibor == 4:
    b = float(input("Введите первое значение: "))
    c = float(input("Введите второе значение: "))
    res = b/c
    print(res)
if vibor == 5:
    b = float(input("Введите первое значение: "))
    c = float(input("Введите второе значение: "))
    res = b%c
    print(res)
