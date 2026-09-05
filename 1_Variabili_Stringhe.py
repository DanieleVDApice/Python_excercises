#Esercizi Variabili
#Esercizio 1
#Dichiarare una variabile "nome" e assegnargli il tuo nome. Mandare a schermo.
nome = "Daniele"

print(nome)

#Esercizio 2
#Dichiarare una variabile "eta" e assegnargli la tua età. Mandare a schermo.
eta = "29"

print(int(eta))

#Esercizio 3
#Dichiarare una variabile "pi" e assegnargli il valore di pi greco (3,14159). Mandare a schermo.
pi = 3.14159

print(pi)

#Esercizio 4
#Creare una variabile "lunghezza" e assegnargli un valore, quindi riassegnare la variabile a 15. Mandare a schermo.
lunghezza = 5
lunghezza = 15

print(lunghezza)

#Esercizio 5
#Creare una variabile "nome_completo" e assegnargli una stringa contenente il tuo nome e cognome. Mandare a schermo.
nome_completo = "Daniele D'Apice"

print(nome_completo)

#Esercizio 6
#Creare una variabile "eta_futura" e assegnargli il valore dell'età che avrai tra 10 anni
#(utilizzando la variabile età già esistente). Mandare a schermo.
eta_futura = int(eta) + 10

print(eta_futura)

#Esercizio 7
#Creare delle variabili "nome", "cognome" ed "anno_di_nascita" ed assegnarle il valore dei valori.
#Mandare a schermo in un unico print. Sovrascrivere tutte le variabili e rimandare a schermo una seconda volta.
nome = "Daniele"
cognome = "D'Apice"
anno_di_nascita = 1996

print(nome, cognome, anno_di_nascita)

#Esercizio 8
#Creare una variabile `eta_attuale` e assegnargli il valore dell'età che hai attualmente,
#calcolandola in base all'anno corrente. Mandare a schermo `eta_attuale`
anno_corrente = 2026
eta_attuale = anno_corrente - anno_di_nascita

print(eta_attuale)

#Esercizi Stringhe
#Esercizio 1
#Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper() per convertirla in
# maiuscolo in una nuova variabile.
stringa = "ciao mondo"
stringa_maiuscola = stringa.upper()
print(stringa_maiuscola)

#Esercizio 2
#Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per convertirla
# in minuscolo in una nuova variabile.
stringa = "Benvenuti a Roma"
stringa_minuscola = stringa.lower()

print(stringa_minuscola)

#Esercizio 3
#Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split() per
# dividere la stringa in una lista di parole.
stringa = "Il meglio deve ancora venire"
stringa_split = stringa.split()

print(stringa_split)

#Esercizio 4
#Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace() per sostituire "World"
# con "Python".
stringa = "Hello World"
stringa_replace = stringa.replace("World", "Python")

print(stringa_replace)
#Esercizio 5
#Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per rimuovere gli spazi vuoti
# all'inizio e alla fine della stringa..
stringa = " Ciao "
stringa_strip = stringa.strip()

print(stringa_strip)

#Esercizio 6
#Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.
stringa = "abcdefg"

print(stringa[:3])

#Esercizio 7
#Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith() per verificare se la
# stringa inizia con "Py".
stringa = "Python"

print(stringa.startswith("Py"))

#Esercizio 8
#Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero di
# volte in cui la lettera "o" appare nella stringa.
stringa = "Ciao mondo"

print(stringa.count("o"))

#Esercizio 9
#Assegnare una stringa "Ciao mondo" ad una variabile "stringa". Mandare quindi a schermo gli ultimi 5 caratteri della
# stringa in maiuscolo, sostituendo il carattere "o" con "k".
stringa = "Ciao mondo"

print(stringa.replace("o","k").upper()[5:])