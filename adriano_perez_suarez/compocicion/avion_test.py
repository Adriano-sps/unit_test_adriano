
#Compocicion
from adriano_perez_suarez.compocicion.avion import Aeronave, Motor


def test_instancia_aeronave():
    motor = Motor("Turbohélice", 20000.0)
    aeronave = Aeronave("Lockheed C-130", motor)
    assert isinstance(aeronave, Aeronave)

def test_atributo_motor():
    motor = Motor("Turbofán", 150000.0)
    assert motor.tipo == "Turbofán"
    assert motor.potencia_newtons == 150000.0


def test_aeronave_tiene_un_motor():
    motor = Motor("Turborreactor", 90000.0)
    aeronave = Aeronave("Boeing 747", motor)

    assert isinstance(aeronave.motor, Motor)
    assert aeronave.motor.tipo == "Turborreactor"
    assert aeronave.motor.potencia_newtons == 90000.0
    

