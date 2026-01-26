# Collections: namedtupla

from collections import namedtuple

Produto = namedtuple("Produto", ["nome", "marca", "preço"])
novo_produto = Produto("Smartphone", "Samsung", 3999.99)
print(f"Criamos o objeto chamado novo_produto, usando como tipo Produto. Ao exibirmos este objeto temos: \n{novo_produto}")

# Iteração
print("\nComo a namedtuple ainda é uma tuple, podemos iterá-la: ")
for valor in novo_produto:
    print(valor)
    
# Desempacotamento
x, y, z = novo_produto
print(f"\nTambém foi possível desempacotar os valores de novo_produto nas variáveis X = {x}, Y = {y} e Z = {z}")