
import os   
clear = lambda:os.system('clear')
from datetime import datetime



now = datetime.now()

def funcao_jogo_forca():

    

    print("\n\n")
    print("********************************")
    print("   Bem vindo ao jogo da forca  ")
    print("********************************")

    palavra_secreta = "banana"

    
    enforcou=False
    acertou=False
    aux1 = 0    
    x= len(palavra_secreta)
    cont = x   
    
    lista = []
 
    print (lista)

    while(aux1 < x):
        lista[aux1]= 15
        aux1= aux1 +1   

    print (lista)    
    
    print(" Tamanho da palavra {}".format(x))

    while(not enforcou and  not acertou):

        chute = input (" Digite uma letra :") 
        if (chute not in palavra_secreta):
            print("Letra {} nao pertence a palavra, você tem mais {} de chances .".format(chute,cont-1))
            cont= cont-1
            if (cont <= 0):
                print("Você perdeu numero maximo de erros")
                break

        elif (chute in palavra_secreta):
            i=0
            pre=0            
            
            for letra in palavra_secreta :
                if (chute == letra):
                    print(" A letra {} foi encontrada nas posicoes {}" .format(chute,i))
                    pre=i                    
                    lista.insert(pre,chute)               
                
                i = i +1
            print ("jogando") 
            
            print(lista)      
    print("Fim de jogo")

if (__name__ == "__main__"):
    funcao_jogo_forca()