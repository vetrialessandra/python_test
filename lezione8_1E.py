# python_test
# Lezione 8 - Esercizio 1
# Indovina il numero misterioso
# Autore: Alessandra Vetri
# Email: vetri@olomedia.it
# Creato il 05/10/2022

#importo librerie random

from random import randrange
#Far scegliere all’utente la lingua (IT on ENG)

scelta_lingua = int(input('Scegli la lingua IT (1) - ENG (2): '))

#inizializzo vittorie e perdite
conta_v=0
conta_p=0
while conta_v < 10:
    #genera numero misterioso
    numero_misterioso = randrange(1, 11)
    #Chiedere all’utente se il numero misterioso è <= a 5 o >5
    if scelta_lingua == 1:
        numero_scelto = int(input('Se pensi che il numero misterioso sia minore uguale a 5 digita 1 se maggiore di 5 digita 2 '))
    else:
        numero_scelto = int(input('If you think the mysterious number is less than 5 type 1 if greater than 5 type 2 '))
    #Comunicare all’utente il risultato.
    if (numero_scelto == 1 and numero_misterioso <= 5) or (numero_scelto == 2 and numero_misterioso > 5):
        conta_v += 1
        if scelta_lingua == 1:
            print('Hai indovinato')
        else:
            print('you guessed it ')
    else:
        conta_p += 1
        if scelta_lingua == 1:
            print('Non hai indovinato')
        else:
            print('you didn\'t guess')
    #Tenere conto dei risultati; l’utente vince se indovina 10 volte prima di sbagliare 10 volte
    if conta_p >= 10:
        if scelta_lingua == 1:
            print('Hai sbagliato 10 volte. Hai perso.')
        else:
            print('you lose')
    elif conta_v >= 10:
        if scelta_lingua == 1:
            print('Hai indovinato 10 volte')
        else:
            print('you guessed it')




