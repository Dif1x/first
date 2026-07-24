kolvo = int(input())
elements = []
for i in range(kolvo):
    elements.append(input())
print(elements)
for j in range(kolvo):
    if " " in elements:
        elements[j].split(" ")


