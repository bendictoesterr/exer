def cal_velocidade_media(distancia: float, tempo: float, unidade_medida = "KM/h"):
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media} {unidade_medida}")

cal_velocidade_media(200, 10)
cal_velocidade_media(200, 10, "m/s")