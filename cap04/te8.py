# Collections: OrderedDict

# Importando:
from collections import OrderedDict 

# Criando:
dicio_ordenado = OrderedDict()
print(dicio_ordenado)

# Adicionando chaves e valores:
dicio_ordenado["NOME"] = "Smatphone"
dicio_ordenado["MARCA"] = "Samsung"
dicio_ordenado["MODELO"] = "S23"

# Pecorrendo para verificar a ordem:
for chave, valor in dicio_ordenado.items():
    print(f"{chave} -- {valor}")
    
# Alterando um novo item:
dicio_ordenado["MARCA"] = "Galaxy"
print(f"\n\t{dicio_ordenado['MARCA']}\n")

# Pecorrendo para verificar a ordem:
for chave, valor in dicio_ordenado.items():
    print(f"{chave} -- {valor}")
    
# Removendo um item:
dicio_ordenado.pop("MARCA")
print(f"\n\t{dicio_ordenado}\n")

# Pecorrendo para verificar a ordem:
for chave, valor in dicio_ordenado.items():
    print(f"{chave} -- {valor}")
    
# Reinserindo um item:
dicio_ordenado["MARCA"] = "Samsung"
print(f"\n\t{dicio_ordenado['MARCA']}\n")

# Pecorrendo para verificar a ordem:
for chave, valor in dicio_ordenado.items():
    print(f"{chave} -- {valor}")