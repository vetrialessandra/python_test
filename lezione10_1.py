# python_test
# Lezione 10 - Esempio 1
# classi
# Autore: Alessandra Vetri
# Email: vetri@olomedia.it
# Creato il 06/10/2022

#Creare una classe Cane con attributi: nome, razza, eta e creare metodi per delle funzionalita di base, come ad esempio mangia e abbaia, fai i bisogni ("Gnam Gnam", "Bau Bau" ."pupù e pipi"

#classe
class cane:
    def __init__(self, nome, razza, eta):
        self.nome=nome
        self.razza=razza
        self.eta=eta

#metodi
    @classmethod
    def abbaia(cls):
        print ("abbaia")

    @classmethod
    def mangia(cls):
        print ("gnam gnam")

    @classmethod
    def beve(cls):
        print("slurp")


cane.abbaia()
cane.beve()
cane.mangia()