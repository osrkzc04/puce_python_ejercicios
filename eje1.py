"Ejercicio 1: Suma de los elementos de un arreglo"
def crear_arreglo(tamaño):
    arreglo = []
    print(f"ingrese {tamaño} números enteros:")
    for i in range(tamaño):
        numero = int(input(f"elemento {i + 1}:"))
        arreglo.append(numero)
    return arreglo
def imprimir_arreglo(arreglo):
    print("arreglo:", end=" ")
    for elemento in arreglo:
        print(elemento, end=" ")
    print()
def suma_arreglo(arreglo):
    suma = 0
    for elemento in arreglo:
        suma += elemento
    return suma
if __name__ == "__main__":
    tamano = int(input("ingrese el tamaño del arreglo: "))
    arreglo = crear_arreglo(tamano)
    imprimir_arreglo(arreglo)
    resultado = suma_arreglo(arreglo)
    print("la suma de los elementos de los arreglo del arreglo es:", resultado)
    