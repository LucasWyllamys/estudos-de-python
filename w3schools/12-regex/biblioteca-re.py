# Uma RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
# O RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado. Com o Regex você consegue:
    # Realizar buscas por padrões e strings.
    # Fazer validações de padrões e texto.
    # Substituições de padõres e strings.
# O Python tem um pacote integrado chamado re, que pode ser usado para trabalhar com expressões regulares.
import re

# Exemplos:
# Pesquise a string para ver se ela começa com "The" e termina com "Spain":
txt = "The rain is Spain"
x = re.search("^The.*Spain$", txt)

print(x.start())