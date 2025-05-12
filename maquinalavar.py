import time

ligado = False
tempo = 0
temperatura = 0

def ligar(novo_tempo, novo_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True
        tempo = novo_tempo
        temperatura = novo_temperatura
        print(f"Lavando por {tempo} segundos na temperatura: {temperatura}°C")
        iniciar_lavar(tempo)
        desligar()
    else:
        print("A maquina já está ligada")

def desligar():
    global ligado
    if ligado:
        ligado = False
        print("A maquina está desligada")
    else:
        print("A maquina já está desligada")

def status():
    if ligado:
        print(f"Tempo:{tempo} segundos \n Temperatura: {temperatura} °C")
    else:
        print(f"Desligado")

def iniciar_lavar(segundos):
    while segundos>0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -=1 #segundos = segundos -1
        if segundos <= 0:
            print("\nTempo esgotado")

def vidro():
    ligar(120,100)

def plastico():
    ligar(60,21)

def metal():
    ligar(120,30)

print("Funções \n 1 - Vidro \n 2 - Plástico \n 3 - Metal")
escolha = int(input("Escolha qual função lavar a louça: \n"))
match escolha:
    case 1:
        vidro()
    case 2:
        plastico()
    case 3:
        metal()