compras = []
resposta = ""
while resposta!= "não":
    
    resposta = input("Deseja colocar algo na lista de compras")

    if resposta == "sim":
        coloca = input("Insira item") 
        compras.append(coloca)
        print(compras)

    eliminar = input("Deseja eliminar item?")

    if eliminar == "sim":
        retira = input("Insira item para retirar")
        compras.remove(retira)
        print(compras)