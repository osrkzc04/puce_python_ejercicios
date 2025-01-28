### Ejercicio 4: Contar ocurrencias de un número en un arreglo
#Descripción: Crea una función que reciba un arreglo y un número, y retorne cuántas veces aparece ese número en el arreglo.  
#Debe tener la función para crear el arreglo e imprimirlo.   
#No se pueden usar funciones propias de listas 
def crear_lista():
  try:
    cantidadArreglo=int(input("ingrese el número de arreglo:"))
    arreglo=[0]*cantidadArreglo
    for i in range(0,cantidadArreglo):
       numero=int(input("ingrese el numero:"))
       arreglo[i]=numero
    return arreglo
  except ValueError:
     print("no se pudo ingresar los datos")
def contar_ocurrencias(arreglo, numero):
    contador = 0
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            contador += 1
    return contador

# Nueva función principal para ejecutar el programa
def ejecutar_programa():
    arreglo = crear_lista()
    if arreglo:
        numero_a_contar = int(input("Ingrese el número a contar en el arreglo: "))
        ocurrencias = contar_ocurrencias(arreglo, numero_a_contar)
        print(f"El número {numero_a_contar} aparece {ocurrencias} veces en el arreglo.")

# Ejecutamos la nueva función principal
ejecutar_programa()     
