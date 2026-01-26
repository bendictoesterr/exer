# Velocidade média = distância / tempo

print("Simulador de computador de bordo.")

dist = float(input("Digite a distância (km): "))
temp = float(input ("Digite o tempo (h): "))

vel_media = dist / temp

# print("A velocidade média é de {} km/h".format(vel_media))
print(f"A velocidade média é de {vel_media} km/h")

# Para arredondar os valores na exibição:
# print("A velocidade média é de {:.2f} km/h".format(vel_media))
# print(f"A velocidade média é de {vel_media:.2f} km/h")