# Conectivos lógicos:

"""
AND → Verdadeiro quando ambas as condições são verdadeiras.
OR → Falso quando ambas são falsas.
NOT → Negação.
"""

user = input("Digite seu login (usuário): ")
senha = input("Digite sua senha: ")

if user.upper() == "ADMIN" and senha == "123":
    print("Acesso permitido")
else:
    print("Acesso negado")