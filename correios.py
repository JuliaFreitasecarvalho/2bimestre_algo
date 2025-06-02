pacotes = ("abc123", "xyz789", "def456", "jkl321", "mno657", "pqr987", "stu741") 
rastreio = ("enviado", "recebido", "em transito", "enviado", "recebido", "em transito", "enviado" ) 

#Quantos pacotes estão emcada status:
print("Numeros de pacotes enviados:", rastreio.count("enviado"))
print("Numeros de pacotes em transito:", rastreio.count("em transito"))
print("Numeros de pacotes recebido:", rastreio.count("recebido"))

#Liste apenas os códigos dos pacotes com status "Em transito":

print("Indices dos pacotes em transito", pacotes[2], pacotes[5])

# Use uma função que recebe um código de rastreamento e retorne o status do pacote, ou uma mensagem informando que o pacote não está cadastrado

codigo = input("Insira codigo para rastreio")
print("seu pacote está no indice", pacotes.index(codigo), "status:", rastreio[pacotes.index(codigo)])

# Ordene os pacotes pelo código da rastreamento e exiba a tupla ordenada
ordena = sorted(pacotes)
print("Pacotes ordenados:", ordena)