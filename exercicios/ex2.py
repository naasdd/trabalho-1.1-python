numerosPrimos = []
numerosGemeos = []

n = 2

while n < 3000:
    divisor = 2

    while divisor <= n:

        if ((n % divisor == 0) and (divisor != n) and (divisor != 1)):
            # print("O número", n, "é divisivel por",
            #       divisor, "Portanto, não é primo")

            break

        else:
            if (divisor == n):
                # print("O número", n, "é primo")
                numerosPrimos.append(n)

            divisor = divisor + 1

    n = n + 1

i = 0
while i < len(numerosPrimos) - 1:

    if ((numerosPrimos[i + 1] - numerosPrimos[i] == 2) and (numerosPrimos[i] >= 1000)):
        print("Os numeros primos",
              numerosPrimos[i], "e", numerosPrimos[i+1], "sao gemeos")
        numerosGemeos.append(numerosPrimos[i])
        numerosGemeos.append(numerosPrimos[i + 1])
        break

    i = i + 1

print("Fim")