from abc import ABC, abstractmethod
import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG)

# Interface (classe abstrata) (contrato público claro): 
class iMensagem(ABC):
    @abstractmethod       
    def enviar(self, numero_celular: str, mensagem: str, caminho_anexo: Optional[str] = None):
        pass

# Interface (classe abstrata) (contrato público claro): 
class iEmail(iMensagem):    # Uso de herança, extendendo a classe iMensagem.
    @abstractmethod 
    def enviar(self, destinatario: str, assunto: str, corpo: str, caminho_anexo: Optional[str] = None):
        pass

# Implementação da interface (iMenssagem):
class WhatsApp(iMensagem):
    def __init__(self):
        logging.debug("Estabelece as conexões com o WhatsApp.")

    def enviar(self, numero_celular: str, mensagem: str, caminho_anexo: Optional[str] = None):
        logging.debug(f"Envia mensagem pelo WhatsApp:")
        logging.debug(f"\tNúmero do WhatsApp: {numero_celular}")
        logging.debug(f"\tMensagem: {mensagem}")
        if caminho_anexo: self.anexar(caminho_anexo)

    def anexar(self, caminho_anexo: str):
        logging.debug(f"\tAnexo: {caminho_anexo}")

# Implementação da interface (iMenssagem):
class SMS(iMensagem):
    def __init__(self):
        logging.debug("Estabelece as conexões com o SMS.")

    def enviar(self, numero_celular: str, mensagem: str):
        logging.debug(f"Envia mensagem pelo SMS:")
        logging.debug(f"\tNúmero do Telefone: {numero_celular}")
        logging.debug(f"\tMensagem: {mensagem}")

# Implementação da interface (iEmail):
class EmailSMTP(iEmail):
    def __init__(self):
        logging.debug("Estabelece as conexões com o servidor de e-mail SMTP.")

    def enviar(self, destinatario: str, assunto: str, corpo: str, caminho_anexo: Optional[str] = None):
        logging.debug(f"Envia e-mail:")
        logging.debug(f"\tDestinatário: {destinatario}")
        logging.debug(f"\tAssunto: {assunto}")
        logging.debug(f"\tCorpo: {corpo}")
        if caminho_anexo: self.anexar(caminho_anexo)

    def anexar(self, caminho_anexo: str):
        logging.debug(f"\tAnexo: {caminho_anexo}")

# Implementação da interface (iEmail):
class EmailOutlook(iEmail):
    def __init__(self):
        logging.debug("Estabelece as conexões com o servidor de e-mail OUTLOOK.")

    def enviar(self, destinatario: str, assunto: str, corpo: str, caminho_anexo: Optional[str] = None):
        logging.debug(f"Envia e-mail:")
        logging.debug(f"\tDestinatário: {destinatario}")
        logging.debug(f"\tAssunto: {assunto}")
        logging.debug(f"\tCorpo: {corpo}")
        if caminho_anexo: self.anexar(caminho_anexo)

    def anexar(self, caminho_anexo: str):
        logging.debug(f"\tAnexo: {caminho_anexo}")