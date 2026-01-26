def soma(a,b):
    resultado = a + b
    return resultado
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

resposta = soma(valor1, valor2)

print(f"A variável resposta recebeu o return da função soma() e agora contém: {resposta}")
print(f"A função está sendo chamada para os valores {valor1} e {valor2} e retornou: {soma(valor1, valor2)}")