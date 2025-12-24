class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"Vehiculo {self.marca} del modelo {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas, anio):
        super().__init__(marca, modelo)
        self.puertas = puertas
        self.anio = anio

    def info(self):
        print(f"{super().info()}, numero de puertas {self.puertas}, año {self.anio}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo, anio):
        super().__init__(marca, modelo)
        self.tipo = tipo
        self.anio = anio

    def info(self):
        print(f"{super().info()}, tipo de vehiculo {self.tipo}, año {self.anio}")

carro1 = Coche("WK", "Gol", 4, 2020)
carro1.info()

moto1 = Motocicleta("Kawasaki", "Ninja", "Deportiva", 2019)
moto1.info()

carro2 = Coche("Seat", "Leon", 4, 2025)
carro2.info()

moto2 = Motocicleta("BMW", "1200cc", "Deportiva", 2013)
moto2.info()