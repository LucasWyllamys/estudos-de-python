# A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
# A classe pai é a classe da qual se está herdando, também chamada de classe base.
# Classe filha é a classe que herda de outra classe, também chamada de classe derivada.

# Criar uma classe pai: Qualquer classe pode ser uma classe pai, então a sintaxe é a mesma para criar qualquer outra classe:
class Person:   # Classe pai
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print(self.firstname, self.lastname)

p1 = Person("Lucas", "Wyllamys")    # Instanciamento da classe (objeto)
p1.printName()  # Saída: Lucas Wyllamys

# Criar uma classe filha: Para criar uma classe que herda as propriedades e métodos da classe pai, envie a classe pai como parâmetro ao criar a classe filha:
class Student(Person):  # Classe filho
    pass        

student = Student("David", "Wilkerson")
student.printName()  # Saída: David Wilkerson

# Quando você adiciona a função __init__(), a classe filha não herdará mais a função __init__() da classe pai.
# A função __init__() da classe filho substitui a herança da função __init__() da classe pai.
# Para manter a herança da função __init__() pai, adicione uma chamada à função __init__() pai (Person.__init__(self, fname, lname)):
class Student(Person):  # Classe filho
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# Use a função super(): Python também tem uma função super() que fará com que a classe filha herde todos os métodos e propriedades de sua classe pai:
# Ao usar a função super(), você NÃO precisa usar o nome do elemento pai, ele herdará automaticamente os métodos e propriedades do seu pai.
class Student(Person):                          # Classe filho
    def __init__(self, fname, lname, year):     # Função de inicialização da classe.
        super().__init__(fname, lname)          # Faz referência as propriedades e métodos da classe pai.
        self.graduationYear = year              # Propriedade

    def welcome(self):                          # Método
        print(f"Seja bem vindo, {self.firstname} {self.lastname}, à classe de {self.graduationYear}")

student = Student("Lucas", "Wyllamys", 2018)    # Instanciamento da classe (objeto)
student.printName()                             # Lucas Wyllamys
student.welcome()                               # Seja bem vindo, Lucas Wyllamys, à classe de 2018 

# NOTA: Se você adicionar um método na classe filha com o mesmo nome de uma função na classe pai, a herança do método pai será substituída.