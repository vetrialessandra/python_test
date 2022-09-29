#creo dizionario dei sinonimi
dizionario_sinonimi={'antico':'obsoleto','stanco':'pigro','vivace':'arzillo','sveglio':'vigile'}

#ordino perle chiavi
dizionario_chiavi = sorted(dizionario_sinonimi.items())

print(dizionario_chiavi)

#ordina in base al valore
dizionario_ordinato={}
dizionario_valore = sorted(dizionario_sinonimi.items(), key = lambda x: x[1])

# scorro la lista
for chiave,valore in dizionario_valore:
    dizionario_ordinato[chiave] = valore
# mostro il contenuto del nuovo dizionario
print(dizionario_ordinato)

#verifico se stanco è presente nel dizionario
print('stanco' in dizionario_sinonimi)
print('ricco' in dizionario_sinonimi)

# estraggo chiavi e valori
chiavi = list(dizionario_sinonimi.keys())
valori = list(dizionario_sinonimi.values())
print(chiavi)
print(valori)

#cambio chiave
#dizionario_sinonimi['antico'] = dizionario_sinonimi.pop('sveglio')
#print(dizionario_sinonimi)

#modificare una valore
dizionario_sinonimi['vivace'] = 'allegro'
print(dizionario_sinonimi)

#aggiunge coppi achiave valore
dizionario_sinonimi['sciocco'] = 'stolto'
print(dizionario_sinonimi)

#eliminare una chiave
dizionario_sinonimi.pop('sciocco')
print(dizionario_sinonimi)

#aggiunge chiave con 2 valori
dizionario_sinonimi['intelligente'] = ['arguto','abile']
print(dizionario_sinonimi)
#eliminare un valore
dizionario_sinonimi['intelligente'].remove('abile')
print(dizionario_sinonimi)