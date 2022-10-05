# python_test
# Lezione 8 - Esempio 3
# Autore: Alessandra Vetri
# Email: vetri@olomedia.it
# Creato il 05/10/2022


# Creare un set con gli elementi dell’ insieme delle note musicali
note = {'DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI'}

# Creare un set con gli elementi dell’ insieme articoli determinativi
articoli_det = {'IL', 'LO', 'LA', 'I', 'GLI', 'LE'}

# Mostrare l’unione dei due set
print( note | articoli_det)

# Mostrare l’ intersezione tra i due set
print( note & articoli_det)

# Mostrare la differenza tra i due set
print('ote - articoli:',  note - articoli_det)
print('articoli-note', articoli_det - note)

# Mostrare la intersezione simmetrica tra i due set
print( note ^ articoli_det)