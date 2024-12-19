from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.DEBUG)

# Interface (classe abstrata) (contrato público claro): 
class iTemplate(ABC):
    @abstractmethod
    def renderizar(self, caminho_template: str, dados: dict, caminho_repositorio: str):
        pass
    
# Implementação da interface:
class TemplateHTML(iTemplate):
    def __init__(self):     # Configurações iniciais para manipulação do arquivo HTML.
        logging.debug(f"Configurações iniciais para manipular arquivos HTLM.")
        self.html_template = None
        self.new_html_template = None

    def renderizar(self, caminho_template: str, dados: dict, caminho_repositorio: str):
        self.__carregar(caminho_template)
        self.__substituir(dados)
        return self.__salvar(caminho_repositorio)

    def __carregar(self, caminho_template: str):     # Pega o caminho do template e armazena o HTML.
        self.html_template = "HTML original do template"
        logging.debug(f"Carrega o template: {caminho_template}, e armazena o html: {self.html_template}")

    def __substituir(self, dados: dict):    # Substitui as variáveis no HTML do template pelos dados fornecidos e armazena os dados novos.                
        logging.debug(f"Substitui os dados: {dados}, no HTLM: {self.html_template}")
        self.new_html_template = "Novo HTML!"

    def __salvar(self, caminho_repositorio: str):     # Salva um novo arquivo HTML com os dados renderizados.   
        logging.debug(f"Salva um novo arquivo HTML com os dados: {self.new_html_template}, no repositório: {caminho_repositorio}")
        return "caminho_novo_arquivo_renderizado"
    
# Implementação da interface:
class TemplateWord(iTemplate):
    def __init__(self):     # Configurações iniciais para manipulação do arquivo Word.
        logging.debug(f"Configurações iniciais para manipular arquivos Word.")
        self.template_word = None

    def renderizar(self, caminho_template: str, dados: dict, caminho_repositorio: str):
        self.__carregar(caminho_template)
        self.__substituir(dados)
        return self.__salvar(caminho_repositorio)

    def __carregar(self, caminho_template: str):     # Pega o caminho do template Word e abre.
        logging.debug(f"Carrega o template: {caminho_template}.")

    def __substituir(self, dados: dict):    # Substitui as variáveis no template Word pelos dados fornecidos.            
        logging.debug(f"Substitui os dados: {dados}, no template Word: {self.template_word}")

    def __salvar(self, caminho_repositorio: str):     # Salva um novo arquivo Word com os dados renderizados.   
        logging.debug(f"Salva um novo arquivo Word com os dados renderizados, no repositório: {caminho_repositorio}")
        return "caminho_novo_arquivo_renderizado"