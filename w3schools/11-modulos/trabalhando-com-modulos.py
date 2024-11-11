# Considere um módulo como sendo o mesmo que uma biblioteca de código.
# Um arquivo contendo um conjunto de funções, matrizes, dicionários, objetos etc. que você deseja incluir em seu aplicativo.
# Você pode criar um alias ao importar um módulo, usando a palavra-chave as.
# Você pode escolher importar apenas partes de um módulo usando a palavra-chave from. Exemplo: 
# from modulo_teste import person1.
import modulo_teste as mt     # Importação do módulo

# Invocando uma função do módulo:
mt.saudacao("Lucas")  # Saída: Hello, Lucas 

# Invocando um dicionário do módulo:
age = mt.person1["age"]
print(age) # Saída: 28

# Função interna que lista todos os nomes de funções (ou nomes de variáveis) em um módulo:
x = dir(mt)
print(x)
''' Saída:
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'person1', 'saudacao']
'''