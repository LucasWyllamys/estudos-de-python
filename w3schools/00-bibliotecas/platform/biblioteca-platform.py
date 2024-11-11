# A biblioteca platform no Python é usada para acessar informações sobre a plataforma na qual o programa está sendo executado. Isso inclui detalhes sobre o sistema operacional, a versão do Python, o hardware e outros aspectos do ambiente de execução.

import platform

print("Sistema Operacional:", platform.system())        # Sistema Operacional: Windows
print("Versão do SO:", platform.version())              # Versão do SO: 10.0.19045
print("Arquitetura:", platform.architecture())          # Arquitetura: ('64bit', 'WindowsPE')
print("Versão do Python:", platform.python_version())   # Versão do Python: 3.12.5

