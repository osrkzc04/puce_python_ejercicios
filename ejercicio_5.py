# Ejercicio 5: Invertir un lista
#Descripción: Escribe una función que reciba un lista de números enteros y retorne otro lista con los elementos en orden inverso.  
#Debe tener la función para crear el lista e imprimirlo.  
#No se pueden usar funciones propias de listas  

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

def invertir_lista(lista):
    invertida = [0]*len(lista) 
    index = 0
    for i in range(1, len(lista)+1, 1):
        invertida[index] = lista[-i]
        index +=1
    return invertida

def imprimir_lista(lista):
    print(lista)


lista = crear_lista()
if(lista!=None):
    imprimir_lista(invertir_lista(lista))
else:
    print("La lista no se ha generado")

