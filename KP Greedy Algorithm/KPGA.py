# KP Problem with Greedy Algorithm
# Instituto Politecnico Nacional
# Escuela Superior de Computo
# Analisis de Algoritmos
# Profesora: Pescador Rojas, Miriam
# Alumnos: Amezcua Arevalo, Bruno; Garcia Mendoza, Jose Luis

import operator

# Cargamos los Valores del archivo txt
with open('values.txt', 'r') as f:
    backpack = [[int(num) for num in line.split(',')] for line in f]
n = len(backpack[0])
# Definimos los valores, los pesos y las relaciones
wts = backpack[0]
vls = backpack[1]
vnw = list(backpack[1])
for i in range(n):
    vnw[i] = float(vls[i])/float(wts[i])

# Le solicitamos al usuario nos indique la capacidad y el numero de objetos de la mochila
capacity = input('Enter the backpack capacity: ')

# Creamos un arreglo de arreglos y lo ordenamos
l=[]
for i in range(n):
    l.append([vls[i], wts[i], vnw[i]])

l = sorted(l, reverse=True, key=operator.itemgetter(2))

print(l)
# Definimos el valor maximo 
maxP = 0
fracObj = 0

# Definimos una tabla con los valores que tomaremos
table = [0 for x in range(n)]

for i in range (n):
    if capacity > 0 and l[i][1] < capacity:
        capacity -= l[i][1]
        maxP += l[i][0]
        table[i] = 1
    else:
        fracObj = i
        break

if capacity > 0:
    maxP += capacity*(l[fracObj][0])/(l[fracObj][1])
    table[fracObj] = float(capacity*(l[fracObj][0])/(l[fracObj][1]))/float(l[fracObj][0])

print(maxP, table)