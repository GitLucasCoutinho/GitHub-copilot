class Car:
    def __init__(self, id, nome, valor, ano, marca):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.ano = ano
        self.marca = marca


def get_cars():
    return [
        Car(1, "Fusca", "R$ 20.000", 1985, "Volkswagen"),
        Car(2, "Civic", "R$ 80.000", 2018, "Honda"),
        Car(3, "Corolla", "R$ 90.000", 2019, "Toyota"),
        Car(4, "Gol", "R$ 35.000", 2012, "Volkswagen"),
        Car(5, "Uno", "R$ 25.000", 2010, "Fiat"),
    ]
