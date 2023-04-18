## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. 
# Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

import sys
sys.path.append(r'/C:/Users/f_cof/Desktop/Proyectos Henry/Python-Prep/08 - Error Handling/herramientas.py')

import herramientas as h

#h1 = h.Herramientas("Hola")
#h1 = h.Herramientas([1,2,3,4])
#print(h1.factorial())
# h1 = h.Herramientas([1,2,"A",3,4])
# print(h1.factorial())

# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

import importlib
importlib.reload(h)

h1 = h.Herramientas([2,3,5,6,2])
# h1.conversion_grados(1,2)
print(h1.conversion_grados('celsius','farenheit'))


# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>

import unittest

class PruebaClase(unittest.TestCase):
    def creacion_objeto_incorrecto(self):
        var = "Hola"
        # self.assertRaises(ValueError, h.Herramientas, var)
        self.failUnlessRaises(ValueError, h.Herramientas, var)

        
