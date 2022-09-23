import random

#chiedo all'utente quanti giocatori sono
scelta = input("quanti giocatori? 1 o 2? ")
scelta=int(scelta)

# c = carta - f= forbice - p= pietra
elenco = {0:'carta',1:'forbice',2:'pietra'}
giocA=int(input("Giocatore A scegli 0 per carta, 1 per forbice, 2 per pietra"))
#se viene scelto 1 sarà un giocatore e il computer
if (scelta ==1):
    giocB = random.randint(0, 2)
   # identifico giocatore A l'utente e giocatore B il pc
else:
    giocB = int(input("Giocatore B scegli 0 per carta, 1 per forbice, 2 per pietra"))

print("il giocatore A ha scelto ", elenco.get(giocA))
print ("il giocatore B ha scelto ",elenco.get(giocB))
#se viene scelto lo stesso valore
if giocA==giocB:
    print ("avete scelto entrambi",elenco.get(giocA))
elif giocB==0 : #se giocatore B sceglie carte vedo tutte le possibili combinazioni del giocatore A
    if giocA==1:
        print("complimenti giocatore A hai visto")
    elif giocA==2:
        print("Ha vinto il giocatore B")
elif giocB==1: #se giocatore B sceglie forbice vedo tutte le possibili combinazioni del giocatore A
    if giocA==0:
        print("ha vinto il giocatore B")
    elif giocA==2:
        print("Ha vinto il giocatore A")
elif giocB==2: #se giocatore B sceglie pietra vedo tutte le possibili combinazioni del giocatore A
    if giocA==0:
        print("ha vinto il giocatore A")
    elif giocA==1:
        print("Ha vinto il giocatore B")

