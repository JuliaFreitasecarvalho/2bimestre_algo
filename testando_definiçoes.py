compras = ["Pão", "Café", "Leite"]
print(compras[0])

compras.remove(compras[2]) #Pode ser removido pelo nome ou pelo indece
print(compras)

compras.append("Açucar") #Append acrescenta um item ao final da lista, podendo adicionar um por vez
print(compras)

compras_ordenadas = sorted(compras) # É preciso criar uma lista nova para receber os elementos ordenados na lista antiga 
print(compras_ordenadas)

for item in compras:
    print("-",item) # Tanto faz o nome que estiver dentro, pois ele é apenas um identificador 



 