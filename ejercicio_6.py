# Descripción: Escribe las siguientes funciones
# función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números pares.
# función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números impares.

def crear_lista():
    try:
        fila = int(input("Ingrese la cantidad de elementos que desea ingresar: "))
        lista = [0]*fila
        for i in range(0,fila):
            elemento = int(input(f"Ingrese un número para el elemento {i+1}: "))
            lista[i]= elemento
        return lista
    except ValueError:
        print("Ha ingresado un dato inconrrecto.")
    
def numeros_pares(lista):
    pares = []
    for i in range(0, len(lista)):
        if(lista[i]%2==0):
            pares.append(lista[i])
    return pares

def numeros_impares(lista):
    impares = []
    for i in range(0, len(lista)):
        if(lista[i]%2!=0):
            impares.append(lista[i])
    return impares

def imprimir_lista(lista):
    print(lista)

lista = crear_lista()

if(lista!=None):
    lista_pares = numeros_pares(lista)
    lista_impares = numeros_impares(lista)
    print("Lista de números pares: ")
    imprimir_lista(lista_pares)
    print("Lista de números impares: ")
    imprimir_lista(lista_impares)