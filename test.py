from collections import defaultdict

categorias = [
    [0,"Salud"],
    [1,"Alimentación"],
    [2,"Trasportes"],
    [3,"Recreación"],
    [4,"Ahorro"],
]

prespuesto = [
    [0,50.0],
    [1,40.0],
    [2,60.0],
    [3,70.0],
    [4,80.0],
]

gastos_mes = [
 [0,0,20.0], # mes,categorio,valor
 [0,1,20.0],
 [0,2,20.0],
 [0,3,20.0],
 [0,4,20.0],
 [5,0,5.0],
 [5,1,5.0],
 [5,2,5.0],
 [5,3,5.0],
 [5,4,5.0],
 [3,0,12.0],
 [3,1,12.0],
 [3,2,12.0],
 [3,3,12.0],
 [3,4,12.0],
]

meses = [
    [0,'Enero'],
    [1,'Febrero'],
    [2,'Marzo'],
    [3,'Abril'],
    [4,'Mayo'],
    [5,'Junio'],
    [6,'Julio'],
    [7,'Agosto'],
    [8,'Septiembre'],
    [9,'Octubre'],
    [10,'Noviembre'],
    [11,'Diciembre']
]


mes = 2

# Verificar si el elemento 5 está en el arr