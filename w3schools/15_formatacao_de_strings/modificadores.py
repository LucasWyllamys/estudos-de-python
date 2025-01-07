# Um espaço reservado também pode incluir um modificador para formatar o valor.
# Um modificador é incluído adicionando dois pontos : seguidos de um tipo de formatação legal, como .2f (que significa número de ponto fixo com 2 decimais).

'''
Modificador         Descrição
:<		            Alinha o resultado à esquerda (dentro do espaço disponível).
:>		            Alinha o resultado à direita (dentro do espaço disponível).
:^		            O centro alinha o resultado (dentro do espaço disponível).
:=		            Coloca o sinal na posição mais à esquerda.
:+		            Use um sinal de mais para indicar se o resultado é positivo ou negativo.
:-		            Use um sinal de menos somente para valores negativos.
: 		            Use um espaço para inserir um espaço extra antes de números positivos (e um sinal de menos antes de números negativos).
:,                  Use uma vírgula como separador de milhar.                      		                
:_		            Use um sublinhado como separador de milhar.
:b		    
:c		         
:d		         
:e		        
:E		          
:f		      
:F		         
:g		           
:G		            
:o		        
:x		           
:X		         
:n		            
:%		             
'''

# Exemplos:----------------------------------------------------------------------

# Exibir o preço com 2 casas decimais:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  # Saída: The price is 59.00 dollars

# Você também pode formatar um valor diretamente sem mantê-lo em uma variável:
txt = f"The price is {95:.2f} dollars"
print(txt)  # Saída: The price is 95.00 dollars

# Use uma vírgula como separador de milhar:
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)  # Saída: The price is 59,000 dollars