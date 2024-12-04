# Uma RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
# O RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado. Com o Regex você consegue:
    # Realizar buscas por padrões e strings.
    # Fazer validações de padrões e texto.
    # Substituições de padõres e strings.
# O Python tem uma biblioteca integrada chamada re, que pode ser usada para trabalhar com expressões regulares.

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