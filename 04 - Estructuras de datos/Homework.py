#Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades = ["Buenos Aires", "Nueva York", "Tokio", "Berlin", "Roma", "Paris"]
print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:3])

# 4) Visualizar el tipo de dato de la lista
print(type(ciudades))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(ciudades[2:])

# 6) Visualizar los primeros 4 elementos de la lista
print(ciudades[0:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append("Buenos Aires")
ciudades.append("Lisboa")
print(ciudades)
# RESPUESTA: NO ARROJA NINGUN ERROR. LA LISTA ADMITE DUPLICADOS

# 8) Agregar otra ciudad, pero en la cuarta posición
ciudades[3] = "Medellin"
#ciudades.insert(3, "Medellin")
print(ciudades)

# 9) Concatenar otra lista a la ya creada
ciudades2 = ["Mar Del Plata","San Bernardo","San Clemente"]

ciudades.extend(ciudades2)
# ciudades = ciudades + ciudades2
print(ciudades)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(ciudades.index("Buenos Aires"))
# RESPUES: SI, index retorna la primer ocurrencia si es que esta repetido

# 11) ¿Qué pasa si se busca un elemento que no existe?
# print(ciudades.index("Kuala Lumpur"))
# Arroja una excepcion de elemento no encontrado en la lista.

# 12) Eliminar un elemento de la lista
ciudades.remove("San Clemente")
print(ciudades)

# 13) ¿Qué pasa si el elemento a eliminar no existe?
# ciudades.remove("Kuala Lumpur")
# Arroja una excepcion de elemento no encontrado en la lista.

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ultimo = ciudades.pop()
print(ultimo)
print(ciudades)

# 15) Mostrar la lista multiplicada por 4
print (ciudades*4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20
# mi_tupla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
mi_tupla = tuple(range(0,21))
print(type(mi_tupla))
print(mi_tupla)

# 17) Imprimir desde el índice 10 al 15 de la tupla
print(mi_tupla[10:16])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in mi_tupla)
print(30 in mi_tupla)

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
nueva = "Paris"
if (nueva not in ciudades):
    ciudades.append(nueva)
    print("Ciudad ", nueva, "Agregada!")
else:
    print("Ciudad ", nueva, "Existente en la Lista, No se ha Agregado!")

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(ciudades.count("Buenos Aires"))
print(mi_tupla.count(20))

# 21) Convertir la tupla en una lista
mi_tupla = list(mi_tupla)
print(type(mi_tupla))


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
v1, v2, v3 = mi_tupla[0:3]
print(v1)
print(v2)
print(v3)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
dicc = {  'Ciudad': ciudades, 
'País': ['Brasil','Paraguay','Ecuador','Uruguay','Chile','Perú','Venezuela','Colombia','Méjico','Uruguay','España','Italia','Francia'], 
'Continente' : ['América','América','América','América','América','América','América','América','América','América','Europa','Europa','Europa']}

print (dicc)

# 24) Imprimir las claves del diccionario
print(dicc.keys())

# 25) Imprimir las ciudades a través de su clave
print(dicc["Ciudad"])