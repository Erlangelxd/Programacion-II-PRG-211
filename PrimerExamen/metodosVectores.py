notas = [100, 70, 85, 100, 100,3, 2,1]
print(notas)
#añadir elementos
notas.append(90)
#quita elementos
notas.pop(1)
#insertar datos por posicion
notas.insert(2, 88)
#retorna la cantidad de veces que se repite un elemento
fr=notas.count(85)
print(fr)
#retorna el indice de un elemento
i=notas.index(2)
print(i)
print(notas)