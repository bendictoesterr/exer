# Calculadora simples de inteiros:

print("Bem-vindo(a) ao calculador de inteiros :) ")
p_valor = int(input("Coloque o primeiro valor: "))
s_valor = int(input("Coloque o segundo valor: "))

# print(type(p_valor)) → serve para sabermos o tipo da variável.

soma = p_valor + s_valor

print("Resultado da SOMA = " + str(soma))

# print("Resultado da SOMA = {}".format(soma))
# print(f"Resultado da SOMA = {soma}")

subtracao = p_valor - s_valor
print("Resultado da SUBTRAÇÃO = " + str(subtracao))
multiplicacao = p_valor * s_valor
print("Resultado da MULTIPLICAÇÃO = " + str(multiplicacao))
divisao = p_valor / s_valor
print("Resultado da DIVISÃO = " + str(divisao))
divisao_inteira = p_valor // s_valor
print("Resultado da DIVISÃO INTEIRA = " + str(divisao_inteira))


