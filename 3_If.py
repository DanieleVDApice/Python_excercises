#Esercizio 1
#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero
# è maggiore di zero, altrimenti stampa "Il numero è negativo".
numero = int(input("Inserire un numero: "))
if numero > 0:
    print("Il numero è positivo")
else:
    print("Il numero è negativo")

#Esercizio 2
#Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore"
# se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo,
# altrimenti stampa "I numeri sono uguali".
numero1 = int(input("Inserire il primo numero: "))
numero2 = int(input("Inserire il secondo numero: "))
if numero1 > numero2:
    print("Il primo numero è maggiore di: ", numero1 - numero2)
elif numero2 > numero1:
    print("Il secondo numero è maggiore di: ", numero2 - numero1)
else:
    print("I numeri sono uguali")

#Esercizio 3
#Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota,
# altrimenti stampa "La stringa non è vuota".
stringa = input("Inserire una stringa: ")
if stringa == "":
    print("La stringa è vuota")
else:
    print("La stringa non è vuota")

#Esercizio 4
#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari,
# altrimenti stampa "Il numero è dispari".
numero = int(input("Inserire un numero: "))
if numero % 2 == 0:
    print(numero, " è pari")
else:
    print(numero, " è dispari")

#Esercizio 5
#Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è
# una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
lettera = input("Inserire una lettera: ")
vocali = ["a", "e", "i", "o", "u"]
if lettera.lower() in vocali:
    print(lettera, " è una vocale")
else:
    print(lettera, "NON è una vocale")

#Esercizio 6
#Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10"
# se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".
numero = int(input("Inserire un numero: "))
if 1 <= numero <= 10:
    print(numero, " è compreso tra 1 e 10")
else:
    print(numero, " NON è compreso tra 1 e 10")

#Esercizio 7
#Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, stampare
# "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10".
# Se il numero è minore di 10, stampare "Il numero è minore di 10".
numero_intero = int(input("Inserire un numero intero: "))
if numero_intero < 10:
    print(numero_intero, " è minore di 10")
elif numero_intero > 10:
    print(numero_intero, " è maggiore di 10")
else:
    print(numero_intero, " è uguale a 10")

#Esercizio 8
#Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u)
# con isalpha(), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante,
# stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare
# "Il carattere inserito non è una lettera".
carattere = input("Inserire una lettera: ")
vocali = ["a", "e", "i", "o", "u"]
if carattere.isalpha():
    if carattere.lower() in vocali:
        print(carattere, " è una vocale")
    else:
        print(carattere, " è una consonante")
else:
    print(carattere, " Non è una lettera")

#Esercizio 9 (difficile)
#Scrivi un programma che chieda all'utente di inserire tre numeri interi che rappresentano i lati di un triangolo.
# Il programma deve verificare se questi tre numeri formano un triangolo rettangolo.
# Se i tre numeri soddisfano la condizione per essere un triangolo rettangolo (cioè rispettano il teorema di Pitagora),
# allora stampa "I tre numeri formano un triangolo rettangolo".
# Altrimenti, stampa "I tre numeri non formano un triangolo rettangolo".
numero1 = int(input("Inserire un numero: "))
numero2 = int(input("Inserire un numero: "))
numero3 = int(input("Inserire un numero: "))

teorema = (numero1 ** 2) + (numero2 ** 2)

if teorema == numero3:
    print("I tre numeri formano un triangolo rettangolo")
else:
    print("I tre numeri NON formano un triangolo rettangolo")