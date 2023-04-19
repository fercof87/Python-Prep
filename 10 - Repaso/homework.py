# Funcion que realiza el factoreo de un Numero
# devuelve 2 listas: la primera con los factores
# y la segunda con los exponentes relacionados en el mismo orden
# si el numero es menor a 1 o no es un numero, retornar none

def factorizar(numero):
    
    if(type(numero) != int or numero < 1):
        return None
    
    lista_primos = []
    i = 2
    # Busqueda de nros primos inferiores al numero parametro
    while (i <= numero):
            es_primo = True
            j=2
            while(j < i/2):
                 if(i % j == 0):
                      es_primo = False
                      break
                 j += 1
            if(es_primo):
                 lista_primos.append(i)
            i += 1 

    lista_factores = []
    lista_exponentes = []

    # buscamos factores y calculamos los exponentes
    for i in lista_primos:
        cant_exponente = 0
        while(numero % i == 0):
            numero /= i
            cant_exponente += 1
        if(cant_exponente>0):
             lista_factores.append(i)
             lista_exponentes.append(cant_exponente)

    return [lista_factores,lista_exponentes]

print(factorizar(5))
print(factorizar(7))
print(factorizar(10))
print(factorizar(11))
print(factorizar(19))
print(factorizar(12))
print(factorizar(24))
print(factorizar(48))
print(factorizar(55))


