# Uma RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
# O RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado. Com o Regex você consegue:
    # Realizar buscas por padrões e strings.
    # Fazer validações de padrões e texto.
    # Substituições de padõres e strings.
# O Python tem um pacote integrado chamado re, que pode ser usado para trabalhar com expressões regulares.
import re

# Validação de CPF:
string = "071.393.565-05"
padrao = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}")  # Como se lê este padrão: [números de 0 a 9]{3 ocorrências}ponto[números de 0 a 9]{3 ocorrências}ponto[números de 0 a 9]{3 ocorrências}traço[némros de 0 a 9]{2 ocorrências}
result = re.fullmatch(padrao, string)  
print(result) 

# Validação RG:

# Validação CNPJ:

# Validação de e-mail:
string = "lucas.wyllamys@outlook.com"
padrao = re.compile("[\w\.]+@[\w]+\.[a-zA-Z]+(\.[a-zA-Z]+)?")
result = re.fullmatch(padrao, string)
print(result)

# Validação CEP:

# Validação Telefone: