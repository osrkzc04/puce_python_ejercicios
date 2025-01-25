### Ejercicio 3: Promedio de un arreglo
#Descripción: Crea una función que reciba un arreglo de números enteros y retorne el promedio de los elementos.  
#Debe tener la función para crear la matriz e imprimirlo.  
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

def promedio_arreglo(arreglo):
    suma = 0
    for cantidadArreglo in arreglo:
        suma += cantidadArreglo
    promedio=suma/len(arreglo)
    return promedio

lista=crear_lista()
promedio = promedio_arreglo(lista)
print(f"El promedio es: {promedio}")