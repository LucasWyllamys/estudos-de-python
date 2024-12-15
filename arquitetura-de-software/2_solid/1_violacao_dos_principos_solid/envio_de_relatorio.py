''' SOLID:
    - SRP: Uma classe, módulo, componente, função, entidade etc., deve ter apenas uma responsabilidade, ou seja, deve ter apenas um motivo para ser modificada.
    - OCP: Classes, objetos, métodos, entidades, funções etc., devem estar abertos para extensão, mas fechados para modificações.
    - LSP: Classes derivadas devem ser capazes de substituir totalmente classes-bases.
    - ISP: As classes não devem ser forçadas a depender de interfaces que não utilizam.
    - DIP: Módulos de alto nível não devem ser dependentes de módulos de baixo nível; ambos devem depender de abstrações. Detalhes devem depender de abstrações, não o inverso.
'''

''' Violação do Princípio SRP: A classe abaixo gera, salva, exibe, imprime e envia relatórios (god class). Isso provoca vários problemas, pois a classe tem várias responsabilidades fazendi com que a classe tenha vários motivos para ser modificada:
    - E se o repositório mudar?
    - E se o banco mudar?
    - E se o serviço de impressão mudar?
    - E se o serviço de e-mail mudar?
'''
class Relatorio:
    def __init__(self, dados, caminho_template, caminho_repositorio):
        self.dados = dados                                  # Dados que serão usado para gerar o relatório.
        self.caminho_template = caminho_template            # Caminho do template que será usado para gerar o relatório.
        self.caminho_repositorio = caminho_repositorio      # Caminho do repositório onde o relatório será armazenado.
        self.caminho_relatorio = ""                         # Caminho completo do arquivo do relatório.

    def gerar(self):
        print(f"Gerando relatório com os dados: {self.dados}, usando o template: {self.caminho_template}")

    def salvar_no_repositorio(self):
        print(f"Salvando no repositório o arquivo do relatório: {self.caminho_repositorio}")
        self.caminho_relatorio = self.caminho_repositorio + r"relatorios\relatorio.pdf"

    def salvar_no_banco(self):
        print(f"Salvando no banco o caminho do relatório: {self.caminho_relatorio}")

    def exibir(self):
        print(f"Exibindo na tela o relatório: {self.caminho_relatorio}")

    def imprimir(self):
        print(f"Imprimindo na impressora o relatório: {self.caminho_relatorio}")

    def enviar(self):
        print(f"Enviando por e-mail o relatório: {self.caminho_relatorio}")

dados = {"Nome": "Lucas", "Idade": 28}
caminho_template = r"C:\Users\lucas\Documents\index.html"
caminho_repositorio = r"C:\Users\lucas\Documents\GitHub"
relatorio = Relatorio(dados, caminho_template, caminho_repositorio)

relatorio.gerar()  
relatorio.salvar_no_repositorio()  
relatorio.salvar_no_banco()        
relatorio.exibir() 
relatorio.imprimir() 
relatorio.enviar()