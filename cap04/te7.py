
from collections import defaultdict

# Criação de um dicionário padrão - Default

dicio_list = defaultdict(list)
dicio_list["PRODUTO"] = "Acer Aspire"
dicio_list["MARCA"] = "Acer"

print(f"Exibindo a chave PRODUTO: {dicio_list['PRODUTO']}")
print(f"Exibindo a chave PREÇO: {dicio_list['PREÇO']}")

# Criação de função que retorna "INEXISTENTE":
def funcao_exemplo():
    return "INEXISTENTE"

dicio_list = defaultdict(funcao_exemplo)
dicio_list["PRODUTO"] = "Acer Aspire"
dicio_list["MARCA"] = "Acer"

print(f"Exibindo a chave PRODUTO com uma função: {dicio_list['PRODUTO']}")
print(f"Exibindo a chave PREÇO com uma função: {dicio_list['PREÇO']}")

# Criação de dicionário com uma função LAMBDA:
dicio_list = defaultdict(lambda: "Não disponível")
dicio_list["PRODUTO"] = "Acer Aspire"
dicio_list["MARCA"] = "Acer"

print(f"Exibindo a chave PRODUTO com uma função 'lambda': {dicio_list['PRODUTO']}")
print(f"Exibindo a chave PREÇO com uma função 'lambda': {dicio_list['PREÇO']}")