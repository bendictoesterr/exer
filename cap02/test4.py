# Entendendo o texto (string)

texto = "Este texto tem uma quebra de linha \n aqui. Porém aqui temos uma \t tabulação."
print(texto)

texto2 = "texto em minúsculas AINDA é texto"
print(texto2.capitalize) # Deixa a primeira letra maiúscula
print(texto2.upper())     # Deixa todo o texto maiúsculo
print(texto2.lower())     # Deixa todo o texto minúsculo

print(texto2.startswith("Tex"))  
# Verifica se o texto começa com a string especificada
print(texto2.endswith("o"))  
# Verifica se o texto termina com a string especificada

print(texto2.count("m")) 
# Conta quantas vezes a string especificada aparece no texto

print(texto2.replace("texto", "frase"))
# Substitui a string especificada por outra

text1 = "Texto em maiúsculas"
text2 = "em"
print(text2 in text1)
# Verifica se a string especificada está presente no texto

