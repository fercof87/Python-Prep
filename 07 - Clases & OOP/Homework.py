# Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>
class  Vehiculo():
    def __init__(self, color, categoria, cilindrada):
        self.color = color
        self.categoria = categoria
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def Acelerar(self, velocidad):
        self.velocidad += velocidad
    def Frenar(self, velocidad):
        self.velocidad -= velocidad
    def Doblar(self, grados):
        self.velocidad += grados

# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

auto = Vehiculo("Azul", "Auto", 1600)
moto = Vehiculo("Rojo", "Moto", 250)
camion = Vehiculo("Negro", "Camion", 5000)

auto.Acelerar(50)
auto.Doblar(50)
moto.Acelerar(50)
moto.Frenar(-50)
camion.Acelerar(50)
camion.Doblar(-50)

# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
class  Vehiculo():
    def __init__(self, color, categoria, cilindrada):
        self.color = color
        self.categoria = categoria
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = 0
    def Acelerar(self, velocidad):
        self.velocidad += velocidad
    def Frenar(self, velocidad):
        self.velocidad -= velocidad
    def Doblar(self, grados):
        self.direccion += grados
    def Estado(self):
        print("Velocidad: ", self.velocidad, ", Direccion: ", self.direccion, ".")
    def Caracteristicas(self):
        print("Color: ", self.color, ", Categoria: ", self.categoria, ", ", self.cilindrada, ".")

auto1 = auto = Vehiculo("Azul", "Auto", 1600)
auto.Acelerar(50)
auto.Doblar(50)
auto1.Caracteristicas()
auto1.Estado()
# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>
class Funciones():
    def __init__(self) -> None:
        pass

    def valida_primo(self, numero):
        es_primo = True
        for i in range(2,numero):
            if(numero % i == 0):
                es_primo = False
                break
        return es_primo
    
    def valida_repetido(self, lista,orden=1):
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

    def conversor(self, valor, unidad_orig = "celsius", unidad_dest = "farenheit"):
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
    
    def calcula_factorial(self, numero):
        if(type(numero) != int or numero <0):
            return None
        if (numero > 1):
            return numero * self.calcula_factorial(numero -1)
        else:    
            return 1


# 6) Probar las funciones incorporadas en la clase del punto 5

func = Funciones()
# Validacion de nro primo
print(func.valida_primo(7))
# valor modal
lista = [1,8,8,2,5,5,4,4,8,5,10,10,7,7]
valor, repeticiones = func.valida_repetido(lista)
print('El valor modal MAYOR es', valor, 'y se repite', repeticiones, 'veces')
valor, repeticiones = func.valida_repetido(lista,0)
print('El valor modal MENOR es', valor, 'y se repite', repeticiones, 'veces')
# Conversor de Grados
func.conversor(10, 'celsius', 'kelvin')
# factorial
print(func.calcula_factorial(5))

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas
class Funciones():
    def __init__(self,lista_numeros) -> None:
        self.lista = lista_numeros

    def __valida_primo(self, numero):
        es_primo = True
        for i in range(2,numero):
            if(numero % i == 0):
                es_primo = False
                break
        return es_primo
    
    def valida_primo(self):
        for i in self.lista:
            if(self.__valida_primo(i)):
                print("El numero ", i, " ES PRIMO")
            else:
                print("El numero ", i, " NO ES PRIMO")
    
    def valida_repetido(self,orden=1):
    #la funcion devolvera menor si recibe un 0 y mayor si recibe un 1
    #por defecto devolvera el Mas Repetido
        repeticiones = 0
        nro_repetido = 0
        chequeados = []
        orden = bool(orden)
        for indice, elemento in enumerate(self.lista):
            #me guardo los que ya verifique para no analizar dos veces un mismo nro
            if(elemento in chequeados):
                continue
            else:
                chequeados.append(elemento)
            #si es la primera ejecucion, entonces me guardo el primer elemento como el maximo
            if(((indice == 0) or (self.lista.count(elemento) > repeticiones) and orden) or ((indice == 0) or (self.lista.count(elemento) < repeticiones) and not orden)):
                nro_repetido = elemento
                repeticiones = self.lista.count(elemento)

        if (repeticiones == 0):
            return None
        return nro_repetido, repeticiones

    def conversor(self,origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversor(i, origen, destino),'grados',destino)

    def __conversor(self, valor, unidad_orig = "celsius", unidad_dest = "farenheit"):
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
    
    def calcula_factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__calcula_factorial(i))

    def __calcula_factorial(self, numero):
        if(type(numero) != int or numero <0):
            return None
        if (numero > 1):
            return numero * self.calcula_factorial(numero -1)
        else:    
            return 1
        
# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
from funciones import *

func = Funciones([1,8,8,2,5,5,4,4,8,5,10,10,7,7])

func.valida_primo()