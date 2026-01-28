# importando o módulo JSON:
import json

# Lendo o conteúdo do arquivo como um texto normal:
with open("arquivo.json", "r", encoding = "utf-8") as arquivo:
    conteudo = arquivo.read()
    
# Colocando a string na função LOADS para que o Python interprete e gere a estrutura adequada:
dicio = json.loads(conteudo)
print(f"O conteúdo do arquivo foi carregado e convertido: {dicio}")
