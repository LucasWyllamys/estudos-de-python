''' SOLID:
    - SRP: Uma entidade de software (classe, módulo, componente, função etc.) deve ter apenas uma responsabilidade, ou seja, deve ter apenas um motivo para ser modificada.
    - OCP: Entidades de software (classes, objetos, métodos, funções etc.) devem estar abertos para extensão, mas fechados para modificações.
    - LSP: Classes derivadas devem ser capazes de substituir totalmente classes-bases.
    - ISP: As classes não devem ser forçadas a depender de interfaces que não utilizam.
    - DIP: Módulos de alto nível não devem ser dependentes de módulos de baixo nível; ambos devem depender de abstrações. Detalhes devem depender de abstrações, não o inverso.
'''
from relatorio import Relatorio
from repositorio import Repositorio
from impressora import Impressora
from e_mail import E_mail

relatorio = Relatorio()
relatorio.gerar(
    {"Nome": "Lucas", "Idade": 28}, 
    r"C:\Users\lucas\Documents\index.html",
    Repositorio().caminho_repositorio
)
relatorio.exibir()

impressora = Impressora()
impressora.imprimir(relatorio.caminho_relatorio)

email = E_mail()
email.enviar(
    "lucas.wyllamys@outlook.com", 
    "Teste de envio de relatório", 
    "Segue anexo relatório.",
    relatorio.caminho_relatorio
)