''' Solução com SRP: Segregar as classes por responsabilidade e usar herança para referenciá-las:

'''
from relatorio import Relatorio
from impressora import Impressora
from e_mail import E_mail

relatorio = Relatorio()
relatorio.gerar(
    {"Nome": "Lucas", "Idade": 28}, 
    r"C:\Users\lucas\Documents\index.html"
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