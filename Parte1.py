def JogoAdvinha():
    import random
    numAleatorio = random.randint(1, 100)
    tentativas = 3
    print("Você tem 3 tentativas!")
    while(tentativas > 0):
        print("---TENTATIVAS RESTANTES--->", tentativas)
        tentativas = tentativas - 1
        palpite = eval(input("Digite o seu palpite: "))
        if(palpite > numAleatorio):
            print("O seu palpite é maior do que o número sorteado!")
        elif(palpite < numAleatorio):
            print("O seu palpite é menor do que o número sorteado!")
        else:
            print("Parabéns! Você acertou!")
            Menu()
        if (tentativas == 0):
            print("Suas chances acabaram! :(")
            print("o número sorteado foi:", numAleatorio)
            Menu()

def Menu():
    perg = eval(input("Digite 1 para jogar novamente e 2 para sair do jogo: "))
    if(perg == 1):
        JogoAdvinha()
    else:
        print("Obrigado por jogar!")
        exit()

JogoAdvinha()