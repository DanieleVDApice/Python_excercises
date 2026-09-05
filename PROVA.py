# Crea un dizionario vuoto chiamato "rubrica" per memorizzare i contatti.
# Fornisci all'utente un menu con le opzioni di aggiungere un nuovo contatto, visualizzare i dettagli di un contatto
# o eliminare un contatto.
# Implementa la logica per ciascuna opzione del menu.
# Assicurati di gestire i casi in cui l'utente cerca di visualizzare o eliminare un contatto che non esiste.
rubrica = {}

while True:
    print("\n1 - Nuovo contatto")
    print("2 - Visualizza contatto")
    print("3 - Elimina contatto")
    print("0 - Chiudi")

    opzione = int(input("Scegli un'opzione: "))

    if opzione == 0:
        print("Rubrica chiusa.")
        break

    elif opzione == 1:
        nome = input("Inserire nome: ")
        cognome = input("Inserire cognome: ")
        numero = input("Inserire numero: ")

        rubrica[nome] = {
            "cognome": cognome,
            "numero": numero
        }

        print("Contatto aggiunto.")

    elif opzione == 2:
        nome = input("Inserire il nome del contatto: ")

        if nome in rubrica:
            print("Nome:", nome)
            print("Cognome:", rubrica[nome]["cognome"])
            print("Numero:", rubrica[nome]["numero"])
        else:
            print("Contatto non trovato.")

    elif opzione == 3:
        nome = input("Inserire il nome del contatto da eliminare: ")

        if nome in rubrica:
            del rubrica[nome]
            print("Contatto eliminato.")
        else:
            print("Contatto non trovato.")

    else:
        print("Opzione non valida.")

# Creare un dizionario dove le chiavi sono dei semi (bastoni, coppe, denari, cuori) e i valori sono una lista da 1 a 13.
# Estrai una carta casuale a partire da un seme chiesto all'utente. Estrai anche una carta casuale senza chiedere nulla
# all'utente.


# Unisci 2 dizionari qualunque in un terzo.
# Poi cerca di generalizzare l'algoritmo e unisci N dizionari dentro un dizionario.


# Dati2 dizionari, uniscili in un terzo invertendo le chiave con i valori e viceversa.

