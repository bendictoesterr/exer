def cal_velocidade_media():
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media}")

# Solicitar distancia e tempo:
distancia = float(input("Digite a distância pecorrida: "))
tempo = float(input("Digite o tempo: "))
cal_velocidade_media()