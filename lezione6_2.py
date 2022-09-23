import os
i=0

for i in range(10): #uso il ciclo for per ripetere 10 volte il ping (-c non funziona)
    os.system('ping google.com')