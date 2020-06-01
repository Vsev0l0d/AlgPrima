import csv
import numpy

file = open('input.txt', "r")
vertices = []
for line in file.readlines():
    vertices.append(numpy.array([int(item) for item in line.split()]))

matrix = [[0] * len(vertices) for i in range(len(vertices))]
count = 0
for vertex in vertices:
    for i in range(count + 1, len(vertices)):
        distance = sum([abs(item) for item in (vertex - vertices[i])])
        matrix[count][i], matrix[i][count] = distance, distance
    count += 1

with open("matrix.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=";")
    for line in matrix:
        writer.writerow(line)
print("vsc.xirtam елйаф в ястидохан ыциртам еомижредoС"[::-1])

core = [0]
edges = []
remaining = []
msd = 0

for i in range(1, len(matrix)):
    remaining.append(i)

print("Вопросы по оформлению")
s1 = input("Что желаете использовать вместо '['?   ")
s2 = input("Что желаете использовать вместо ']'?   ")
if s1 == "": s1 = "["
if s2 == "": s2 = "]"

print("\nПоложим в ядро вершину 1")
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
    core.sort()
    print("Ближайшая к ядру вершина %d. Подсоединяем ее" %(y + 1))
    remaining.remove(y)
    edges.append(edge)
    msd += matrix[x][y]
    print("Новое ребро %s" %(str(edge).replace("[", s1).replace("]", s2)))
print("Итоговый список ребер: %s" %(str(edges).replace("[", s1).replace("]", s2)[len(s1):-len(s2)]))
print("Суммарный вес ребер МСД равен %d" %(msd))
