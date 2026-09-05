#ESERCIZIO LIST
# Creare una lista vuota e assegnarla a una variabile.
# Aggiungere numeri interi da 1 a 5 alla lista.
# Accedere all'elemento con indice 2.
# Aggiungere un nuovo elemento "6" alla lista.
# Rimuovere l'elemento con indice 3 dalla lista.
# Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.
# Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
# Ordinare la lista precedente in ordine decrescente.
# Contare quante volte l'elemento "2" appare nella lista precedente.
numeri = []

i = 1
while i <= 5:
    numeri.append(i)

    i += 1
print(numeri)

print(numeri[2])

numeri.append(6)

print(numeri)

numeri.remove(numeri[3])

print(numeri)

numeri_nuovi = [numeri [:3]]

print(numeri_nuovi)

indici_dispari = []

y = 0

while y < len(numeri):
    if y % 2 == 1:
        indici_dispari.append(numeri[y])

    y += 1

print(indici_dispari)

numeri.reverse()

print(numeri)

numero = 0

if 2 in numeri:
    numero += 1

print(f"Il numero 2 appare {numero} volte nella lista.")

# Creare una nuova lista che contenga gli elementi con indici pari della lista precedente, con for e while.
# Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente, con for e while.
for_pari = []
for_dispari = []

for i in range(len(numeri)):
    if i % 2 == 0:
        for_pari.append(numeri[i])
    if i % 2 == 1:
        for_dispari.append(numeri[i])

print(for_pari)
print(for_dispari)

while_pari = []
while_dispari = []

i = 0

while i < len(numeri):
    if i % 2 == 0:
        while_pari.append(numeri[i])
    if i % 2 == 1:
        while_dispari.append(numeri[i])

    i += 1

print(while_pari)
print(while_dispari)

# Creare una lista di numeri interi e stampare solo gli elementi divisibili per 3.
numeri = [12, 7, 18, 25, 31, 44]

for numero in numeri:
    if numero % 3 == 0:
        print(numero)

# Creare due liste di numeri interi. Stampare solo i numeri che sono presenti in entrambe le liste.
numeri = [12, 7, 18, 25, 31, 44]
numeri_bis = [12, 7, 18, 99, 5, 44]

for numero in numeri:
    for numero_bis in numeri_bis:
        if numero == numero_bis:
            print(numero)

#ESERCIZI TUPLE
# Creare una tupla contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
# Aggiungere l'elemento "pesca", poi rimuovere ogni elemento "mela" dalla tupla precedente.
frutta = ("mela", "banana", "kiwi", "mela")
lista_frutti_while = list(frutta)
lista_frutti_while.append("pesca")

for frutta in frutta:
    if frutta == "mela":
        lista_frutti_while.remove("mela")

frutta = tuple(lista_frutti_while)

print(frutta)

# Aggiungere l'elemento ananas, verificare se l'elemento "ananas" è presente
# nella tupla precedente e rimuoverlo.
if not "ananas" in frutta:
    lista_frutti_while.append("ananas")
else:
    lista_frutti_while.remove("ananas")

frutta = tuple(lista_frutti_while)

print(frutta)

# Crea una tupla contenente cinque elementi di tipi diversi.
# Stampa il primo e l'ultimo elemento della tupla.
elementi = (10, "frutta", 2.5, False, frutta)

print(elementi[0])
print(elementi[-1])

# Creare una tupla contenente i numeri interi da 1 a 5.
# Creare una tupla contenente i numeri pari della tupla precedente usando for e while.
# Fare lo stesso con i dispari.
# Fare l'esercizio utilizzando un solo ciclo per estrarre pari e dispari (due tuple diverse).
numeri = (1, 2, 3, 4, 5)
pari_for = []
dispari_for = []

for numero in numeri:
    if numero % 2 == 0:
        pari_for.append(numero)
    else:
        dispari_for.append(numero)

i = 0
pari_while = []
dispari_while = []
while i < len(numeri):
    if numeri[i] % 2 == 0:
        pari_while.append(numeri[i])
    else:
        dispari_while.append(numeri[i])

    i += 1

tuple_pari_for = tuple(pari_for)
tuple_dispari_for = tuple(dispari_for)
tuple_pari_while = tuple(pari_while)
tuple_dispari_while = tuple(dispari_while)

print(tuple_pari_for)
print(tuple_dispari_for)
print(tuple_pari_while)
print(tuple_dispari_while)

# Scrivi un programma che riordini gli elementi in ordine alfabetico di una tupla di stringhe.
# Utilizza for e while.
frutti = ("mela", "banana", "arancia", "pera", "kiwi")
lista_frutti_for = list(frutti)
for frutta in range(len(lista_frutti_for)):
    for x in range(len(lista_frutti_for) - 1):
        if lista_frutti_for[x] > lista_frutti_for[x - 1]:
            temp = lista_frutti_for[x]
            lista_frutti_for[x] = lista_frutti_for[x + 1]
            lista_frutti_for[x + 1] = temp

        frutti_for = tuple(lista_frutti_for)

        print(frutti_for)

lista_frutti_while = list(frutti)

n = len(lista_frutti_while)
i = 0

while i < n:
    j = 0

    while j < n - 1:
        if lista_frutti_while[j] > lista_frutti_while[j + 1]:
            temp = lista_frutti_while[j]
            lista_frutti_while[j] = lista_frutti_while[j + 1]
            lista_frutti_while[j + 1] = temp

        j += 1

    i += 1

frutti_while = tuple(lista_frutti_while)

print(frutti_while)
# Creare una lista di tuple, in cui ogni tupla contiene due stringhe.
# Stampare solo le tuple che hanno entrambe le stringhe di lunghezza pari.
# Fare lo stesso con quelle di lunghezza dispari.
lista_tuple = [
    ("cane", "gatto"),
    ("sole", "mare"),
    ("penna", "quadro"),
    ("vino", "pane"),
    ("rosso", "blu"),
    ("fiore", "albero")
]
for tuple in lista_tuple:
    if len(tuple[0]) % 2 == 0 and len(tuple[1]) % 2 == 0:
        print(f"Tupla pari: {tuple}")
    if len(tuple[0]) % 2 == 1 and len(tuple[1]) % 2 == 1:
        print(f"Tupla dispari: {tuple}")

# Creare una lista di tuple, in cui ogni tupla contiene due stringhe.
# Stampare le tuple in cui entrambe le stringhe iniziano per 'a'.
Lista = [("Ancora", "Spiaggia"), ("Amalfi", "Ancona"), ("Napoli", "Stabia")]

for tupla in Lista:
    if tupla[0].startswith("A") and tupla[1].startswith("A"):
        print(tupla)

# Creare una lista di tuple, in cui ogni tupla contiene due numeri interi.
# Stampare le tuple in cui la somma dei due numeri è pari.
Numeri = [(13, 13), (10, 11), (14, 10)]
risultato = 0

for tupla in Numeri:
    risultato = tupla[0] + tupla[1]
    if risultato % 2 == 0:
        print(tupla)

#ESERCIZI SET
# Creare un set vuoto e assegnarlo a una variabile.
# Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
# Aggiungere l'elemento "pesca" al set precedente.
# Rimuovere l'elemento "pera" dal set precedente.
frutta = {"mela", "banana", "kiwi", "mela"}
frutta.add("pesca")
frutta.discard("pera")
print(frutta)
# Verificare se l'elemento "ananas" è presente nel set precedente. Se è presente lo rimuovi,
# altrimenti fai un print di avviso.
if "ananas" in frutta:
    frutta.remove("ananas")
else:
    print("Ananas non presente.")

# Creare un set contenente i numeri interi da 1 a 5.
# Creare un nuovo set contenente i numeri pari del set precedente.
# Fare lo stesso con i dispari.
# Utilizzare for (unica scelta possibile).
numeri = {1, 2, 3, 4, 5}
pari = set()
dispari = set()

for numero in numeri:
    if numero % 2 == 0:
        pari.add(numero)
    else:
        dispari.add(numero)

print(numeri)
print(pari)
print(dispari)

# Crea due set, A e B, contenenti alcuni numeri interi.
# Trova l'intersezione tra A e B.
# Trova l'unione tra A e B.
# Trova la differenza tra A e B.
# Verifica se un certo elemento è presente in uno dei due set.

A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {2, 4, 6, 8, 10, 12, 14, 16, 18}

C = A.intersection(B)
print(C)
D = A.union(B)
print(D)
E = A.symmetric_difference(B)
print(E)

elemento = 8

if elemento in A or elemento in B:
    print(f"{elemento} presente")

#ESERCIZI DICT
# Creare un dizionario vuoto e assegnarlo a una variabile.
# Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.
persona = {
    "nome" : "Mario",
    "cognome" : "Rossi",
    "età" : 30,
}

print(persona)
# Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.
persona["email"] = "mario.rossi@email.com"
print(persona)

# Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.
persona.pop("cognome")
print(persona)

# Creare una nuova lista che contenga solo le chiavi del dizionario precedente.
chiavi_persona = []

for key in persona:
    chiavi_persona.append(key)

print(chiavi_persona)

# Creare una nuova lista che contenga solo i valori del dizionario precedente.
valori_persona = []

for value in persona.values():
    valori_persona.append(value)

print(valori_persona)

# Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.
persona["età"] = 35

print(persona)

# Contare il numero di elementi nel dizionario precedente.
elementi = 0

for keys, values in persona.items():
    elementi += 1

print(elementi)

# Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
for key in persona:
    print(key)

# Scrivere un programma che utilizzi un loop for per stampare tutti i valori di un dizionario.
for value in persona.values():
    print(value)

# Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
for key, value in persona.items():
    print(key, value)

# Creare un dict in cui le chiavi sono stringhe e i valori sono numeri interi.
# Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5.
numeri = {
    "uno" : 1,
    "due" : 2,
    "tre" : 3,
    "quattro" : 4,
    "cinque" : 5,
    "sette" : 7,
    "nove" : 9,
    "undici" : 11
}


for value in numeri.values():
    if value > 5:
        print(value)

# Creare un dizionario di partenza che contenga un nome ed un cognome. Dopo inserire la matricola, chiedendola
# in input (insieme a nome e cognome) e aggiungere poi gli esami sostenuti con il nome della materia
# ed il voto ottenuto. Calcola inoltre la media delle materie.
persona = {
    "nome" : " ",
    "cognome" : " ",
}

persona["nome"] = input("Inserire il nome: ")
persona["cognome"] = input("Inserire il cognome: ")
persona["matricola"] = input("Inserire la matricola: ")
esami_sostenuti = int(input("Quanti esami hai sostenuto?: "))
persona["esami"] = {}
somma_voti = 0

i = 0
while i < esami_sostenuti:
    esame = input("Inserire esame: ")
    voto = int(input("Inserire voto: "))

    persona["esami"][esame] = voto
    somma_voti += voto

    i += 1

persona["media"] = somma_voti / esami_sostenuti

print(persona)

# Crea un dizionario vuoto chiamato "rubrica" per memorizzare i contatti.
# Fornisci all'utente un menu con le opzioni di aggiungere un nuovo contatto, visualizzare i dettagli di un contatto
# o eliminare un contatto.
# Implementa la logica per ciascuna opzione del menu.
# Assicurati di gestire i casi in cui l'utente cerca di visualizzare o eliminare un contatto che non esiste.


# Creare un dizionario dove le chiavi sono dei semi (bastoni, coppe, denari, cuori) e i valori sono una lista da 1 a 13.
# Estrai una carta casuale a partire da un seme chiesto all'utente. Estrai anche una carta casuale senza chiedere nulla
# all'utente.


# Unisci 2 dizionari qualunque in un terzo.
# Poi cerca di generalizzare l'algoritmo e unisci N dizionari dentro un dizionario.


# Dati2 dizionari, uniscili in un terzo invertendo le chiave con i valori e viceversa.

