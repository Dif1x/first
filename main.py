matrix = []
rows = int(input())
cols = int(input())
for j in range(rows):
    new_matrix = []
    for i in range(cols):
        el = int(input())
        new_matrix.append(el*2)
    matrix.append(new_matrix)
print("\n".join(map(str, matrix)))