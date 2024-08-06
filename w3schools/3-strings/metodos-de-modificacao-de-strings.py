# O método upper() retorna a string em maiúsculas.
a = "Olá, Mundo!"
print(a.upper())                      # Saída: "OLÁ, MUNDO!"

# O método lower() retorna a string em letras minúsculas:
b = "Olá, Mundo!"
print(b.lower())                      # Saída: "olá, mundo!

# O método strip() remove qualquer espaço em branco do início ou do fim:
c = " Olá, Mundo! "
print(c.strip())                      # Saída: "Olá, Mundo!"

# O método replace() substitui uma string por outra string:
d = "Olá, Mundo!"
print(d.replace('O', 'A'))            # Saída: "Alá, Mundo!"

# O método split() retorna uma lista onde o texto entre o separador especificado se torna os itens da lista.
# O método split() divide a string em substrings se encontrar instâncias do separador:
e = "Olá, Mundo!"
print(e.split(","))                   # Saída: ['Olá', ' Mundo!'] (lista)