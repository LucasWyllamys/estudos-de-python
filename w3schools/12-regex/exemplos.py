import re

string = "Lucas Wyllamys"

# O método compile() cria um padrão:
padrao = re.compile("Lucas Wyllamys")   # Entre os parenteses deste método defina um padrão de string

# O método fullmatch verifica que a string inteira atende ao padrão especificado.
# Se a string não atender inteiramente ao padrão especificado, retorna None. 
# Se a string atende ao padrão, retorna o objeto do tipo re:
result = re.fullmatch(padrao, string)   
print(result)   # Saída: <re.Match object; span=(0, 14), match='Lucas Wyllamys'>
# Obs.: o atributo span indica onde que a string começa e termina (o valor de término não entra na conta!).

# https://www.google.com.br/