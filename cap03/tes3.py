# Companhia Aérea: Tipos de Clientes

"""
Limites de bagagem despachada:
1 - Clientes Premium → Até 32kg
2 - Clientes Gold → Até 28kg
3 - Clientes Regular → Pagam pela bagagem
"""

tipo_cliente = int(input("Olá, digite o tipo de cliente: \n\t1 - PREMIUM \n\t2 - GOLD \n\t3 - REGULAR "))
peso_bag = float(input("Digite peso da bagagem a ser despachada (kg): "))

msg = f"Cliente {tipo_cliente}, bagagem dentro do limite permitido, boa viagem :)"

if tipo_cliente == 1:
    if peso_bag <= 32:
        print(msg)
    else:
        excede = peso_bag - 32
        print(f"Os clientes {tipo_cliente} têm direto a despacharem até 32kg. Dirija-se ao balcão para realizar pagamento do excendente.")
elif tipo_cliente == 2: # Equivale a "se não se", age como else quando a consição if anterior é falsa, ou um novo if.
    if peso_bag <= 28:
        print(msg)
    else:
        excede = peso_bag - 28
        print(f"Os clientes {tipo_cliente} têm direto a despacharem até 28kg. Dirija-se ao balcão para realizar pagamento do excendente.")
else:
        print(f"Os clientes {tipo_cliente} não têm direto à bagagem gratuita. Dirija-se ao balcão para realizar pagamento da bagagem.")