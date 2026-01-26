def cal_velocidade_media(distancia, tempo):
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media}")

# Solicitar distância e tempo:
dist_digitada = float(input("Digite a distância pecorrida: "))
tempo_digitado = float(input("Digite o tempo: "))
cal_velocidade_media(dist_digitada, tempo_digitado)
