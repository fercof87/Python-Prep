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