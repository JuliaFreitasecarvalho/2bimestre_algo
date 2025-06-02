#Para ser um Tupla precisa estar entre parenteses ()
numero = (5, 8, 12, 8, 7, 8, 3)
print("Tupla original:", numero) # Mostrando para o usuario a tupla original, sem manipulações.
print("Tamanho da tupla:",len(numero))
print(numero[2])#Escolhendo elemento atraves do indice, lembrando que começa do 0
print("Fazendo uma Slicing do 2 ao 5", numero[2:5]) #O slicing não pega o ultimo item definido no recorte
print("Quantas vezes o numero 8 repete:", numero.count(8))#Count mostra quantas vezes um elemneto repete
print("posição da primeira ocorrencia do numero 7:", numero.index(7))#Index mostra qual será a posição do elemento

minimo_tuplas = min(numero)
print("O menor numero dentro da tupla:",minimo_tuplas)

maximo_tuplas = max(numero)
print("O mairo numero dentro da tupla:",maximo_tuplas)

soma_tuplas = sum(numero)
print("A soma de todos é:", soma_tuplas)

ordem_tuplas = sorted(numero)
print("A ordem a tupla é:", ordem_tuplas)

print("O NUMERO 4 ESTÀ NA TUPLA???????????????AAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 4 in numero)

numero2 = (15,20)
tupla_concatenada = numero+numero2 #Junta das duas tuplas
print("A concatenação da tupla 1 e 2 resulta na nova tupla:", tupla_concatenada)

duplicar = numero*2
print(duplicar)