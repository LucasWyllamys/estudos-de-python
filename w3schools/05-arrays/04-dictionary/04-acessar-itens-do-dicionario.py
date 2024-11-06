# Você pode acessar os itens de um dicionário consultando seu nome de chave, dentro de colchetes:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisDict["model"]
print(x)    # Saída: Mustang

# Existe também um método chamado get() que lhe dará o mesmo resultado:
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisDict.get("model")
print(x)    # Saída: Mustang
