matriz = []

while True:
    try:
        element = int(input("Ingrese un número: "))
        matriz.append(element)
        opcion = input("¿Desea ingresar otro número? (s/n): ")
        match opcion.lower():
            case "s":
                continue
            case "n":
                print("La matriz es: ")
                print(matriz)
                break
            case _:
                print("Opción no válida.")
    except ValueError:
        print("Ha ingresado un dato inconrrecto.")
        break
