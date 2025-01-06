# Um objeto Match é um objeto que contém informações sobre a pesquisa e o resultado.
# Se não houver correspondência, o valor None será retornado, em vez do objeto Match.
''' Métodos do objeto Match:
Método          Descrição      
group()         Retorna a string correspondente ao padrão.        
start()         Retorna a posição inicial da correspondência.
end()           Retorna a posição final da correspondência.
span()          Retorna uma tupla contendo as posições inicial e final da correspondência.
''' 
''' Propriedades do objeto Match:
Propriedade     Descrição
string          Retorna a string passada para a função.
'''

# Principais métodos:-------------------------------------------------------------------------------------------------------------
import re

# Faz uma pesquisa que retornará um objeto Match:--------------------------------------------------
txt = "The rain in Spain"
padrao = "ai"
match = re.search(padrao, txt)
print(match)    # Saída: <re.Match object; span=(5, 7), match='ai'>

# Exemplo com o método span():--------------------------------------------------------------------
txt = "The rain in Spain"
padrao = "ai"
match = re.search(padrao, txt)
print(match.span()) # Saída: (12, 17) (significa que a string começa na posição 12 e termina na 16 (17 não entra!)).

# Exemplo com o método start():--------------------------------------------------------------------
# Retorna a posição do primeiro caractere de espaço em branco.
txt = "The rain in Spain"
pattern = r"\s"
match = re.search(pattern, txt).start()
print(match)    # Saída: 3 

# Exemplo com o método group():-------------------------------------------------------------------
# Retorna a string correspondente ao padrão.
txt = "São 13 horas!"
pattern = r"\d+"
match = re.search(pattern, txt).group()
print(match)    # Saída: 13

# Exemplo com a propriedade string:---------------------------------------------------------------
txt = "The rain in Spain"
pattern = r"\bS\w+"
match = re.search(pattern, txt)
print(match.string)     # Saída: The rain in Spain (string especificada)
# Procura por um caractere "S" maiúsculo no início de uma palavra e imprima a palavra:
print(match.group())    # Saída: Spain (correspondência)