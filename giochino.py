import random


def gioco():
    giocatore1 = 0
    giocatore2 = 0
    round = 0

    while giocatore1 < 10 and giocatore2 < 10 and round < 16:
        scelta_random = random.randint(1,100)
        scelta_utente = str(input('Will the next number be odd or even? : '))


        if (scelta_utente=='even') == scelta_random%2==0:
            print(f' The PC choose {scelta_random} you choose {scelta_utente},\n You WON!!')
            giocatore1 += 1
        else:
            print(f' the PC choose {scelta_random} you choose {scelta_utente},\n You LOSE!!')
            giocatore2 += 1

            
        round += 1
        print(f"Score: \n Player : {giocatore1}  \n Machine : {giocatore2}")
        if round == 15:
            print('last cast!!!!')
    
    if giocatore1 > giocatore2:
        print("You Won!!")
    elif giocatore2 > giocatore1:
        print("You lose, Machine Won!!")
    else:
        print("Draw Match....try Again")

gioco()
