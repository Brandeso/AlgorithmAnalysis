# Coin Change Problem with Dynamic Programming
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

# Invertimos el arreglo de las monedas
coins.reverse()

# Creamos una tabla de tamanio monedasxcambio
w, h = change + 1, len(coins)
table = [[0 for x in range(w)] for y in range(h)]

start_time = time.time()
for i in range(h):
    for j in range(w):
        if i == 0 and j > 0:
            table[i][j] = 1 + table[i][j-1]
        else: 
            if coins[i] <= j:
                table[i][j] = min(table[i-1][j], 1 + table[i][j-coins[i]])
            else: 
                table[i][j] = table[i-1][j]
end_time = time.time() - start_time

ans = []
for i in range(len(coins)):
    ans.append(table[i][change])

print('---------- %s s ----------' % end_time)
print(coins)
print(ans)
print('El minimo de monedas para regresar el cambio es: %s' % min(ans))