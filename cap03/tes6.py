# Laços de repetição: for

"""
for x in [dentro de...] range(limite inicial, limite final, pulos)

for contadora in range(10, 100, 2):
    print(contadora)
    
"""
    
# Na maioria, o limite superior é exclusivo. Se escolher 100, irá até 99...

# break → serve para PARAR a condição do loop

num = int(input("Informe o número do qual deseja o fatorial: "))
fat = num

for val in range(1, num, 1):
    fat = fat * val
    
print(f"O fatorial de {num} é igual a {fat}")
