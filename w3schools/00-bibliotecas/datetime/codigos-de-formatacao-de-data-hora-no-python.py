'''
Directive	  Description	                                                                    Example
%a	          Dia da semana, versão curta	                                                    Wed
%A	          Dia da semana, versão completa	                                                Wednesday                            
%w	          Dia da semana como um número de 0 a 6, 0 é domingo                                3
%d	          Dia do mês de 01 a 31                                                             31
%b	          Nome do mês, versão curta                                                         Dec
%B	          Nome do mês, versão completa                                                      December
%m	          Mês como um número de 01 a 12                                                     12
%y	          Ano, versão curta, sem século                                                     18
%Y	          Ano, versão completa                                                              2018
%H	          Hora 00 a 23                                                                      17
%I	          Hora 00 a 12                                                                      05
%p	          AM/PM                                                                             PM
%M	          Minuto 00 a 59                                                                    41
%S	          Segundo 00 a 59                                                                   08
%f	          Microssegundo 000000 a 999999                                                     548513
%z	          Deslocamento UTC                                                                  +0100
%Z	          Fuso horário                                                                      CST
%j	          Número do dia do ano 001 a 366                                                    365
%U	          Número da semana do ano, domingo como o primeiro dia da semana, 00 a 53           52
%W	          Número da semana do ano, segunda-feira como o primeiro dia da semana, 00 a 53     52
%c	          Versão local da data e hora                                                       Mon Dec 31 17:41:00 2018
%C	          Século                                                                            20
%x	          Versão local da data                                                              12/31/18
%X	          Versão local da hora                                                              17:41:00
%%	          Um caractere %                                                                    %
%G	          Ano ISO 8601                                                                      2018
%u	          ISO 8601 dia da semana (1-7)                                                      1
%V	          ISO 8601 número da semana (01-53)                                                 01
'''

# Exemplos:
from datetime import datetime

hoje = datetime.now()
print(hoje)                 # Saída: 2024-11-12 13:19:35.414494
print(hoje.strftime("%a"))  # Saída: Tue
print(hoje.strftime("%A"))  # Saída: Tuesday
print(hoje.strftime("%w"))  # Saída: 2
print(hoje.strftime("%d"))  # Saída: 12
print(hoje.strftime("%b"))  # Saída: Nov
print(hoje.strftime("%B"))  # Saída: November
print(hoje.strftime("%m"))  # Saída: 11
print(hoje.strftime("%y"))  # Saída: 24
print(hoje.strftime("%Y"))  # Saída: 2024
print(hoje.strftime("%H"))  # Saída: 13
print(hoje.strftime("%I"))  # Saída: 01
print(hoje.strftime("%p"))  # Saída: PM
print(hoje.strftime("%M"))  # Saída: 02
print(hoje.strftime("%S"))  # Saída: 47
print(hoje.strftime("%f"))  # Saída:
print(hoje.strftime("%z"))  # Saída:
print(hoje.strftime("%Z"))  # Saída:
print(hoje.strftime("%j"))  # Saída: 317
print(hoje.strftime("%U"))  # Saída: 45
print(hoje.strftime("%W"))  # Saída: 46
print(hoje.strftime("%c"))  # Saída: Tue Nov 12 13:07:09 2024
print(hoje.strftime("%C"))  # Saída: 20
print(hoje.strftime("%x"))  # Saída: 11/12/24
print(hoje.strftime("%X"))  # Saída: 13:07:09
print(hoje.strftime("%%"))  # Saída: %
print(hoje.strftime("%G"))  # Saída: 2024
print(hoje.strftime("%u"))  # Saída: 2
print(hoje.strftime("%V"))  # Saída: 46