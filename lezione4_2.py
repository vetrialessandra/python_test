name = input("Come ti chiami? ")
password="Password_sicura"
pass_utente=input(name +" inserisci la password ")

if pass_utente==password:
    print ("Benvenuto " + name)
else:
    print ("password non corretta")
