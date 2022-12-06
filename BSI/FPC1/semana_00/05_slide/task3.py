# Entrar com um distância (km) e o tempo de viagem (horas) de um automóvel, e dizer se a velocidade média foi superior ao limite (110 km/h) ou não.

def verificar(dist, temp):
    acima_limite = False
    if dist/temp > 110:
        acima_limite = True
    return acima_limite
