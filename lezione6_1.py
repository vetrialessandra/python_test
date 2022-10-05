lista=[1,2,3]
tupla=[4,5,6,7,8]

#conto i caratteri della lista
print (len(lista))
#contro i caratteri della tupla
print (len(tupla))

#utilizzando il ciclo
length = 0
for cont_tupla in tupla:
    length += 1
print (length)

#Convertire una lista in una tupla
conv_tupla=tuple(lista)
print (conv_tupla)

#Convertire una tupla in una lista
conv_lista=list(tupla)
#modifico la lista
conv_lista[0]=8
print (conv_lista)
