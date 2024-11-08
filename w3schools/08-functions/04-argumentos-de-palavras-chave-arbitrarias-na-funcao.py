# Se você não sabe quantos argumentos de palavra-chave serão passados ​​para sua função, adicione dois asteriscos: **antes do nome do parâmetro na definição da função.
# Dessa forma, a função receberá um dicionário de argumentos e poderá acessar os itens adequadamente:
def my_function(**family):
    print(family)    # Saída: {'father': 'Lucas', 'mather': 'Ise', 'child': 'Luise'}

my_function(father = "Lucas", mather = "Ise", child = "Luise")  