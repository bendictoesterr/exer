# Restaurante Self-Service à Kilo

print("Bem-vindo ao Restaurante Self-Service à Kilo!")

preco_quilo = float(input("Digite o preço por quilo da refeição: R$ "))

peso_prato = float(input("Digite o peso do prato em quilos: "))

preco = preco_quilo * peso_prato
print(f"O preço total a pagar é: R$ {preco:.2f}")

if peso_prato > 1.0:
    print("Você excedeu 1kg, pode comer à vontade pagando o valor fixo de R$ 80,00.")
    
    