def exibe_ficha(**dados):
    print(dados)
    print("----FICHA----")
    for chave, valor in dados.items():
        print(f"{chave.upper()} -- {valor}")
ficha_cliente = {
    "nome":"Ester Bendicto",
    "estado civil":"solteira",
    "idade":"20",
    "filhos": False
}
exibe_ficha(**ficha_cliente)
