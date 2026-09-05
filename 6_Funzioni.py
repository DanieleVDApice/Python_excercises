# 1)Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.

def somma_lista(lista):
    somma = 0
    for i in lista:
        somma += i
    return somma

print(somma_lista([1, 2, 3, 4, 5]))

# 2)Scrivi una funzione che prende una stringa e restituisce la stringa invertita.

def inverti_stringa(stringa):
    return stringa[::-1]

print(inverti_stringa("Daniele Vittorio D'Apice"))

# 3)Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano
# con una lettera specificata.

def trova_lettera(lettera):
    lista = ["Ape", "Bottiglia", "Ciliegia", "Dado", "Albero"]
    parole = []
    lettera = lettera.upper()
    for parola in lista:
        if parola[0] == lettera:
            parole.append(parola)
    return parole

print(trova_lettera("a"))

# 4)Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna
# parola.

def lunghezza_parola(lista):
    lunghezza = []
    for parola in lista:
        lunghezza.append(len(parola))
    return lunghezza
parole = ["Ape", "Bottiglia", "Ciliegia", "Dado", "Albero"]
print(lunghezza_parola(parole))

#5)Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.

def piu_lunga(lista):
    lunga = ""
    for parola in lista:
        if len(parola) > len(lunga):
            lunga = parola
    return lunga
parole = ["Ape", "Bottiglia", "Ciliegia", "Dado", "Albero"]
print(piu_lunga(parole))

#6)Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.

def trova_palindrome(lista):
    palindrome = []
    for parola in parole:
        if parola == parola[::-1]:
            palindrome.append(parola)
    return palindrome

parole = ["casa", "albero", "penna", "radar", "anna", "otto"]
print(trova_palindrome(parole))

# 7)Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.

def trova_pari(lista):
    pari = []
    for numero in numeri:
        if numero % 2 == 0:
            pari.append(numero)
    return pari

numeri = [1,2,3,4,5,6,7,8,9,10]
print(trova_pari(numeri))

# 8)Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.

def trova_massimo(lista):
    massimo = 0
    for numero in numeri:
        if numero > massimo:
            massimo = numero
    return massimo

numeri = [1,2,3,4,5,6,7,8,9,10]
print(trova_massimo(numeri))

# 9)Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.

def trova_media(lista):
    media = 0
    for numero in numeri:
        media = media + numero
    return media/len(numeri)

numeri = [1,2,3,4,5,6,7,8,9,10]
print(trova_media(numeri))

# 10)Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo
# i numeri maggiori di un valore specificato.

def trova_maggiori(valore):
    numeri_maggiori = []
    for numero in numeri:
        if numero > valore:
            numeri_maggiori.append(numero)
    return numeri_maggiori

numeri = [1,2,3,4,5,6,7,8,9,10]
print(trova_maggiori(5))