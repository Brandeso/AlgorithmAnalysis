# KP Problem with Dynamic Programming
# Instituto Politecnico Nacional
# Escuela Superior de Computo
# Analisis de Algoritmos
# Profesora: Pescador Rojas, Miriam
# Alumnos: Amezcua Arevalo, Bruno; Garcia Mendoza, Jose Luis

# Cargamos los Valores del archivo txt
with open('values.txt', 'r') as f:
    backpack = [[int(num) for num in line.split(',')] for line in f]

# Le solicitamos al usuario nos indique la capacidad de la mochila
capacity = input('Enter the backpack capacity: ')

# Creamos un arreglo de 0's, del tamanio de la capacidad y la cantidad de items
w, h = capacity + 1, len(backpack[0])
table = [[0 for x in range(w)] for y in range(h)]

# Iteramos sobre los items (filas) y sobre los pesos (columnas)
for index in range(h):
    for weight in range(w):
        # Si el peso del item es mayor que la capacidad
        if wts[index] > weight:
            table[index][weight] = table[index - 1][weight]
            continue

        # Si el peso del item es menor que la capacidad
        priorValue = table[index -1][weight]
        newValue = vls[index] + table[index-1][weight - wts[index]]
        table[index][weight] = max(priorValue, newValue)

print('Tabla llenada')
for i in range(h):
    print(table[i])
