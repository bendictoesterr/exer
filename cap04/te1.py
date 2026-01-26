# Programa de CALORIAS:

cal = []
resp = ""

while resp.upper() != "N":
    caloria = int(input("Quantas calorias você consumiu nessa refeição? "))
    cal.append(caloria)
    resp = input("Você deseja informar as calorias de mais uma refeição? (s/n) ")

total = 0

print("As calorias informadas para este dia foram: ")
for caloria in cal:
    total = total + caloria
    print(caloria)

media = total / len(cal)
print(f"Ao longo do dia foram consumidas {total} calorias, com uma média de {media:.2f} calorias por refeição.")
