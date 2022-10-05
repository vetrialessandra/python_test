#chiedo all'utente di scegliere un numero ra 1 a 100
num = input('Scegli un numero da 1 a 100')
num= int(num)

#indico il numero da indovinare
num_da_indovinare=int(90)

if num>num_da_indovinare:
    print("Hai indicato un numero troppo grande")
elif num<num_da_indovinare:
    print ("Hai indicato un numero troppo piccolo")
elif num==num_da_indovinare:
    print("numero esatto")