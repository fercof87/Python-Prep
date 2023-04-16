# Flujos de Control
print("\n\n\n INICIO PRACTICA DE FLUJOS DE CONTROL \n\n")


# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
var1 = int(input("Ingrese un Entero: "))
if(var1 > 0):
    print("La Variable es Mayor a Cero.")
elif(var1 < 0):
    print("La Variable es Menor a Cero.")
else:
    print("La Variable es Igual a Cero.")

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
var2 = "Hola"
var3 = 123
if(type(var2) == type(var3)):
    print("Las Variables Son del mismo tipo de dato ==> ", type(var2))
else:
    print("Las Variables son de diferentes tipos de datos ==> ", type(var2), " vs. ", type(var3))

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1,21):
    if(i % 2 == 0):
        print(i, "\t ES PAR.")
    else:
        print(i, "\t ES IMPAR.")

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(0,6):
    print(i, "**3 = ", i**3)

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
var4 = int(input("Ingrese un Entero: "))
for i in range(1,var4+1):
    print("CICLO NRO ==> ", i)

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
factorial = 1
nro = 5
aux = nro

if(type(nro) == int):
    if(nro>0):
        while( aux > 1):
            factorial = factorial * aux
            aux -= 1
    else:
        print("\n ~~ El Nro Ingresado no es  Mayor que CERO. ~~ ")    
else:
    print("\n ~~ La Variable Ingresada no es un ENTERO. ~~ ")    

print ("El factorial de ", nro, " es ==> ", factorial, ".")


# 7) Crear un ciclo for dentro de un ciclo while
n = 0
while(n < 5):
    n += 1
    for i in range(1,n):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))

# 8) Crear un ciclo while dentro de un ciclo for
n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))

# 9) Imprimir los números primos existentes entre 0 y 30
# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

for i in range(0,31):
    es_primo = True
    for j in range(2,int(i/2)+1):
        if(i> 3 and i % j == 0):
            es_primo = False
            break
    if(es_primo):
        print(i, " ==> ES PRIMO.")


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

print("\n\n\n CON 30 NROS")
cantidad_ciclos_sin = 0
cantidad_ciclos_con = 0
for i in range(0,31):
    es_primo = True
    for j in range(2,int(i/2)+1):
        if(i> 3 and i % j == 0):
            es_primo = False
            cantidad_ciclos_sin +=1
    if(es_primo):
        print(i, " ==> ES PRIMO.")
print("ciclos sin break: ", cantidad_ciclos_sin)

for i in range(0,31):
    es_primo = True
    for j in range(2,int(i/2)+1):
        if(i> 3 and i % j == 0):
            es_primo = False
            cantidad_ciclos_con +=1
            break
    if(es_primo):
        print(i, " ==> ES PRIMO.")
print("ciclos CON break: ", cantidad_ciclos_con)
print("Optimizacion: ", cantidad_ciclos_con/cantidad_ciclos_sin*100, "%.")

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print("\n\n\n CON 60 NROS")
cantidad_ciclos_sin = 0
cantidad_ciclos_con = 0
for i in range(0,61):
    es_primo = True
    for j in range(2,int(i/2)+1):
        if(i> 3 and i % j == 0):
            es_primo = False
            cantidad_ciclos_sin +=1
    if(es_primo):
        print(i, " ==> ES PRIMO.")
print("ciclos sin break: ", cantidad_ciclos_sin)

for i in range(0,61):
    es_primo = True
    for j in range(2,int(i/2)+1):
        if(i> 3 and i % j == 0):
            es_primo = False
            cantidad_ciclos_con +=1
            break
    if(es_primo):
        print(i, " ==> ES PRIMO.")
print("ciclos CON break: ", cantidad_ciclos_con)
print("Optimizacion: ", cantidad_ciclos_con)
print("Optimizacion: ", cantidad_ciclos_con/cantidad_ciclos_sin*100, "%.")

# RESPUESTA: Al aumentar la cantidad de nros, la optimizacion disminuye porque tiene que hacer muchas mas comparaciones (ciclos)

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
nro = 99
while(nro <= 300):
    nro +=1
    if(nro % 12 != 0 ):
        continue
    print(nro)


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
print("\n\n\n BUSCADOR DE NROS PRIMOS \n\n\n")
primera = True
nro=1
while(True):
    es_primo = True
    if (primera):
        opcion = (input("Desea Buscar Nros PRIMO? (S/s/N/n): ")).upper()
        primera = False
    else:
        opcion = (input("Desea Buscar el Siguiente nro PRIMO? (S/s/N/n): ")).upper()
    if(opcion not in ["N","S"]):
        print("Opcion Ingresada Incorrecta. Ingrese S/s/Nn: ")
    else:
        if(opcion == "N"):
            print("\n\n BUSQUEDA FINALIZADA. MUCHAS GRACIAS. \n\n")
            break
        else:
            for i in range(2,nro):
                if(nro % i ==0):
                    es_primo = False
                    break
            if(es_primo):
                print(nro)
    nro += 1


# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
for i in range(100,301):
    #SI ES MULTIPLO DE 6 TMB SERA DIVISIBLE POR 3 YA QUE CUALQUIER MULTIPLO DE 6 ES DIVISIBLE POR 3
    if(i % 6 == 0): 
        print(i)
        break

print("\n\n\n FIN PRACTICA DE FLUJOS DE CONTROL \n\n")
