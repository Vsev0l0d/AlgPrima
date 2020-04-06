file = open('input.txt', "r")

core = [0]
edges = []
matrix = []
remaining = []
msd = 0

for line in file.readlines():
    matrix.append([int(item) for item in line.split()])

for i in range(1, len(matrix)):
    remaining.append(i)

for i in range(len(matrix) - 1):
    MIN = -1
    for line in core:
        for column in remaining:
            if (MIN == -1) | (MIN > matrix[line][column]):
                MIN = matrix[line][column]
                edge = [line + 1, column + 1]
                y = column
                x = line
    core.append(y)
    print("Ближайшая к ядру вершина %d. Подсоединяем ее" %(y + 1))
    remaining.remove(y)
    edges.append(edge)
    msd += matrix[x][y]
    print("Новое ребро %s" %(edge))
print("Итоговый список ребер: %s" %(edges))
print("Суммарный вес ребер МСД равен %d" %(msd))