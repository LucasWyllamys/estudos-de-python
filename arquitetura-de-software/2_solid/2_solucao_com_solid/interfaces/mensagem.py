from abc import ABC, abstractmethod
from typing import Optional

# Interface (classe abstrata): 
class iMensagem(ABC):
    @abstractmethod       
    def enviar(self, parametros: dict):
        '''Parâmetros:
            mensagem: str, 
            corpo: str
            destinatario: str, 
            numero_celular: str, 
            assunto: str, 
            caminho_anexo: str
        '''
        pass

