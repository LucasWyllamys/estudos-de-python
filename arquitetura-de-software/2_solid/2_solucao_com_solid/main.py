''' SOLID:
    - SRP: Uma entidade de software (módulo, classe, método, função, componente etc.) deve ter apenas uma responsabilidade, ou seja, deve ter apenas um motivo para ser modificada.
    - OCP: Entidades de software (módulo, classe, método, função, componente etc.) devem estar abertos para extensão, mas fechados para modificações.
    - LSP: Classes derivadas devem ser capazes de substituir totalmente classes-bases.
    - ISP: As classes não devem ser forçadas a depender de interfaces que não utilizam.
    - DIP: Módulos de alto nível não devem ser dependentes de módulos de baixo nível; ambos devem depender de abstrações. Detalhes devem depender de abstrações, não o inverso.
'''
from relatorio import Relatorio
import impressora
import repositorios
from implementations import mensagem
import template as temp

relatorio = Relatorio(temp.TemplateHTML(), impressora.ImpressoraB(), mensagem.EmailOutlook())
relatorio.gerar(
    r"C:\Users\lucas\Documents\index.html",
    {"Nome": "Lucas", "Idade": 28}, 
    repositorios.path["repositorio2"]
)
relatorio.exibir()
relatorio.imprimir()
relatorio.enviar(
    {
        "destinatario":     "lucas.wyllamys@outlook.com", 
        "assunto":          "Teste de envio de relatório", 
        "corpo":            "Olá, Mundo!",
        "caminho_anexo":    relatorio.caminho_relatorio
    }
)
'''Parâmetros:
    mensagem: str, 
    corpo: str
    destinatario: str, 
    numero_celular: str, 
    assunto: str, 
    caminho_anexo: str
'''