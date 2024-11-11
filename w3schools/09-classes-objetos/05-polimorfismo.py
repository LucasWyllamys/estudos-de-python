# A palavra "polimorfismo" significa "muitas formas" e, em programação, refere-se a métodos/funções/operadores com o mesmo nome que podem ser executados em muitos objetos ou classes.
# As classes filhos herdam as propriedades e métodos da classe pai.
# Polimorfismo de função: Um exemplo de uma função Python que pode ser usada em diferentes objetos é a função len() que pode ser usada em strings, tuplas, dicionários etc.
# O polimorfismo é frequentemente usado em métodos de classe, onde podemos ter várias classes com o mesmo nome de método.

# Por exemplo, digamos que temos três classes: Car, Boat, e Plane, e todas elas têm um método chamado move(). Por causa do polimorfismo, podemos executar o mesmo método para todas as três classes que são diferentes e independentes entre si:
class Vehicle:  # Classe pai
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):  # Classe filho
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat(Vehicle):    # Classe filho
    pass

class Plane(Vehicle):   # Classe filho
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

car1.move()     # Saída: Drive!
boat1.move()    # Saída: Move! (herdou da classe pai Vehicle)
plane1.move()   # Saída: Fly!

for x in (car1, boat1, plane1):
    print(x.brand, x.model)     # Propriedades
    x.move()                    # Método
''' Saída:
Ford Mustang
Drive!
Ibiza Touring 20
Move!
Boeing 747
Fly!
'''

''' NOTA:
- No exemplo acima, você pode ver que a classe Car está vazia, mas herda as propriedades brand, model, e o método move() da classe pai Vehicle.
- As classes Boate e Plane também herdam as propriedades brand, modele e o método move() da classe pai Vehicle, mas ambas substituem o método move().
- Devido ao polimorfismo, podemos executar o mesmo método para todas as classes.
'''
