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

# 6) Probar las funciones incorporadas en la clase del punto 5

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
