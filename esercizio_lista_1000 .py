#Costruire due liste, la prima che contiene i numeri pari fino a 1000 
#la seconda che contiene i numeri dispari fino a 1000
#a partire dalle prime due liste,
#costruire una terza lista che contiene prima tutti i pari e poi tutti i dispari
 
pari = []
dispari = []

for num in range (0,1000):
    if num % 2==0:
        pari.append(num)
    else:
        dispari.append(num)
                
lista_finale = pari + dispari
print(lista_finale) 