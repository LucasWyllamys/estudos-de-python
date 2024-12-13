# Uma classe é como um construtor de objetos ou um "molde" para criar objetos.
# Para criar uma classe, use a palavra-chave class.
# Métodos são funções que pertencem ao objeto.
# Propriedades são variáveis que armazenam as características do objeto.
# Todas as classes têm uma função chamada __init__(), que é sempre executada quando a classe está sendo iniciada.
# Use a função __init__() para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado.
# O parâmetro self é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe.
# A função __str__() controla o que deve ser retornado quando o objeto de classe é representado como uma string. 
# Se função a __str__() não estiver definida, a representação em string do objeto será retornada (<__main__.Person object at 0x000002385BB97C50>).
class Person:
    def __init__(self, name, age):  # Função inicializadora, inicia as propriedades e/ou métodos necessários.
        self.name = name            # Propriedade
        self.age = age              # Propriedade
    
    def saudacao(self):             # Método
        print(f"Olá, meu nome é {self.name}!")

    def __str__(self):
        return f"Nome: {self.name}, idade: {self.age}"

p1 = Person("Lucas", 28)            # Instanciamento do objeto
p1.saudacao()                       # Chamada do método - Saída: Olá, meu nome é Lucas!

p1.age = 40                         # Modifica a propriedade do objeto
print(p1.age)                       # Saída: 40
print(p1)                           # Nome: Lucas, idade: 40

# Você pode excluir propriedades em objetos usando a palavra-chave del:
del p1.age

# Você pode excluir objetos usando a palavra-chave del:
del p1

# Definições class não podem estar vazias, mas se por algum motivo você tiver uma definição class sem conteúdo, insira a palavra-chave pass na declaração para evitar um erro:
class Animal:
    pass