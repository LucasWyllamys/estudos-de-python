# Uma "instrução if" é escrita usando a palavra-chave if .
a = 33
b = 200

if b > a:
    print("b é maior que a")
# Saída: b é maior que a

# A palavra-chave elif é a maneira do Python dizer "se as condições anteriores não forem verdadeiras, então tente esta condição".
a = 33
b = 33

if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")
# Saída: a e b são iguais.

# A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores:
a = 200
b = 33

if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")
else:
    print("a é maior que b")
# Saída: a é maior que b

# Você também pode ter um else sem o elif:
a = 200
b = 33

if b > a:
    print("b é maior que a")
else:
    print("b não é maior que a")
# Saída: b não é maior que a

# Se você tiver apenas uma instrução para executar, você pode colocá-la na mesma linha da instrução if:
a = 200
b = 33

if a > b: print("a é maior que b")

# Se você tiver apenas uma instrução para executar, uma para if e uma para else, você pode colocar tudo na mesma linha.
# Essa técnica é conhecida como Operadores Ternários ou Expressões Condicionais:
a = 2
b = 330

print("A") if a > b else print("B")  # Saída: B

# Você também pode ter várias instruções else na mesma linha:
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")   # Saída: =

# As instruções if não podem estar vazias, mas se por algum motivo você tiver uma instrução if sem conteúdo, insira a palavra-cheve 'pass' para evitar um erro:
a = 33
b = 200

if b > a:
    pass    # Não retorna erro!
