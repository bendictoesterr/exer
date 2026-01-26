# Função para calcular a velocidade média:
def calc_velocidade_media(distancia: float, tempo: float, unidade_medida = "km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f"{velocidade_media:.2f} {unidade_medida}"

# Função para converter a temperatura:
def converter_temperatura(temperatura:float, unidade_medida = "celsius"):
    if unidade_medida == "celsius":
        return f"{(temperatura * 1.8 + 32):.2f} fahrenheit"
    elif unidade_medida == "fahrenheit":
        return f"{((temperatura - 32) / 1.8):.2f} celsius"
    else:
        return 0
           
# Função para exibir menu:
def menu():
    print("\t----MENU---- \n\t1 - Calcula a velocidade média. \n\t2 - Converter a temperatura. \n\t3 - Sair.")
    
def aluno_de_fisica():
    op = 0
    while op != 3:
        menu()
        op = int(input("Informe a opção desejada: "))
        if op == 1:
            distancia_percorrida = float(input("Informe a distância: "))
            tempo_viagem = float(input("Informe o tempo da viagem: "))
            medida = input("Informe a unidade de medida: ")
            print(f"A velocidade média é {calc_velocidade_media(distancia_percorrida, tempo_viagem, medida)}")
        elif op == 2:
            temperatura_informada = float(input("Informe a temperatura que deseja converter: "))
            medida = input("A temperatura informada está em celsius ou fahrenheit? ")
            print(f"O resultado da conversão é {converter_temperatura(temperatura_informada, medida)}")
        elif op == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

aluno_de_fisica()