# Como retornar uma cadeia de string dentro de uma string.
# Obs.: O primeiro caractere tem índice 0.
# Obs.: A última posição não é inclusa.
b = "Lucas Wyllamys"
print(b[2:5])
# Saída: "cas " (retorna a cadeia de string da posição 2 até a 5, a posição 5 não é inclusa!).

# Ao deixar de fora o índice inicial, o intervalo começará no primeiro caractere:
b = "Lucas Wyllamys"
print(b[:5])
# Saída: Lucas

# Ao deixar de fora o índice final, o intervalo irá até o fim:
b = "Lucas Wyllamys"
print(b[2:])
# Saída: cas Wyllamys

# Use índices negativos para iniciar a fatia a partir do final da string:
b = "Lucas Wyllamys"
print(b[-5:-2])
# Saída: lam (l na posição -5 partindo de s com índice 0 (final da string), m (não incluso) na posição -2 partindo de s com índice 0).