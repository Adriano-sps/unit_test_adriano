class Motor:
    def __init__(self, tipo: str, potencia_newtons: float):
        self.tipo = tipo
        self.potencia_newtons = potencia_newtons

class Aeronave:
    def __init__(self, modelo: str, motor: Motor = None): # type: ignore
        self.modelo = modelo
        self.motor = motor if motor else Motor("turbofan por defecto", 0.0)