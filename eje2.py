"Ejercicio 2: Buscar el número más grande y más pequeño en un arreglo bidimensional"
def crear_matriz(filas, columnas):
    matriz = []
    print(f"ingrese los elementos de la matriz ({filas}x{columnas}):")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"elemento [{i + 1}][{j + 1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz
def imprimir_matriz(matriz):
    print("matriz:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
            print()
def encontrar_min_max(matriz):
    minimo = matriz[0][0]
    maximo = matriz[0][0]

    for fila in matriz:
        for elemento in fila:
            if elemento < minimo:
                minimo = elemento
            if maximo > elemento:
                maximo = elemento
    return minimo, maximo
if __name__ == "__main__":
    filas = int(input("ingrese el número de filas de la matriz: "))
    columnas = int(input("ingrese el número de las columnas de la matriz: "))

    matriz = crear_matriz(filas, columnas)
    imprimir_matriz(matriz)

    minimo, maximo = encontrar_min_max(matriz)
    print("el numero más pequeño de la martiz es:", minimo)
    print("el numero más grande de la martiz es:", maximo)
