from datetime import datetime, timedelta

hoje = datetime.now()   # Data hora de agora: 2024-11-12 11:32:52.863303
print(hoje.date())      # Data de hoje: 2024-11-12

# Para somar valores a uma data é necessário usar a função timedelta() para informar qual é o tipo do valor que será somado (dias, meses, anos, horas etc):
amanha = hoje + timedelta(days=1)           # Soma 1 dia a data especificada
print(amanha.date())                        # Saída: 2024-11-13
semanaQueVem = hoje + timedelta(weeks=2)    # Soma 1 semana a data especificada
print(semanaQueVem.date())                  # Saída: 2024-11-26

# Diferença entre datas:
diferenca = semanaQueVem - amanha
print(diferenca.days)                       # Saída: 13 

# Use o método strptime() para converter uma uma string de qualquer formato em uma data no formato do Python:
dataContrato = "06/08/2020"
dataContrato = datetime.strptime(dataContrato, "%d/%m/%Y")  # "%d/%m/%Y", nexte contexto, é o formato da data que o método está lendo.
print(dataContrato.date())                                  # Saída: 2020-08-06

# Use o método strftime() para converter uma data no formato do Python em uma string de data de qualquer formato:
hoje = hoje.strftime("%d/%m/%Y")    # "%d/%m/%Y", nexte contexto, é o formato da data que você quer como retorno.
print(hoje)                         # Saída: 12/11/2024