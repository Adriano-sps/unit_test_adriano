class Piloto:
    def __init__(self, nombre: str, licencia: str):
        self.nombre = nombre
        self.licencia = licencia

class Avion:

    def __init__(self, modelo: str):
        self.modelo = modelo
        self.pilotos = []

    def agregar_piloto(self, piloto: Piloto):
        if isinstance(piloto, Piloto):
            self.pilotos.append(piloto)