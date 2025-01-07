# Levantar uma exceção: Como desenvolvedor Python, você pode escolher lançar uma exceção se uma condição ocorrer.
# Para lançar (ou levantar) uma exceção, use a palavra-chave raise.

# Gera um erro e interrompe o programa se x for menor que 0:
x = -1

if x < 0:
    raise Exception("Desculpe, não há números abaixo de zero.") 
# Saída:
#Traceback (most recent call last):
#  File "c:\Users\U350504\Documents\GitHub\estudos-de-python\w3schools\14_raise\raise.py", line 8, in <module>
#    raise Exception("Desculpe, não há números abaixo de zero.")
#Exception: Desculpe, não há números abaixo de zero.

print("Este comando será executado apenas se não ocorrer a exceção.")

# A palavra-chave raise é usada para gerar uma exceção.
# Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário:
# Gera um TypeError se x não for um inteiro:
x = "hello"

if not type(x) is int:
    raise TypeError("Somente números inteiros são permitidos.")