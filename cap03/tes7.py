# Projeto - Capítulo 03:

opc = 0

while opc != 3:
    print ("\n\t1 - Receber um elogio. \n\t2 - Calcular o fatorial de um número. \n\t3 - Sair. \n") 
    opc = int(input("Escolha a opção do menu: "))
    
    if opc == 1:
        print("Não desanime, você consegue!")
        
    elif opc == 2:
            num = int(input("Informe o número do qual deseja o fatorial: "))
            fat = num

            for val in range(1, num, 1):
                fat = fat * val
            print(f"O fatorial de {num} é igual a {fat}")
                 
    elif opc == 3:
        print("Saindo...")
        break
    
    else:
        print("Você não selecionou nenhuma opção válida. \n\t TENTE NOVAMENTE")