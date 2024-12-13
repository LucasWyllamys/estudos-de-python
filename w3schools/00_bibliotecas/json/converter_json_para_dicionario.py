# JSON (JavaScript Object Notation) é uma sintaxe para armazenar e trocar dados. JSON é frequentemente usado para transmitir dados entre um servidor e uma aplicação web.
# JSON é baseado em texto e usa uma estrutura de chave-valor semelhante a objetos em JavaScript. Ele é amplamente utilizado em APIs e serviços web para enviar dados de forma estruturada.
# O Python tem um módulo integrado chamado json, que pode ser usado para trabalhar com dados JSON:
import json

# Se você tiver uma string JSON, poderá analisá-la usando o método json.loads(). O resultado será um dicionário Python:
myJSON = '{"name":"Lucas", "age":"28", "city":"New York"}'  # JSON

myDict = json.loads(myJSON)                                 # Converte em um dicionário Python
print(myDict["city"])                                       # Saída: New York