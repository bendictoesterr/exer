# Projeto: Cadastro de doação de sangue

print("Bem-vindo ao sistema de cadastro de doação de sangue!")
#nome
nome = input("Digite seu nome completo: ")

#peso
peso = float(input("Digite seu peso (kg): "))

#altura
altura = float(input("Digite sua altura (cm): "))

#idade
idade = int(input("Digite sua idade: "))

# tem peso mínimo p doar 
peso_minimo = peso >= 50

# tem idade mínima p doar
idade_minima = idade >= 16

text_saida = f"\tNOME: {nome.upper()},\n\tPESO: {peso} kg\n\tALTURA: {altura} cm\n\tIDADE: {idade} anos\n\tTEM PESO MÍNIMO PARA DOAR SANGUE: {peso_minimo}\n\tTEM IDADE MÍNIMA PARA DOAR SANGUE: {idade_minima}\n\t"

print(text_saida)