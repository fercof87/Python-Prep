# Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
# CON FOR
lista = []
for i in range(-15,0):
    lista.append(i)
print(lista)

# CON WHILE
# lista = []
# nro = -15
# while (nro > 0):
#     lista.append(nro)
#     nro += 1
# print(lista)


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
nro = 0
while(nro < len(lista)):
    if(lista[nro] % 2 == 0):
        print(lista[nro])
    nro += 1

# 3) Resolver el punto anterior sin utilizar un ciclo while
print(lista[1::2])
for elemento in lista:
    if(elemento % 2 == 0):
        print(elemento)

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
for elemento in lista[:3]:
    print(elemento)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
for indice, elemento in enumerate(lista):
    print(indice, "==> ", elemento)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
print ("\n\n\n #6#")
lista = [1,2,5,7,8,10,13,14,15,17,20]
print (lista)
nro = 1
while (nro < 20):
    if(nro not in lista):
        lista.insert(nro-1,nro)
    nro += 1
print (lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

fibo = []
n = 0
while(n < 30):
    if(n<2):
        fibo.append(n)
    else:
        fibo.append(fibo[n-1] + fibo[n-2])
    n += 1
print(fibo)

# 8) Realizar la suma de todos elementos de la lista del punto anterior
print(sum(fibo))

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. 
# El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>

pares = 0
cant = len(fibo) - 1

while(pares < 5):
    print(fibo[cant - pares] / fibo[cant - pares - 1])
    pares += 1

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
for indice, letra in enumerate(cadena):
    if(letra == "n"):
        print (indice)


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
dicc = {  'Ciudad': ['Buenos Aires','Caracas','Bogotá','Lisboa','Roma'], 
'País': ['Argentina','Venezuela','Colombia','Portugal','Italia'], 
'Continente' : ['América','América','América','Europa','Europa']}
for i in dicc:
    print (i)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
cadena = list(cadena)
iterador = iter(cadena)
for i in range(0,len(cadena)):
    print(next(iterador))

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,0]
lista3 = list(zip(lista1,lista2))
print(lista3)

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
nueva = [i for i in lis if i % 7 ==0]
print(nueva)

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cant = 0
for elemento in lis:
    if(type(elemento) == list):
        cant += len(elemento)
    else:
        cant += 1
print(cant)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
for indice, elemento in enumerate(lis):
    if(type(elemento) != list):
        lis[indice] = [elemento]
print(lis)
