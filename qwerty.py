slov = {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
print(slov)
keys = slov.keys()
find = input()
if find in keys:
    print(slov[find])
else:
    print("ключ не существует")
