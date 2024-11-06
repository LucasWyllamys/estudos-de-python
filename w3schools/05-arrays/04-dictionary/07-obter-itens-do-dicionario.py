# O método items() retornará cada item em um dicionário, como tuplas em uma lista.
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisDict.items()
print(x)
# Saída: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# A lista retornada é uma visualização dos itens do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de itens:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)
# Saída: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020      # Modificação de item existente
car["color"] = "red"    # Novo item

print(x)
# Saída: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'red')])
