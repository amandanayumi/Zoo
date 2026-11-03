from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Cachorro(Animal):
    def falar(self):
        print(self.nome, ": Au au")

    def mover(self):
        print(self.nome, "corre")


class Gato(Animal):
    def falar(self):
        print(self.nome, ": Miau")

    def mover(self):
        print(self.nome, "pula")


class Vaca(Animal):
    def falar(self):
        print(self.nome, ": Muuu")

    def mover(self):
        print(self.nome, "caminha")


class Voador:
    def voar(self):
        print(self.nome, "voa")


class Nadador:
    def nadar(self):
        print(self.nome, "nada")


class Pato(Animal, Voador, Nadador):
    def falar(self):
        print(self.nome, ": Quack")

    def mover(self):
        print(self.nome, "anda")
        self.voar()
        self.nadar()


class Jacare(Animal, Nadador):
    def falar(self):
        print(self.nome, ": Roar")

    def mover(self):
        print(self.nome, "anda")
        self.nadar()


def fazer_som(animal):
    animal.falar()


def fazer_movimento(animal):
    animal.mover()


rex = Cachorro("Rex")
mimi = Gato("Mimi")
mimosa = Vaca("Mimosa")
donald = Pato("Donald")
jacare = Jacare("Jacaré")

fazer_som(rex)
fazer_movimento(rex)
fazer_som(mimi)
fazer_movimento(mimi)
fazer_som(mimosa)
fazer_movimento(mimosa)
fazer_som(donald)
fazer_movimento(donald)
fazer_som(jacare)
fazer_movimento(jacare)