# JSON:
# → Importando JSON:
import json

# Dicionário:
dicio = {
    "nome":"Python",
    "missão":"Ser incrível"
}

# Utilizando a função DUMPS para converter o dicionário, resultando em uma string com estrutura do JSON:
texto = json.dumps(dicio, indent = 4, ensure_ascii = False)
print(f"O dicionário foi convertido para string, e seu comando é: {texto}")

# Gravando em um arquivo: (Json → é um texto)
with open("arquivo.json", "w", encoding = "utf-8") as arquivo:
    arquivo.write(texto)
    print("O texto está no formato JSON e foi salvo dentro do arquivo")
