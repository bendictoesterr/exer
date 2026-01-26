# Dicionários:

# Criação do dicionário:
dicio = {
    "nome": "Ester Bendicto",
    "idade": 20,
    "dia de nascimento": 26,
    "mês de nascimento": "abril"
}

print(dicio)

print(f"\n\tO valor da chave idade é {dicio['idade']}")

# Inserindo uma nova chave e valor:
dicio["ano de nascimento"] = 2005
print(dicio)

# Método KEYS (Mostra as chaves):
print(dicio.keys())
for chave in dicio.keys():
    print(chave)

# Método VALUES
print(dicio.values())
for valor in dicio.values():
    print(valor)

# Método ITEMS
print(dicio.items())
for chave, valor in dicio.items():
    print(f"{chave} -- {valor}")

# Método GET 
print(dicio.get("cpf"))
print(dicio.get("nome"))

# Método SETDEFAULT
dicio.setdefault("cor", "laranja")
dicio.setdefault("cor", "roxo") # → não vai adicionar, pois já tem um valor. 
print(dicio)