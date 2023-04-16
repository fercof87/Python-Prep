# Variables
print("\n\n\n INICIO PRACTICA DE VARIABLES \n\n")
# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
num_ent = 10
print("1  ==> ", num_ent)

# 2) Imprimir el tipo de dato de la constante 8.5
print("2  ==> ", type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print("3  ==> ", type(num_ent))

# 4) Crear una variable que contenga tu nombre
mi_nombre = "Fernando"
print("4  ==> ", mi_nombre)

# 5) Crear una variable que contenga un número complejo
num_complejo1 = 2 + 3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print("6  ==> ", type(num_complejo1))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
mi_pi = 3.1416
print("7  ==> ", mi_pi)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
# NO. La primera es un String y la segunda un Booleano
var1 = "True"
var2 = True
print("8-9==> ", type(var1))
print("8-9==> ", var1)
print("8-9==> ", type(var2))
print("8-9==> ", var2)

# 10) Asignar a una variable, la suma de un número entero y otro decimal
suma = 10 + 15.54
print("10 ==> ", suma)

# 11) Realizar una operación de suma de números complejos
num_complejo2 = 1 + 1j
num_complejo3 = num_complejo1 + num_complejo2 
print("11 ==> ", num_complejo3)

# 12) Realizar una operación de suma de un número real y otro complejo
suma2 = num_complejo3 + suma
print("12 ==> ", suma2)

# 13) Realizar una operación de multiplicación
print("13 ==> 10 * 5 = ", 10*5)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
print("14 ==> 2 ** 8  = ", 2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print("15 ==> 27 / 4  = ", 27/4)

# 16) De la división anterior solamente mostrar la parte entera
print("16 ==> 27 // 4  = ", 27//4)

# 17) De la división de 27 entre 4 mostrar solamente el resto
print("17 ==> 27 % 4  = ", 27%4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print("18 ==> 6*4+3  = ", 6*4+3)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("19 ==> ", "Hola" + " Mundo!")

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
# Devuelve False porque estoy comparando un string con un entero
print("20 ==> ",2=="2")

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print("21 ==> ",2==int("2"))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# Por que la coma decimal en python se representa con "." y no con ","
# a = float('3,8')
a = float('3.8')

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
b = 3
b -=2
print("23 ==> ", b)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# El sistema de numeracion binario es aquel compuesto por solamente 2 elementos, el 1 y el 0. Es el lenguaje mas bajo que interpreta un computador. Podriamos decir, que dew fondo, una pc solo entiende 1 y 0.
# el resultado arrojado es el de haber dezplazado el valor 1 en binario dos posiciones a la izquiera. El primer movimiento genera un 2 y el segundo un 4.
c = 1 << 2
print("24 ==> ", c)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# da error por tratarse de tipos de datos distintos. Estamos sumando un int a un str. 
# Si los dos operandos son iguales, hay dos resultados posibles ==> 4 (si ambos son enteros) o "22" si ambos son str.
# print("25 ==> ", 2+"2")
print("25 ==> str ", "2"+"2")
print("25 ==> int ", 2 + 2)

# 26) Realizar una operación válida entre valores de tipo entero y string
cadena = "Hola "
multiplicador = 5
print ("26 ==> cadena*multiplicador: ", cadena*multiplicador)

print("\n\n\n FIN PRACTICA DE VARIABLES \n\n")