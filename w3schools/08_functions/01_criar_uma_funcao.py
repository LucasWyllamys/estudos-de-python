# Em Python, uma função é definida usando a palavra-chave def:
def my_function(first_name, last_name):
    print(first_name + " " + last_name)     # Saída: Lucas Wyllamys

# Chamada da função:
my_function("Lucas", "Wyllamys")    

# definições function não podem estar vazias, mas se por algum motivo você tiver uma definição function sem conteúdo, insira a declaração pass para evitar um erro:
def my_function2():
    pass

my_function2()  # Não gera erro!