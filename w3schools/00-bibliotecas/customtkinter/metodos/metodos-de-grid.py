'''
- grid(): Método que divide uma janela ou frame em colunas e linhas, que colapsam quando estão vazias, mas se adaptam ao tamanho dos widgets colocados dentro delas. Define a posição e o padding do widget.
    - row: Parâmetro que define em qual linha do grid o widget está localizado.
    - column: Parâmetro que define em qual coluna do grid o widget está localizado.
    - padx: Parâmetro que define o padding do eixo x.
    - pady: Parâmetro que define o padding do eixo y.
    - sticky: Parâmetro que define como um widget será "ancorado" dentro da célula onde ele é posicionado. Controla o alinhamento do widget em relação aos lados da célula da grade em que está inserido. Por padrão, o widget fica centralizado na célula.
        - Os valores de sticky são definidos com base nos pontos cardeais (Norte, Sul, Leste, Oeste):
            - "n": Norte (topo).
            - "s": Sul (parte inferior).
            - "e": Leste (direita).
            - "w": Oeste (esquerda).
        - Você pode combinar as direções para ajustar o posicionamento:
            - "ns": Alinha-se verticalmente (expande para preencher de Norte a Sul).
            - "ew": Alinha-se horizontalmente (expande para preencher de Leste a Oeste).
            - "nsew": Expande para preencher toda a célula.
    - columnspan: Parâmetro que especifica o número de colunas que um widget deve ocupar dentro de uma grade. Ele permite que o widget "atravesse" várias colunas, ocupando o espaço combinado delas.
        - columnspan=1 (padrão): O widget ocupa apenas uma única coluna (o comportamento padrão).
        - columnspan=n: O widget se estende por n colunas, começando da coluna definida no parâmetro column.

- grid_columnconfigure(): Método que configura o comportamento de uma coluna dentro do layout de grade. Ele permite ajustar propriedades como a largura, peso e se a coluna pode ou não se expandir quando a janela é redimensionada.
    - index: Parâmetro que especifica o índice da coluna que você deseja configurar (começa em 0).
    - weight: Parâmetro que determina a "prioridade" da expansão da coluna quando a janela é redimensionada.
        - 0 (padrão): A coluna não expande.
        - >0: A coluna se expande proporcionalmente ao peso definido.
    - minsize: Parâmetro que define o tamanho mínimo da coluna (em pixels).
    - pad: Parâmetro que adiciona um preenchimento extra ao tamanho da coluna.
'''