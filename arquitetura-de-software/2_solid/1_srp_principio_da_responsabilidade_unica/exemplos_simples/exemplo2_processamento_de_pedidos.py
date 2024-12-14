'''
○ Single Responsibility Principle - SRP (Princípio da Responsabilidade Única): Uma classe, módulo, componente, função, entidade etc., deve ter apenas uma responsabilidade. 
    § Benefícios: 
        □ Facilidade de manutenção: Mudanças em uma responsabilidade não afetam outras.
        □ Testabilidade: Classes menores e focadas são mais fáceis de testar.
        □ Reutilização: Classes focadas podem ser reutilizadas em outros contextos.
'''

# Violação do Princípio: Uma única classe gerencia pedidos, calcula preços e processa pagamentos:
'''
# Quebra o SRP
class OrderManager:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def process_payment(self, total):
        print(f"Processing payment of ${total}")
'''

# Solução com SRP: Crie classes para separar responsabilidades:

class Order:        # Classe para gerenciar os pedidos.
    def __init__(self, items):
        self.items = items

    def calculate_total(self):      # Método que retorna o montante dos itens da ordem.
        return sum(item['price'] * item['quantity'] for item in self.items)

class PaymentProcessor:     # Classe para processar o pagamento.
    @staticmethod
    def process_payment(amount):    # Método que processa o pagamento.
        print(f"Processando pagamento de R$ {amount}")

order = Order([     # Instancia a classe com os itens da ordem de pagamento.
    {"price": 10.0, "quantity": 2},
    {"price": 5.0, "quantity": 4}
])
total = order.calculate_total()     # Calcula a soma total dos valores dos itens
PaymentProcessor.process_payment(total)     # Processa o pagamento. Saída: Processando pagamento de R$ 40.0
