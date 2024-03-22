#sapendo che la funzione random.randint(start, end)genera un numero intero compreso tra start e end, 
#end compreso,costruire una lista di numeri casuali lunga 100 e stampare la somma di tutti i suoi numeri
import random

# creare una lista vuota per contenere i numeri casuali
numeri_casuali = []

# generare 100 numeri casuali e aggiungerli alla lista
for i in range(100):
    numeri_casuali.append(random.randint(1, 10))
print (numeri_casuali)

# calcolare la somma di tutti i numeri casuali
somma = sum(numeri_casuali)

# stampare la somma
print(somma)