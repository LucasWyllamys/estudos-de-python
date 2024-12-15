# Para inserir caracteres ilegais em uma string, use um caractere de escape.
# Um caractere de escape é uma barra invertida (\) seguida pelo caractere que você deseja inserir.
''' Caracteres de escape:
\'                  Citação única
\\                  Barra invertida
\n                  Linha nova
\r                  Retorno de transporte    
\t                  Tab
\b                  Backspace (apaga o caractere anterior)
\f
\ooo
'''

# Um exemplo de caractere ilegal são aspas duplas dentro de uma string cercada por aspas duplas.
txt = 'Nós somos os chamados \'Vikings\' do norte'  
print(txt)  # Saída: "Nós somos os chamados 'Vikings' do norte"