print(" калькулятор!\n для выхода напишите exit")
while True:
    virash = input("Введите выражение: ")
    if virash.lower() == "exit":
        print("конец")
        break
    try:
        result = eval(virash)
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Ошибка, деление на ноль!")
        continue
    except Exception:
        print("Ошибка, некорректное выражение!")
        continue