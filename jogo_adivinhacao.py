import random
from datetime import datetime

now = datetime.now()

import os   
clear = lambda:os.system('clear')
def funcao_jogo_adivinhacao():
    clear ()
    
    print("     {}/{}/{}      {}:{} ".format(now.day,now.month,now.year,now.hour,now.minute))
    print("\n")
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1,101))
    numero_tentaticas = 0 
    vez=1
    pontos = 1000

    
    print(" (1) - FÁCIL ")
    print(" (2) - MÉDIO ")
    print(" (3) - DIFÍCIL ")
    
    facil = "FACIL"
    medio = "MÉDIO  "
    dificil = "DIFÍCIL"

    escolha_nivel = int(input("Escolha o nivel  : "))

    if (escolha_nivel == 1):
        numero_tentaticas = 10
        print ("Você escolheu nivel {} ,  tem {} tentativas, Boa sorte !".format(facil,numero_tentaticas))
    elif (escolha_nivel == 2):
        numero_tentaticas = 6
        print ("Você escolheu nivel {} ,  tem {} tentativas, Boa sorte !".format(medio,numero_tentaticas))
    else:
        numero_tentaticas = 3
        print ("Você escolheu nivel {} ,  tem {} tentativas, Boa sorte !".format(dificil,numero_tentaticas)) 

    for vez in range (1 , numero_tentaticas+1) :
        print("Tentativa {} de {} ".format( vez , numero_tentaticas))
        chute_str = input("Digite seu numero de 1 a 100 :")
        print("Você digitou :" ,chute_str)
        chute = int(chute_str)

        if ( chute < 1 or chute > 101):
            print(" Você perdeu uma rodada numero inválido ")
            print("-----------------------------------------------------------------")
            continue     

        acertou     = numero_secreto == chute 
        errou_maior = numero_secreto < chute 
        errou_menor = numero_secreto > chute 

        if(acertou):
            print("Voçê acertou")
            print("-----------------------------------------------------------------")
            break
        else :
            if(errou_maior):
                print("Voçê errou! Seu chute foi MAIOR que o numero secreto ")
            if(errou_menor):
                print("Voçê errou! Seu chute foi MENOR que o numero secreto ")

            pontos_perdidos = abs (numero_secreto - chute)
            pontos = pontos - pontos_perdidos            
    
        print("-----------------------------------------------------------------")
    print("Sua pontuação foi",pontos)
    
if(__name__ == "__main__"):
    
    funcao_jogo_adivinhacao()


