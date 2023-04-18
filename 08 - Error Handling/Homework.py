#!/usr/bin/env python
# coding: utf-8
## Manejo de errores

# 1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. 
# Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

import sys
sys.path.append('C:/Users/f_cof/Desktop/Proyectos Henry/Python-Prep/08 - Error Handling/herramientas.py')

import herramientas as h

#h1 = h.Herramientas("Hola")
#h1 = h.Herramientas([1,2,3,4])
#print(h1.factorial())
# h1 = h.Herramientas([1,2,"A",3,4])
# print(h1.factorial())

# 2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

import importlib
importlib.reload(h)

# h1 = h.Herramientas([2,3,5,6,2])
# # h1.conversion_grados(1,2)
# print(h1.conversion_grados('celsius','farenheit'))


# 3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
# Creacion del objeto incorrecta<br>
# Creacion correcta del objeto<br>
# Metodo valor_modal()<br>

import unittest

class PruebaClase(unittest.TestCase):

    def creacion_objeto_incorrecto(self):
        var = "Hola"
        self.assertRaises(ValueError, h.Herramientas, var)

    def creacion_objeto_correcta(self):
        param = [1,2,2,5]
        h1 = h.Herramientas(param)
        self.assertEqual(h1.lista, param)

    def metodo_modal(self):
        lis = [1,2,1,3]
        h2 = h.Herramientas(lis)
        moda, veces = h2.valor_modal(False)
        resultado = [moda,veces]
        self.assertEqual(resultado,[1,2])
        
unittest.main(argv=[''], verbosity=0, exit=False)

# 4) Probar una creación incorrecta y visualizar la salida del "raise"
h2 = h.Herramientas('algo') 

# 6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo
class ProbandoMiClase2(unittest.TestCase):

    def test_verifica_primos1(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        primos = h1.verifica_primo()
        primos_esperado = [True, True, False, False, True]
        self.assertEqual(primos, primos_esperado)

importlib.reload(h)
unittest.main(argv=[''], verbosity=2, exit=False)

# 7) Agregar casos de pruebas para el método conversion_grados()

class ProbandoMiClase3(unittest.TestCase):

    def test_verifica_conversion1(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        grados = h1.conversion_grados('celsius','farenheit')
        grados_esperado = [35.6, 37.4, 46.4, 50.0, 55.4]
        self.assertEqual(grados, grados_esperado)

importlib.reload(h)

unittest.main(argv=[''], verbosity=2, exit=False)

# 8) Agregar casos de pruebas para el método factorial()
class ProbandoMiClase4(unittest.TestCase):

    def test_verifica_factorial(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        factorial = h1.factorial()
        factorial_esperado = [2, 6, 40320, 3628800, 6227020800]
        self.assertEqual(factorial, factorial_esperado)

importlib.reload(h)

unittest.main(argv=[''], verbosity=2, exit=False)