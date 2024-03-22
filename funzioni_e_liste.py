
# sia data una lista <ls> contenente N digit da 1 a N
# non necessariamente tutti presenti quindi con
# eventuali ripetizioni
# [1, 2, 3, 4, 5, 6, 7, 8]
# N=8
# [1,1,2,2,3,5,8,8]

# N=5
# [1,3,5,1,5]

# sia data una seconda lista, costruita esattamente
# come la precedente, ovviamente con valori diversi,
# ma sempre nel rispetto del valore N

# N=6
# ls=[1,1,2,2,5,6]
# lsCheck=[2,3,3,6,6,4]

# Scrivere una funzione alla quale passerete 
# come parametri ls e lsCheck e la funzione deve riportare 
# due valori 
# il primo: tutte le volte che c'è lo stesso digit 
# nella stessa posizione di ls e lsCheck
# nel nostro esempio il primo valore tornato dalla funzione sarà 1
# adesso per completare il calcolo tolgo dalle 2 liste i valori che stanno nella stessa posizione


# il secondo: tutte le volte in cui un elemento della lista lsCheck
# è presente nella lista ls
# ma non nelle stessa posizione
# nel nostro esempio la funzione torna:
# c'è il 2 nella nella ls?
# sì, lo tolgo

# ls=[1,2,5]
# lsCheck=[2,3,6,6,4]


# ls=[1,4,1]
# lsCheck=[5,5,5,3,6]
# uguali=2
# diversi=2

# ls=[6,6,5]
# lsCheck=[3,4,4,1,4]
# uguali=3
# diversi=2


# Genera una lista che contiene N numeri casuali tra 1 e N

import random

def GeneraLista(N):
    numeri_casuali = []
    
    for i in range(N):
        numero_casuale = random.randint(1, N)
        numeri_casuali.append(numero_casuale)
    
    return numeri_casuali


N = int(input("Inserisci il valore di N: "))


lista1 = GeneraLista(N)
lista2 = GeneraLista(N)

# Stampiamo la lista generata
print("Lista di numeri casuali:", lista1)
print("Lista di numeri casuali:", lista2)

# Funzione che confronta due liste e conta gli elementi 
# uguali nella stessa posizione
# Funzione che confronta due liste e conta gli elementi uguali nella stessa posizioneimport random

# Funzione che genera una lista contenente N numeri casuali tra 1 e N
def GeneraLista(N):
    numeri_casuali = [random.randint(1, N) for _ in range(N)]
    return numeri_casuali

# Funzione che confronta due liste e conta gli elementi uguali nella stessa posizione
def contauguali(lista1, lista2):
    contatore = 0
    nuova_lista1 = []
    nuova_lista2 = []
    
    for i in range(min(len(lista1), len(lista2))):
        if lista1[i] == lista2[i]:
            contatore += 1
        else:
            nuova_lista1.append(lista1[i])
            nuova_lista2.append(lista2[i])

    return contatore, nuova_lista1, nuova_lista2




numero_elementi_uguali, nuova_lista1, nuova_lista2 = contauguali(lista1, lista2)

# Stampiamo il numero di elementi uguali e le nuove liste
print("Numero di elementi uguali nella stessa posizione:", numero_elementi_uguali)
print("Nuova lista 1:", nuova_lista1)
print("Nuova lista 2:", nuova_lista2)


