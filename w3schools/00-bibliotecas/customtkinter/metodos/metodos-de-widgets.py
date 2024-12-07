'''
CTkButton(): Método que cria um botão.
    - master: Parâmetro que especifica a janela na qual o botão será localizado.
    - text: Parâmetro que define o texto do botão.
    - command: Parâmetro que define a função de Call Back que será executada quando o botão for pressionado.

CTkCheckBox(): Método que cria um CheckBox.
    - master: Parâmetro que especifica a janela na qual o botão será localizado.
    - text: Parâmetro que define o texto do CheckBox.

CTKLabel(): Método que cria um rótulo.
    - master: Parâmetro que especifica a janela na qual o rótulo será localizado.
    - text: Parâmetro que define o texto do rótulo.
    - fg_color: Parâmetro que define a cor de fundo do rótulo.
        - Cor personalizada: Você pode passar uma cor específica, como uma string no formato hexadecimal (e.g., "#FFFFFF") ou um nome de cor reconhecido pelo CustomTKinter (e.g., "red").
        - Cor padrão: Se você não definir fg_color, ele usará a cor padrão do tema.
        - Transparente: Defina fg_color=None se quiser que o fundo seja transparente (ou use a cor do widget pai como fundo).
    - corner_radius: Parâmetro que define o raio das bordas arredondadas de um widget. 

CTkRadioButton():    

winfo_children(): Retorna todos os widgets filhos do widget pai.

get(): Retorna o estado do widget.

cget(): Retorna o valor do atributo especificado entre os parênteses.

set(): Atribue o valor especificado (entre parêntese) à variável do tipo: variable = ctk.StringVar(value="")
    - Ex.: variable.set(value)
'''