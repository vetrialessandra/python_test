#chiedo all'utente di inserire un numero
num = input('Inserisci un numero intero da 1 a 10')
num= int(num)
if num>=1 and num<=10:
    print('La tabellina è: ')
    i=1
    while i<=10 :
        #stampo la tabellina
        print(str(num * (i)))
        i +=1
else:
    print('Hai inserito un numero superiore a 10')