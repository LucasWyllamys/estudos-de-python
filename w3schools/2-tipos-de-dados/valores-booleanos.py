# Quase todo valor é avaliado True se tem algum tipo de conteúdo.
print(bool('abc'))                      # Saída: true (Qualquer string é True, exceto strings vazias.)
print(bool(123))                        # Saída: false (Qualquer número é True, exceto 0.)
print(bool(['maça', 'uva', 'banana']))  # Saída: true (Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.)

# Na verdade, não há muitos valores que avaliam para False, exceto valores vazios, como (), [], {}, "", o número 0e o valor None. E, claro, o valor Falseavalia para False.