# Uma RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
# O RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado. Com o Regex você consegue:
    # Realizar buscas por padrões e strings.
    # Fazer validações de padrões e texto.
    # Substituições de padõres e strings.
# O Python tem um pacote integrado chamado re, que pode ser usado para trabalhar com expressões regulares.
import re

# Exemplos:--------------------------------------------------------------------

string = "Lucas Wyllamys Carmo da Silva - Lucas Wyllamys"

padrao = re.compile("Lucas Wyllamys")

result = re.fullmatch(padrao, string)  
print(result)   # Saída: None

result = re.search(padrao, string)
print(result)   # Saída: <re.Match object; span=(0, 14), match='Lucas Wyllamys'>. O atributo span indica onde que a string começa e termina (o valor de término não entra na conta!).

result = re.findall(padrao, string)
print(result)   # Saída: ['Lucas Wyllamys', 'Lucas Wyllamys']
