# Sistema de Ficha Cadastral:

"""
Consiste no uso de "dicionário" e loop "While"
"""

op = 0
ficha = {}

while op != 4:
    print("FICHA CADASTRAL: \n\t1 - Incluir informações na ficha; \n\t2 - Recuperar informações da ficha; \n\t3 - Exibir a ficha completa; \n\t4 - Sair; \n")
    op = int(input("Informe a opção desejada: "))

    if op == 1:
        chave = input("\nEm qual campo deseja inserir seus dados? ")
        valor = input(f"Qual informação você quer adicionar no campo {chave}? ")
        ficha.update({chave:valor})

    elif op == 2:
        print(f"\nOs campos disponíveis na ficha são: {ficha.keys()}")
        chave = input("Você deseja obter dados de qual campo? ")
        if chave in ficha.keys():
            print(f"{chave} → {ficha.get(chave)}")
        else:
            print("O campo informado não existe na ficha cadastral.")

    elif op == 3:
        print("\n---FICHA---")
        for campo, dado in ficha.items():
            print(f"{campo.upper()} → {dado}")
        print("-----------------------------")

    elif op == 4:
        print("Obrigado, saindo do sistema...")
        break