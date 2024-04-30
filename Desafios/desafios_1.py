consumo = float(input("Digite o seu consumo mensal para recomendar o plano ideal para você: "))

def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10 and consumo <=20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

print(recomendar_plano(consumo))