import time

#Variaveis globais
ligado= False
tempo= 0
potencia= 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True 
        tempo = novo_tempo 
        potencia = nova_potencia
        print(f"Microondas ligado por {tempo} segundos na potencia {potencia}")
        iniciar_cronometro(tempo)
        desligar() #desligar automaticamente 
    else:
        print("Microondas já está ligado")

def desligar():
    global ligado
    if ligado:
        ligado = False 
        print("Microondas está deslgado")
    else:
        print("MIcroondas já está desligado")

def status():
    if ligado:
        print(f"Tempo:{tempo} segundos \n potencias: {potencia}")
    else:
        print(f"Desligado")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"Tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -=1 #segundos = segundos -1
        if segundos <= 0:
            print("\nTempo esgotado")

#definiçôes do Microondas

def pipoca():
    ligar(30,100)

#rodar função
pipoca()