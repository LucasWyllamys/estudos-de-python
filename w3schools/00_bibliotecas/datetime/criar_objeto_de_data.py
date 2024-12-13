# Para criar uma data, podemos usar a classe datetime() (construtor) do módulo datetime.
# A classe datetime() requer três parâmetros para criar uma data: ano, mês e dia.
# A classe datetime() também aceita parâmetros para hora e fuso horário (hora, minuto, segundo, microssegundo, tzone), mas eles são opcionais e têm um valor padrão de 0, (None para fuso horário).

import datetime as dt

data = dt.datetime(2020, 5, 17)     # Construtor de data
print(data)                         # Saída: 2020-05-17 00:00:00