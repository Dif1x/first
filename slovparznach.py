n = int(input())
a = {}
for _ in range(n):
    key = input()
    value = int(input())
    a[key] = value
newa = dict(map(lambda item: (item[0], item[1]), a.items()))
for key, value in newa.items():
    print(key, "-", value)