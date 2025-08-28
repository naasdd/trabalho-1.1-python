mensagem = input("Insira sua mensagem a ser criptografada: ")
chave = int(input("Insira um numero de criptografia: "))

alfabeto = "abcdefghijklmnopqrstuvwxyz"
mensagemCriptografada = ""

for c in mensagem:
    if c in alfabeto:
        posicao = alfabeto.index(c)          
        novaPosicao = (posicao + chave) % 26 
        mensagemCriptografada += alfabeto[novaPosicao]
    else:
        mensagemCriptografada += c      

print("Mensagem criptografada:", mensagemCriptografada)
