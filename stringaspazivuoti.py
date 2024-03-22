#data una lista di stringhe, eliminare dalla lista tutte le stringhe vuote
ls = ["uno", "", "due", "tre", "", "", "fine"]
ls_filtrata = []

for i in ls:
    if i != "":
        ls_filtrata.append(i)

print(ls_filtrata)

s = ["uno", "", "due", "tre", "", "", "fine"]
ls_filtrata = []

for i in ls:
    if len(i)>0:
        ls_filtrata.append(i)

print(ls_filtrata)

ls = ["uno", "", "due", "tre", "", "", "fine"]

def non_vuota(elemento):
    return elemento != ""

ls_filtrata = list(filter(non_vuota, ls))

print(ls_filtrata)

#contare quanti caratteri ci sono in alice.txt
#contare quanti caratteri non sono spazi bianchi
#contare quanti caratteri alfanmerici ci sono
file = open("alice.txt", "r")
testo = file.read()
caratteri_totali=0
caratteri_non_spazi_bianchi =0
caratteri_alfanumerici=0
caratteri_alfanumericii=0

for caratteri in testo:
        caratteri_totali+= 1

print("caratteri totali", caratteri_totali)

#contare quanti caratteri non sono spazi bianchi
for caratteri in testo:
     if  caratteri != " ":
        caratteri_non_spazi_bianchi += 1

print("Numero di caratteri che non sono spazi bianchi:", caratteri_non_spazi_bianchi)

#contare quanti caratteri alfanmerici ci sono
for carattere in testo:
    if carattere.isalnum():
        caratteri_alfanumerici += 1
print("Numero di caratteri alfanumerici nel testo:", caratteri_alfanumerici)

for carattere in testo:
    if carattere in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
        caratteri_alfanumericii += 1
print ("numero di caratteri alfanumerici:", caratteri_alfanumericii)

