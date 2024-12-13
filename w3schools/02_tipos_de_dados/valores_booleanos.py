# Quase todo valor é avaliado True se tem algum tipo de conteúdo.
print(bool('abc'))                      # Saída: True (Qualquer string é True, exceto strings vazias.)
print(bool(123))                        # Saída: True (Qualquer número é True, exceto 0.)
print(bool(['maça', 'uva', 'banana']))  # Saída: True (Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.)

# Na verdade, não há muitos valores que avaliam para False, exceto valores vazios, como (), [], {}, "", o número 0 e o valor None. E, claro, o valor False avalia para False:
print(bool(False))      # Saída: False
print(bool(None))       # Saída: False
print(bool(0))          # Saída: False
print(bool(""))         # Saída: False
print(bool(()))         # Saída: False
print(bool([]))         # Saída: False
print(bool({}))         # Saída: False

# Um objeto retorna False se for feito de uma classe com uma _len_ função que retorna 0 ou False.
class myClass():
    def __len__(self):
        return 0

myobj = myClass()
print(bool(myobj))          # Saída: False

# Você pode criar funções que retornam um valor booleano.
def myFunction():
    return True

print(myFunction())         # Saída: True

if myFunction():
    print('SIM!')           # Saída: True
else:
    print('NÃO!')

# Como verificar se um objeto é de um determinado tipo de dados:
# Use a função isinstance() para verificar se um objeto é de um determinado tipo de dados
x = 200
print(isinstance(x, int))   # Saída: True