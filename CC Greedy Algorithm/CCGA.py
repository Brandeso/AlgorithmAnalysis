# Coin Change Problem with Greedy Algorithm
# Instituto Politecnico Nacional
# Escuela Superior de Computo
# Analisis de Algoritmos
# Profesora: Pescador Rojas, Miriam
# Alumnos: Amezcua Arevalo, Bruno; Garcia Mendoza, Jose Luis

import time

# Cargamos los Valores del archivo txt
with open('values2.txt', 'r') as f:
    for line in f:
        coins = [int(num) for num in line.split(',')]

# Le pedimos al usuario nos indique el cambio a devolver
change = input('Introduzca el cambio a devolver: ')

# Inicilizamos una tabla en 0 en la que guardaremos las monedas totales
table = [0 for x in range(len(coins))]

# Inicializamos un arreglo que contendra el cambio
ans = []

start_time = time.time()
while change > 0:
    for i in range(len(coins)):
        while coins[i] <= change:
            change -= coins[i]
            ans.append(coins[i])
            table[i] += 1
end_time = time.time() - start_time

print('---------- %s s ---------' % end_time)
print(coins)
print(table)