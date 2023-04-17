# Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def valida_primo(numero):
    es_primo = True
    for i in range(2,numero):
        if(numero % i == 0):
            es_primo = False
            break
    return es_primo

print(valida_primo(0))
print(valida_primo(1))
print(valida_primo(2))
print(valida_primo(3))
print(valida_primo(4))
print(valida_primo(5))
print(valida_primo(6))
print(valida_primo(7))
print(valida_primo(8))
print(valida_primo(9))
print(valida_primo(10))
print(valida_primo(11))

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
def valida_lista_primos(lista):
    primos = []
    for elemento in lista:
        if(valida_primo(elemento)):
            primos.append(elemento)
    return primos

print(valida_lista_primos([1,2,3,4,5,6,7,8,9,10,11]))
            

# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
def valida_repetido(lista,orden=1):
    #la funcion devolvera menor si recibe un 0 y mayor si recibe un 1
    #por defecto devolvera el Mas Repetido
    repeticiones = 0
    nro_repetido = 0
    chequeados = []
    orden = bool(orden)
    for indice, elemento in enumerate(lista):
        #me guardo los que ya verifique para no analizar dos veces un mismo nro
        if(elemento in chequeados):
            continue
        else:
            chequeados.append(elemento)
        #si es la primera ejecucion, entonces me guardo el primer elemento como el maximo
        if(((indice == 0) or (lista.count(elemento) > repeticiones) and orden) or ((indice == 0) or (lista.count(elemento) < repeticiones) and not orden)):
            nro_repetido = elemento
            repeticiones = lista.count(elemento)

    if (repeticiones == 0):
        return None
    return nro_repetido, repeticiones
        

print("\n\n MENOR \n\n")
print(valida_repetido([6,1,1,1,2,2,2,2,3,3,4,5,5,5,5,5,5,6,6,5,5,6,6,6,6,6,6,6,6,6,6,7,7,10],1))
print(valida_repetido([1,1,1,1,1,0,1,1,1,1,0],1))
print(valida_repetido([],1))
print("\n\n MAYOR \n\n")
print(valida_repetido([6,1,1,1,2,2,2,2,3,3,4,5,5,5,5,5,5,6,6,5,5,6,6,6,6,6,6,6,6,6,6,7,7,10],0))
print(valida_repetido([1,1,1,1,1,0,1,1,1,1,0],0))
print(valida_repetido([],0))

# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br> (f - 32)*5/9 = C
# Fórmula 2	: °C + 273.15 = °K<br>  
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
def conversor(valor, unidad_orig = "celsius", unidad_dest = "farenheit"):

    resultado = valor

    if(unidad_orig == "celsius"):
        if(unidad_dest == "farenheit"):
            resultado = (valor * 9 / 5) + 32
        if(unidad_dest == "kelvin"):
            resultado = valor + 273.15
    
    if(unidad_orig == "farenheit"):
        if(unidad_dest == "celsius"):
            resultado = (valor - 32) * 5 / 9
        if(unidad_dest == "kelvin"):
            resultado = ((valor - 32) * 5 / 9) + 273.15
    
    if(unidad_orig == "kelvin"):
        if(unidad_dest == "celsius"):
            resultado = valor - 273.15
        if(unidad_dest == "farenheit"):
            resultado = ((valor - 273.15) *9 / 5) + 32

    return resultado

# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
print("\n\n 6 \n\n")
lista = ["celsius", "farenheit", "kelvin"]
grados = 1

for i in range(0,3):
    for j in range(0,3):
        print (grados, " Grados", lista[i], " a ", lista[j], " es: ", conversor(grados,lista[i],lista[j]), ".")

# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
def calcula_factorial(numero):
    if(type(numero) != int or numero <0):
        return None
    if (numero > 1):
        return numero * calcula_factorial(numero -1)
    else:    
        return 1

print("\n\n 7 \n\n")
print (calcula_factorial(-1))    
print (calcula_factorial("a"))    
print (calcula_factorial(123.456))    
print (calcula_factorial(0))
print (calcula_factorial(1))
print (calcula_factorial(2))
print (calcula_factorial(3))
print (calcula_factorial(4))
print (calcula_factorial(5))