'''
○ Single Responsibility Principle - SRP (Princípio da Responsabilidade Única): Uma classe, módulo, componente, função, entidade etc., deve ter apenas uma responsabilidade. 
    § Benefícios: 
        □ Facilidade de manutenção: Mudanças em uma responsabilidade não afetam outras.
        □ Testabilidade: Classes menores e focadas são mais fáceis de testar.
        □ Reutilização: Classes focadas podem ser reutilizadas em outros contextos.
'''

# Problema: Uma classe gerencia usuários e envia emails:
'''
# Quebra o SRP
class UserManager:
    def __init__(self, users):
        self.users = users

    def send_email(self, user, subject, body):
        print(f"Sending email to {user['email']}: {subject}\n{body}")
'''

# Solução com SRP: Separe a lógica de gerenciamento de usuários e envio de emails:
class UserManager:  # Classe para gerenciar os usuários.
    def __init__(self, users):
        self.users = users

class EmailService:     # Classe para envio de e-mails.
    @staticmethod
    def send_email(users, subject, body):    # Método que envia o e-mail.
        for user in users:
            print(f"Destinatário: {user['email']}")
            print(f"Assunto: {subject}")
            print(f"Corpo: {body}\n")

users = [   # Lista de usuários.
        {
            "name": "Lucas", 
            "email": "lucas@example.com"
         }, 
        {
            "name": "Ise", 
            "email": "ise@example.com"
        }
    ]
user_manager = UserManager(users)   # Instancia a classe que gerencia os usuários.
EmailService.send_email(user_manager.users, "Texto do assunto", "E-mail enviado!")  # Envia o e-mail (direto da classe sem instanciar).