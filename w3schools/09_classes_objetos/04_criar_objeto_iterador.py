# Iterável: É um objeto que pode ser iterado. Ele possui o método __iter__() que retorna um iterador. Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis.
# Iterador: É um objeto que realiza a iteração, implementa os métodos especiais __iter__() e __next__(), permitindo que você percorra seus elementos um por um.
# __iter__(): Este método deve retornar o próprio objeto iterador. Ele é chamado quando um iterador é inicializado, por exemplo, ao usar um for loop.
# __next__(): Este método retorna o próximo item da sequência. Quando não há mais itens para retornar, ele deve levantar a exceção StopIteration.
# StopIteration: No método __next__(), podemos adicionar uma condição de término para gerar um erro se a iteração for feita um número especificado de vezes: Para evitar que a iteração continue para sempre, podemos usar a instrução StopIteration.
    # raise: Esta palavra-chave é usada para levantar uma exceção em Python. Quando uma exceção é levantada, a execução do programa é interrompida e o controle é passado para o bloco de exceção correspondente, se houver.
    # StopIteration: Esta é uma exceção embutida em Python que sinaliza o fim de uma iteração. Quando o método __next__() de um iterador levanta esta exceção, ele informa ao loop que não há mais itens a serem iterados.

class Contador:
    def __init__(self, limite):     # Método __init__()
        self.atual = 0
        self.limite = limite

    def __iter__(self):             # Método __iter__()
        return self                 # Retorna o próprio objeto iterador.

    def __next__(self):             # Método __next__()
        if self.atual < self.limite:
            self.atual += 1
            return self.atual       # Retorna o próximo item da sequência.
        else:
            raise StopIteration     # Exibe um erro caso o número de iterações seja maior do que o especificado.
    
contador = Contador(5)              # Instamciamento da classe (objeto).

for numero in contador:             # O for loop, na verdade, cria um objeto iterador (__iter__()) e executa o método next() (__next__()) para cada loop.
    print(numero)
''' Saída:
1
2
3
4
5
'''

# Criação de uma classe que usa os conceitos de iterável e iterador para percorrer todas as suas propriedades e imprimir na tela ao ser iterada por um for loop:
class Parents:
    def __init__(self, *parentes):          # Método __init__()
        self.parentes = parentes
        self.i = -1

    def __iter__(self):                     # Método __iter__()
        return self                         # Retorna o próprio objeto iterador.

    def __next__(self):                     # Método __next__()
        if self.i <= len(self.parentes) - 2:
            self.i += 1
            return self.parentes[self.i]    # Retorna o próximo item da sequência.
        else:
            raise StopIteration             # Exibe um erro caso o número de iterações seja maior do que o especificado.
        
parentes = Parents("Wyllamys", "Lucinalva", "David", "Silas")   # Instamciamento da classe (objeto).
for x in parentes:        # O for loop, na verdade, cria um objeto iterador (__iter__()) e executa o método next() (__next__()) para cada loop.
    print(x)
''' Saída:
Wyllamys
Lucinalva
David
Silas
'''