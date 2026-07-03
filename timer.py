import time

a = int(input("Сколько секунд отсчитать? "))
for i in range(a):
    print(i+1)
    time.sleep(1)