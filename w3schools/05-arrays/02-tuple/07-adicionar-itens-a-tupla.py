# Como as tuplas são imutáveis, elas não têm um método interno append(), mas existem outras maneiras de adicionar itens a uma tupla:

# 1. Converter em uma lista: assim como na solução alternativa para alterar uma tupla, você pode convertê-la em uma lista, adicionar seus itens e convertê-la novamente em uma tupla:
thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")

thisTuple = tuple(y)
print(thisTuple)  # Saída: ('apple', 'banana', 'cherry', 'orange')

# 2. Adicione tupla a uma tupla. Você tem permissão para adicionar tuplas a tuplas, então se você quiser adicionar um item, (ou muitos), crie uma nova tupla com o(s) item(ns), e adicione-a à tupla existente:
thisTuple = ("apple", "banana", "cherry")
# Nota: Ao criar uma tupla com apenas um item, lembre-se de incluir uma vírgula após o item, caso contrário ela não será identificada como uma tupla.
y = ("orange",)
thisTuple += y  # Soma as tuples

print(thisTuple)  # Saída: ('apple', 'banana', 'cherry', 'orange')
