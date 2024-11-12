# JSON (JavaScript Object Notation) é uma sintaxe para armazenar e trocar dados. JSON é frequentemente usado para transmitir dados entre um servidor e uma aplicação web.
# JSON é baseado em texto e usa uma estrutura de chave-valor semelhante a objetos em JavaScript. Ele é amplamente utilizado em APIs e serviços web para enviar dados de forma estruturada.
# O Python tem um módulo integrado chamado json, que pode ser usado para trabalhar com dados JSON:
import json

# Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o método json.dumps():
myDict = {                      # Dicionário (objeto Python)
    "name": "Lucas",
    "age": 28,
    "city": "New York"
}

myJSON = json.dumps(myDict)     # Converte o dicionário em JSON
print(myJSON)                   # Saída: {"name": "Lucas", "age": 28, "city": "New York"} (objeto JSON)

# Você pode converter objetos Python dos seguintes tipos em strings JSON:
# Quando você converte de Python para JSON, os objetos Python são convertidos no equivalente JSON (JavaScript):
'''
Python	    JSON
dict	    Object
list	    Array
tuple	    Array
str	        String
int	        Number
float	    Number
True	    true
False	    false
None	    null
'''
# Exemplo 1: Converta objetos Python em strings JSON e imprima os valores:
print(json.dumps({"name": "Lucas", "age": 30})) # dict para JSON: {"name": "Lucas", "age": 30}  
print(json.dumps(["apple", "bananas"]))         # list para JSON: ["apple", "bananas"]
print(json.dumps(("apple", "bananas")))         # tuple para JSON: ["apple", "bananas"]
print(json.dumps("hello"))                      # str para JSON: "hello"
print(json.dumps(42))                           # int para JSON: 42
print(json.dumps(31.76))                        # float para JSON: 31.76
print(json.dumps(True))                         # True para JSON: true
print(json.dumps(False))                        # False para JSON: false
print(json.dumps(None))                         # None para JSON: null
# Exemplo 2: Converta um objeto Python contendo todos os tipos de dados legais:
myDict = {
    "name": "Lucas",
    "age": 28,
    "married": True,
    "divorced": False,
    "children": ("Luise", "Ben"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

myJSON = json.dumps(myDict) 
print(myJSON)   # Saída: {"name": "Lucas", "age": 28, "married": true, "divorced": false, "children": ["Luise", "Ben"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

# O método json.dumps() possui os parâmetros indent, separators e sort_keys para facilitar a leitura do resultado:
# Use o parâmetro indent (opcional) para definir o número de recuos na identação.
# Você também pode definir os separadores (opcional), o valor padrão é (", ", ": "), o que significa usar uma vírgula e um espaço para separar cada objeto, e dois pontos e um espaço para separar chaves de valores.
# Use o parâmetro sort_keys (opcional) para especificar se o resultado deve ser classificado ou não.
myJSON = json.dumps(myDict, indent=4) 
print(myJSON) 
myJSON = json.dumps(myDict, indent=4, separators=("; ", " = "), sort_keys=True) 
print(myJSON)
''' Saída:
{
    "age" = 28;
    "cars" = [
        {
            "model" = "BMW 230";
            "mpg" = 27.5
        };
        {
            "model" = "Ford Edge";
            "mpg" = 24.1
        }
    ];
    "children" = [
        "Luise";
        "Ben"
    ];
    "divorced" = false;
    "married" = true;
    "name" = "Lucas";
    "pets" = null
}
'''


