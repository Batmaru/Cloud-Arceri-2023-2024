# problema: ho la stringa "123", la voglio trasformare in [1,2,3]
#definire una funzione che risolva il  problema

#def stringa_in_lista(stringa):
 #   lista = []
  #  for carattere in stringa:
   #     lista.append(int(carattere))
    #return lista

#stringa = "123"
#lista = stringa_in_lista(stringa)
#print(lista)  

fin = open("alice.txt", "r")
linee = fin.readlines()
fin.close()

# Rimuovi i caratteri di fine riga
l1 = []
for l in linee:
    l1.append(l.strip())

# Aggiorna la variabile linee
linee = l1

# Stampa le righe senza i caratteri di fine riga
print(linee)

# Dividi la stringa s usando il punto e virgola come separatore
s = "alfa; beta; gamma"
print(s.split(";"))  # Stampa ["alfa", " beta", " gamma"]

# Stampa tutte le parole che compongono alice.txt
for linea in linee:
        print(linea.split())




    