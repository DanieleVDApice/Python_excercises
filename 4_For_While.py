import random

#Esercizio 1
#Stampare i numeri da 10 a 1 usando un loop while.
i = 10
while i != 0:
    print(i)
    i -= 1

#Esercizio 2
#Calcolare il fattoriale di un numero intero positivo n usando un loop while.
n = int(input("Inserire un numero intero: "))
fattoriale = 1

i = 1

while i <= n:
    fattoriale *= i
    print(fattoriale)

    i += 1

#Esercizio 3
#Chiedere all'utente di inserire una lista di numeri interi. Stampare la somma di tutti i numeri usando un loop while.
contatore = int(input("Quanti numeri vuoi inserire?: "))
somma = 0
i = 0

while i < contatore:
    numero = int(input("Inserire un numero: "))
    somma += numero
    print(somma)

    i += 1

#Esercizio 4
#Chiedere all'utente di inserire una stringa. Stampare solo le consonanti della stringa usando un loop while.
stringa = input("Inserire una stringa: ")
vocali = ["a", "e", "i", "o", "u"]
i = 0

while i < len(stringa):
    if stringa[i].lower() not in vocali:
        print(stringa[i])

    i += 1

#Esercizio 5
# Scrivere un programma che utilizzi un loop for (e while) per stampare ogni elemento di una lista.
# Scrivere un programma che utilizzi un loop while per stampare tutti i numeri da 1 a 10.
# Stampare i numeri da 10 a 1 usando un loop while.
# Stampare i numeri pari da 2 a 10 (e da 10 a 2) usando un loop while.
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeri:
    print("for: ", numero)

i = 0
while i < len(numeri):
    if i % 2 == 0:
        print("Numeri pari: ", numeri[i])
    print("While: ", numeri[i])
    i += 1

while i <= len(numeri) and i != 0:
    print("While contrario: ", numeri[i - 1])

    i -= 1

#Esercizio 6
# Leggere un numero in input (N) e utilizzare un ciclo while per stampare i primi N (partendo da 0) numeri pari e
# dispari.
n = int(input("Inserire un numero: "))

i = 0

while i <= n:
    if i % 2 == 0:
        print("Pari: ", i)
    if i % 2 == 1:
        print("Dispari: ", i)

    i += 1

#Esercizio 7
# Leggere due numeri in input (N e M) e utilizzarli per stampare tutti i numeri compresi tra N e M
# utilizzando un ciclo while. Distinguere pari e dispari.
n = int(input("Inserire un numero: "))
m = int(input("Inserire un numero: "))

if n < m:
    while n <= m:
        if n % 2 == 0:
            print("Pari: ", n)
        if n % 2 == 1:
            print("Dispari: ", n)
        if n == m:
            break

        n += 1

if n > m:
    while m <= n:
        if m % 2 == 0:
            print("Pari: ", m)
        if m % 2 == 1:
            print("Dispari: ", m)
        if m == n:
            break

        m += 1

#Esercizio 8
# Leggere due numeri in input (N e M) e utilizzarli per sommare tutti i numeri compresi tra N e M utilizzando un
# ciclo while.
n = int(input("Inserire un numero: "))
m = int(input("Inserire un numero: "))
somma = 0
differenza = 0
i = 0

if n < m:
    differenza = m - n
if n > m:
    differenza = n - m

while i <= differenza:
    if n < m:
        somma += (n + i)
        print("Somma totale dei numeri: ", somma)
    if n > m:
        somma += (m + i)
        print("Somma totale dei numeri: ", somma)

    i += 1

#Esercizio 9
# Leggere due numeri in input (N e M) e fare la somma alterna, cioè somma i pari e sottrai i dispari.
# Farlo anche con una lista, usando il for e il while.
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somma_for_pari = 0
somma_for_dispari = 0


for numero in numeri:
    if numero % 2 == 0:
        somma_for_pari += numero

    if numero % 2 == 1:
        somma_for_dispari += numero

print("Somma pari con FOR: ", somma_for_pari)
print("Somma dispari con FOR: ", somma_for_dispari)

somma_while_pari = 0
somma_while_dispari = 0
i = 0

while i < len(numeri):
    if numeri[i] % 2 == 0:
        somma_while_pari += numeri[i]
    if numeri[i] % 2 == 1:
        somma_while_dispari += numeri[i]

    i += 1
print("Somma pari con WHILE: ", somma_while_pari)
print("Somma dispari con WHILE: ", somma_while_dispari)


n = int(input("Inserire un numero: "))
m = int(input("Inserire un numero: "))
somma_pari = 0
somma_dispari = 0
differenza = 0

i = 0
if n < m:

    differenza = m - n
if m < n:
    differenza = n - m

while i <= differenza:
    if n < m:
        if (n + i) % 2 == 0:
            somma_pari += (n + i)
        if (n + i) % 2 == 1:
            somma_dispari += (n + i)
    if n > m:
        if (m + i) % 2 == 0:
            somma_pari += (m + i)
        if (m + i) % 2 == 1:
            somma_dispari += (m + i)

    i += 1

print("Somma pari: ", somma_pari)
print("Somma dispari: ", somma_dispari)

#Esercizio 10
# Scrivere un programma che utilizzi un loop for (e while) per sommare tutti i numeri in una lista.
# Adesso fare lo stesso, ma imporre che la somma non superi 20.
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somma_for = 0

for numero in numeri:
    somma_for += numero
    if somma_for > 20:
        somma_for = 20
        break

print("Somma for: ", somma_for)

somma_while = 0
i = 0

while i < len(numeri):
    somma_while += numeri[i]

    i += 1
print("Somma while: ", somma_while)

#Esercizio 11
# Scrivere un programma che utilizzi un for (e while) per calcolare la media di una lista di numeri (int e float).
numeri = [1, 2.15, 3, 4.30, 5, 6.45, 7, 8.20, 9, 10.35]
somma_for = 0

for numero in numeri:
    somma_for += numero

media_for = somma_for / len(numeri)
print("Somma FOR: ", somma_for)
print("Media FOR: ", media_for)

somma_while = 0

i = 0
while i < len(numeri):
    somma_while += numeri[i]

    i += 1

media_while = somma_while / len(numeri)
print("Somma WHILE: ", somma_while)
print("Media WHILE: ", media_while)

#Esercizio 12
# Calcolare il fattoriale di un numero intero positivo n usando un loop while.
# Poi calcola il fattoriale di ogni elemento della lista, con for e while.
numero = int(input("Inserire un numero: "))
numeri = [3, 4, 5, 6]
fattoriale_n = 1
i = 1
while i <= numero:
    fattoriale_n *= i

    i += 1
print("Fattoriale Input: ", fattoriale_n)

fattoriale_lista_while = []
y = 0
while y < len(numeri):

    n = numeri[y]
    fattoriale = 1
    i = 1

    while i <= n:
        fattoriale *= i
        i += 1

    fattoriale_lista_while.append(fattoriale)

    y += 1

print("Fattoriali WHILE: ", fattoriale_lista_while)

fattoriale_lista_for = []
for n in numeri:

    fattoriale = 1

    for i in range(1, n + 1):
        fattoriale *= i

    fattoriale_lista_for.append(fattoriale)

print("Fattoriali FOR: ", fattoriale_lista_for)

#Esercizio 13
# Calcola i quadrati di una serie di numeri dentro una lista con for e while.
numeri = [2, 4, 6, 8, 10]
quadrati_for = []

for numero in numeri:
    quadrato = numero * numero

    quadrati_for.append(quadrato)

print("FOR: ", quadrati_for)

quadrati_while = []
i = 0
while i < len(numeri):
    quadrato = numeri[i] * numeri [i]

    quadrati_while.append(quadrato)

    i += 1

print("WHILE: ", quadrati_while)

#Esercizio 14
# Calcolare la potenza di un numero intero. I valori base ed esponente sono a scelta dello studente.
# Ricordiamo che un numero a elevato a n è il prodotto di a eseguito n volte.
# Poi fare il calcolo usando una lista di numeri come base e come esponente.
bases = [2, 4, 6, 8]
esponentes = [3, 5, 7, 9]
potenze = []

for base in bases:
    for esponente in esponentes:
        potenza = base ** esponente
        potenze.append(potenza)

print(potenze)


potenze_while = []

base = 0
esponente = 0
i = 0
while i < len(esponentes):
    potenza = bases[base] ** esponentes[esponente]

    potenze_while.append(potenza)

    i += 1
    base += 1
    esponente += 1

print(potenze_while)
#Oppure
#potenze_due = []
#for base in bases:
#    for esponente in esponentes:
#        potenza = 1
#        for i in range(esponente):
#            potenza *= base
#            potenze_due.append(potenza)
#print(potenze_due)

#i = 0
#while i < len(bases):
#    j = 0
#    while j < len(esponentes):
#        base = bases[i]
#        esponente = esponentes[j]
#        potenza = 1
#        k = 0
#        while k < esponente:
#            potenza *= base
#            k += 1
#        potenze.append(potenza)
#        j += 1
#    i += 1
#print(potenze)

#Esercizio 15
# Esegui una somma cumulativa dei numeri inseriti dall'utente fino a quando viene inserito il numero 0 utilizzando un
# ciclo while.
quantita = int(input("Quanti numeri vuoi inserire: "))
totale = 0

i = 0
while i < quantita:
    numero = int(input("Inserire un numero: "))
    totale += numero
    if numero == 0:
        break
    i += 1
print("Totale: ", totale)

#Esercizio 16
# Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10.
# Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.
risposta = random.randint(1, 10)

indovinato = False
while indovinato == False:
    utente = int(input("Inserire un numero compreso tra 1 a 10: "))

    if utente == risposta:
        print("Hai indovinato!")
        indovinato = True
    else:
        print("Hai sbagliato, ritenta")

#Esercizio 17
# Inserire due numeri interi da tastiera: n, val. Il programma a questo punto deve chiedere all’utente di inserire n
# valori interi e verificare quanti di questi sono maggiori, minori o uguali a val.
# E se volessi farlo con una lista?
val = int(input("Inserire un numero: "))
quantita = int(input("Quanti numeri vuoi inserire?: "))
maggiore = []
minore = []
uguale = []

i = 0
while i < quantita:
    numero = int(input("Inserire un numero: "))
    if numero < val:
        minore.append(numero)
        print(numero, "è minore di ", val )
    if numero > val:
        maggiore.append(numero)
        print(numero, "è maggiore di ", val)
    if numero == val:
        uguale.append(numero)
        print(numero, "è uguale a ", val)
    i += 1
print("Minori: ", len(minore)," Maggiori: ", len(maggiore)," Uguali: ", len(uguale))


val_due = int(input("Inserire un numero compreso tra 1 e 10: "))
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

maggiori = 0
minori = 0
uguali = 0
for numero in numeri:
    if numero < val_due: minori += 1
    if numero > val_due: maggiori += 1
    if numero == val_due: uguali += 1

print("Maggiori: ", maggiori)
print("Minori: ", minori)
print("Uguali: ", uguali)

#Esercizio 18
# Scrivere un programma che stampi a video tutti i numeri compresi tra due estremi a e b letti da tastiera.
# Il programma deve dire anche quanti sono i pari, i dispari e quanti i numeri totali.
a = int(input("Inserire un numero: "))
b = int(input("Inserire un numero: "))

pari = 0
dispari = 0
totali = 0

i = 0
y = 0
if a < b:
    y = b
    i = a
if b < a:
    y = a
    i = b

while i <= y:
    if i % 2 == 0:
        pari += 1
    else:
        dispari += 1

    print(i)
    totali += 1
    i += 1

print("Pari: ", pari, "Dispari: ", dispari, "Totali: ", totali)

#Esercizio 19
# Calcolare la somma dei cubi dei primi k numeri pari.
# Farlo anche per i dispari. Dare anche la somma totale.
numeri = [3, 4, 5, 6, 7, 8]
cubi = []
somma_pari = 0
somma_dispari = 0
somma_totale = 0

i = 0
while i < len(numeri):
    cubo = numeri[i] * numeri[i] * numeri[i]
    cubi.append(cubo)
    if numeri[i] % 2 == 0:
        somma_pari += cubo
    else:
        somma_dispari += cubo
    i += 1
    somma_totale = somma_pari + somma_dispari

print("Lista numeri: ", numeri)
print("Lista cubi: ", cubi)
print("Somma cubi dei numeri pari: ", somma_pari)
print("Somma cubi dei numeri dispari: ", somma_dispari)
print("Somma totale: ", somma_totale)

#Esercizio 20
# Scrivere un programma che lette da tastiera le temperature
# T di un mese (il numero di giorni del mese è letto da tastiera) determini la temperatura media,
# la temperatura minima e la temperatura massima. Farlo sia con while che con for.
temperature = [20, 16, 21, 15, 17, 18, 17, 15, 22, 17, 17, 15, 19, 16, 21, 20, 19, 20, 18, 24, 20, 22, 21, 17, 19, 18,
               24, 16, 17, 25]
temperatura_media = 0
temperatura_minima = temperature[0]
temperatura_massima = temperature[0]

i = 0
while i < len(temperature):
    temperatura_media += temperature[i]
    if temperature[i] < temperatura_minima:
        temperatura_minima = temperature[i]
    if temperature[i] > temperatura_massima:
        temperatura_massima = temperature[i]

    i += 1

temperatura_media /= len(temperature)

print(f"Temperature mese: {temperature}")
print(f"Temperatura minima: {temperatura_minima}")
print(f"Temperatura massima: {temperatura_massima}")
print(f"Temperatura media: {temperatura_media}")

#for temperatura in temperature:
#    temperatura_media += temperatura
#    if temperatura < temperatura_minima:
#        temperatura_minima = temperatura
#    if temperatura > temperatura_massima:
#        temperatura_massima = temperatura
#
#temperatura_media /= len(temperature)
#print(f"Temperature mese: {temperature}")
#print(f"Temperatura minima: {temperatura_minima}")
#print(f"Temperatura massima: {temperatura_massima}")
#print(f"Temperatura media: {temperatura_media}")

#Esercizio 21
# Generare un numero a caso compreso tra 1-100 e chiedere all’utente un numero fino a quando non
# è uguale a quello generato casualmente. Dire ogni volta se il numero immesso è > o < di quello
# iniziale. Indicare anche il numero di tentativi.

risposta = random.randint(1, 100)
tentativi = 5

while tentativi > 0:
    tentativi -= 1

    utente = int(input("Inserisci un numero compreso tra 1 e 100: "))
    if utente == risposta:
        print("Congratulazioni! Hai indovinato!")
        break
    if utente < risposta:
        print("Pss. Prova ad aumentare.")
    if utente > risposta:
        print("Pss. Prova a diminuire.")
    if tentativi > 0:
        print(f"Hai ancora {tentativi} tentativi.")
    if tentativi == 0:
        print(f"Mi dispiace, hai perso. Il numero giusto era: {risposta}")
        break