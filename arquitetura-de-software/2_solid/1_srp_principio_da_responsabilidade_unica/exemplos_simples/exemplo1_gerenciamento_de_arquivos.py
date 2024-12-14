'''
○ Single Responsibility Principle - SRP (Princípio da Responsabilidade Única): Uma classe, módulo, componente, função, entidade etc., deve ter apenas uma responsabilidade. 
    § Benefícios: 
        □ Facilidade de manutenção: Mudanças em uma responsabilidade não afetam outras.
        □ Testabilidade: Classes menores e focadas são mais fáceis de testar.
        □ Reutilização: Classes focadas podem ser reutilizadas em outros contextos.
'''

# Violação do Princípio: Uma única classe realiza múltiplas tarefas: gerencia dados e salva informações no disco:
''' 
# Quebra o SRP
class FileManager:
    def __init__(self, data):
        self.data = data

    def save_to_file(self, file_name):
        with open(file_name, 'a') as file:
            file.write(self.data)

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            self.data = file.read()
'''

# Solução com SRP: Separe as responsabilidades em classes distintas:

class DataHandler:  # Classe para manipular dados.
    def __init__(self, data=""):
        self.data = data

    def update_data(self, new_data):    # Método para atualizar o dado.
        self.data = new_data

class FileManeger: # Classe para gerenciar arquivos.
    @staticmethod
    def save_to_file(data, file_name):  # Método para escrever/salvar os dados novos ou modificados no arquivo.
        with open(file_name, "a") as file:  #  Adicionar ao conteúdo existente em vez de sobrescrevê-lo, use o modo "a".
            file.write("\n" + data)  # Adiciona uma linha nova.

    @staticmethod
    def load_from_file(file_name):  # Método para carregar as informações/dados do arquivo.
        with open(file_name, "r") as file:
            return file.read()

data_handler = DataHandler("Hello, Word!")                  # Instancia o objeto e armazena o dado.
FileManeger.save_to_file(data_handler.data, "example1.txt")  # Salva o dado no arquivo.
loaded_data = FileManeger.load_from_file("example1.txt")     # Retorna a informação lida do arquivo.
data_handler.update_data(loaded_data)                       # Atualiza o atributo na classe com o novo dado.   