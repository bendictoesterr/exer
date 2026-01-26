# Mega Saldão (desconto)

"""
Opções de pagto: 
1 - Boleto Bancário (5% de desconto)
2 - Cartão de Crédito (parcela até 12x).
"""

print("Bem-vindo ao Mega Saldão!")

total = float(input("Digite o valor total das compras: R$ "))
forma_pagto = int(input("Escolha a forma de pagamento (1 - Boleto, 2 - Cartão): "))

if forma_pagto == 1:
    desconto = total * 0.05
    print(f"Valor com desconto de 5%: R$ {total - desconto:.2f}")
else:
    parcela = int(input("Digite em quantas parcelas você deseja pagar (até 12x s/juros): "))
    valor_parc = total/parcela
    print(f"Valor da parcela: R$ {valor_parc:.2f} em {parcela}x")