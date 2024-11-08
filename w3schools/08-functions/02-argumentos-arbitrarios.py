# Se você não sabe quantos argumentos serão passados ​​para sua função, adicione * (asterisco) antes do nome do parâmetro na definição da função.
# Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens adequadamente:
def my_function(*kids):
    print(kids)     # Saída: ('Emil', 'Tobias', 'Linus', 'Einstein')

my_function("Emil", "Tobias", "Linus", "Einstein")  