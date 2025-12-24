class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"Vehiculo {self.marca} del modelo {self.modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def info(self):
        print(f"{super().info()}, numero de puertas {self.puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def info(self):
        print(f"{super().info()}, tipo de vehiculo {self.tipo}")

carro1 = Coche("WK", "Gol", 4)
carro1.info()

moto1 = Motocicleta("Kawasaki", "Ninja", "Deportiva")
moto1.info()