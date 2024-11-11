# A palavra-chave nonlocal é usada para trabalhar com variáveis ​​dentro de funções aninhadas.
# A palavra-chave nonlocal faz com que a variável pertença à função externa:
def myFunc1():
    x = "Lucas"
    def myFunc2():
        nonlocal x   # Sem esta declaração o valor de retorno da função seria x = "Lucas"
        x = "Wyllamys"
    myFunc2()
    return x

print(myFunc1())    # Saída: Wyllamys