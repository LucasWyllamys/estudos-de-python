# Em Python, uma função é definida usando a palavra-chave def:
def my_function(first_name, last_name):
    print(first_name + " " + last_name)

# Chamada da função:
my_function("Lucas", "Wyllamys")    # Saída: Lucas Wyllamys

# Se você não sabe quantos argumentos serão passados ​​para sua função, adicione * (asterisco) antes do nome do parâmetro na definição da função.
# Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens adequadamente:
def my_function(*kids):
    print("O filho mais novo é " + kids[2])

my_function("Emil", "Tobias", "Linus", "Einstein")  # Saída: O filho mais novo é Linus

# Você também pode enviar argumentos com a sintaxe chave = valor.
# Dessa forma, a ordem dos argumentos não importa:
def my_function(child1, child2, child3):
    print("O filho mais novo é " + child2)

my_function(child3="Emil", child1="Tobias", child2="Linus")     # Saída: O filho mais novo é Emil