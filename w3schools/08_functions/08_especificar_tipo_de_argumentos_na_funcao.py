# Para especificar que uma função pode ter apenas argumentos posicionais, adicione , / após os argumentos.
# Sem isso, , / você tem permissão para usar argumentos de palavras-chave, mesmo que a função espere argumentos posicionais.
# Mas ao adicionar, , / você receberá um erro se tentar enviar um argumento de palavra-chave.
def my_function(x, /):
    print(x)

my_function(3)

# Para especificar que uma função pode ter apenas argumentos de palavras-chave, adicione *, antes dos argumentos.
# Sem isso, *, você tem permissão para usar argumentos posicionais mesmo que a função espere argumentos de palavra-chave.
# Mas com isso *, você receberá um erro se tentar enviar um argumento posicional.
def my_function2(*, x):
    print(x)

my_function2(x = 3)

# Você pode combinar os dois tipos de argumentos na mesma função.
# Qualquer argumento antes de / ,é somente posicional, e qualquer argumento depois de é *, somente palavra-chave.
def my_function3(a, b, /, *, c, d):
    print(a + b + c + d)

my_function3(5, 6, c = 7, d = 8)