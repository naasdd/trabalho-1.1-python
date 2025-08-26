print("Programa lê uma frase e identifica se a mesma é um palíndromo ou não")

frase = input("Digite uma frase: ")
fraseNormal = []
fraseInversa = []


for n in frase: # aqui ele cria um array da frase invertida
    if(n != ' '):
        fraseInversa.insert(0, n)
        fraseNormal.append(n)


i = 0

while i < len(fraseNormal): # aqui ele verifica letra por letra
    if(fraseNormal[i] != fraseInversa[i]):
        palindromo = False
        break
    else:
        palindromo = True
    i += 1

if(palindromo):
    print("A frase: ", frase,", é um plaíndromo")

else:
    print("A frase: ", frase,",não é um plaíndromo")