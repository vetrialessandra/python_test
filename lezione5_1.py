#Creo una lista
lista = ["C","S","R","V"]
# Stampo lista
print(lista)
# stampo il secondo elemento
print('il secondo elemento della lista è: ', lista[1])
# Sostituire il 3 valore della lista
lista[2] = 'AAA'
# Stampare la nuova lista
print('Lista: ', lista)
# Stampare i primi 3 elementi della lista
print('I primi 3 elementi sono: ', lista[:3])
# Rimuovere il 2 elemento della lista
del lista[1]
# Stampo lista
print(lista)
# Contare quante volte un elemento è presente nella lista
ins = input('Inserire elemento da cercare: ')
conta = lista.count(str(ins))
print('L\'elemento ' + str(ins) + ' è presente ' + str(conta) + ' volte')