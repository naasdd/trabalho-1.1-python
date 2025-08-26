valor = int(input("Insira um numero: "))

fibonacci = [0, 1]

print("   ")

i = 2
while True:
    novoValor = (fibonacci[i - 1] + fibonacci[i - 2])
    fibonacci.append(novoValor)
    if (novoValor > valor):
        menor = fibonacci[i] - valor
        maior = valor - fibonacci[i - 1]

        if (maior > menor):
            resposta = fibonacci[i]
            print("resposta = fibonacci[i] = ", fibonacci[i])
        else:
            resposta = fibonacci[i - 1]
            print("resposta = fibonacci[i - 1] = ", fibonacci[i - 1])

        break
    else:
        i = i + 1

print(fibonacci)

print("O valor da sequência de fibonacci mais próximo de", valor, "é: ", resposta)
