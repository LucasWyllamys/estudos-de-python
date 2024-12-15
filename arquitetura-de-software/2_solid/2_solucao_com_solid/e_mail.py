class E_mail:
    @staticmethod
    def enviar(destinatario, assunto, corpo, anexo):
        print(f"Envia e-mail:")
        print(f"\tDestinatário: {destinatario}")
        print(f"\tAssunto: {assunto}")
        print(f"\tCorpo: {corpo}")
        print(f"\tAnexo: {anexo}")