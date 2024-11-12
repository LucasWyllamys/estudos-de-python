from datetime import datetime

hoje = datetime.now()   # Retorna a data atual do sistema.
print(hoje)             # Data hora atual do sistema: 2024-11-12 10:46:47.434202

# Métodos de data:
print(hoje.date())      # Data: 2024-11-12
print(hoje.day)         # Dia: 12
print(hoje.month)       # Mês: 11
print(hoje.year)        # Ano: 2024
# Métodos de hora:
print(hoje.time())      # Hora do dia: 10:46:47.434202
print(hoje.hour)        # Hora: 10
print(hoje.minute)      # Minuto: 46
print(hoje.second)      # Segundo: 47

# Use o método strptime() para converter uma uma string de qualquer formato em uma data no formato do Python:
dataContrato = "06/08/2020"
dataContrato = datetime.strptime(dataContrato, "%d/%m/%Y")  # "%d/%m/%Y", nexte contexto, é o formato da data que o método está lendo.
print(dataContrato.date())                                  # Saída: 2020-08-06

# Use o método strftime() para converter uma data no formato do Python em uma string de data de qualquer formato:
hoje = hoje.strftime("%d/%m/%Y")    # "%d/%m/%Y", nexte contexto, é o formato da data que você quer como retorno.
print(hoje)                         # Saída: 12/11/2024