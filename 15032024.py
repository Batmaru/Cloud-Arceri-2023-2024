# Apri il file in modalità lettura
file = open("persone.txt", "r")
lines = file.readlines()  # Leggi tutte le righe del file e memorizzale in una lista
file.close()  # Chiudi il file dopo aver letto tutte le righe

# Inizializza una lista vuota per memorizzare i dati organizzati per cognome
persone_list = []

# Leggi ogni riga del file
for line in lines:
    # Divide la riga utilizzando la virgola come separatore
    dati = line.split(",")

    # Estrai nome, cognome ed età dai dati
    nome = dati[0]
    cognome = dati[1]
    eta = int(dati[2])

    # Aggiungi la tupla contenente nome, cognome ed età alla lista
    persone_list.append((nome, cognome, eta))

# Organizza i dati per cognome mantenendo lo stesso ordine
persone_dict = {}
for persona in persone_list:
    cognome = persona[1]
    if cognome not in persone_dict:
        persone_dict[cognome] = []
    persone_dict[cognome].append(persona)

# Stampa il dizionario contenente i dati organizzati per cognome in ordine alfabetico
print("Dati organizzati per cognome in ordine alfabetico:")
for cognome in sorted(persone_dict.keys()):
    print("persone con cognome" f"{cognome}"":\n")
    for persona in persone_dict[cognome]:
        nome = persona[0]
        cognome = persona[1]
        eta = persona[2]
        print(f"  Nome: {nome}, Cognome: {cognome}, Età: {eta}\n")
