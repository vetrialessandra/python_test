#creo una lista di voti
voti=[10,8,6,7,9]
#dichiaro il voto più alto possibile in modo da cerce un numero inferiore
min=100
for num in voti:
    if num < min:
        min = num
print("Il voto piu' piccolo della lista è " + str(min) )

#metodo 2 - senza considerare un valore max di paragone
num_precedente=0
for num in voti:
    if num < min:
        min = num
    num_precedente=num
print("Il voto piu' piccolo della lista è " + str(min) )
