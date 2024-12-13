'''
Método          Descrição
.upper()        Retorna a string em maiúsculas.
.lower()        Retorna a string em letras minúsculas.
.strip()        Remove qualquer espaço em branco do início ou do fim.
.replace()      Substitui uma string por outra string.
.split()        Retorna uma lista onde o texto entre o separador especificado se torna os itens da lista.
.capitalize()   Converte o primeiro caractere para maiúsculo.
.find()         Pesquisa a string por um valor especificado e retorna a posição onde ele foi encontrado.
'''

# upper()
a = "Olá, Mundo!"
print(a.upper())                      # Saída: "OLÁ, MUNDO!"

# lower()
b = "Olá, Mundo!"
print(b.lower())                      # Saída: "olá, mundo!

# strip()
c = " Olá, Mundo! "
print(c.strip())                      # Saída: "Olá, Mundo!"

# replace():
d = "Olá, Mundo!"
print(d.replace('O', 'A'))            # Saída: "Alá, Mundo!"

# split()
e = "Olá, Mundo!"
print(e.split(","))                   # Saída: ['Olá', ' Mundo!'] (lista)