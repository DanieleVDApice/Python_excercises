#ESERCIZI @staticmethod

#Facile
#Classe: MathUtils
#Crea una @staticmethod chiamata is_even(numero) che: ritorna True se il numero è pari, False altrimenti
#Usala sia: tramite la classe, tramite un’istanza

class Pari:
    def __init__(self, numero):
        self.numero = numero
    @staticmethod
    def is_pari(numero):
        return numero % 2 == 0


pari = Pari(1000)
print(pari.is_pari(pari.numero))

print(Pari.is_pari(122345))

#Medio
#Classe: StringUtils
#Crea una @staticmethod chiamata is_palindrome(testo) che:
#ignora maiuscole/minuscole, ignora spazi, ritorna True se la stringa è palindroma
#Esempi:
#"Anna" → True
#"i topi non avevano nipoti" → True

class Parola:
    def __init__(self, stringa):
        self.stringa = stringa

    @staticmethod
    def is_palindroma(stringa):
        stringa = stringa.lower()
        stringa = stringa.replace(" ", "")
        stringa = stringa.replace(".", "")
        stringa = stringa.replace("-", "")
        stringa = stringa.replace(",", "")
        return stringa == stringa[::-1]

parola = Parola("I topi non avevano nipoti")
print(parola.is_palindroma(parola.stringa))

print(Parola.is_palindroma("Annarella"))

# Difficile
#Classe: PasswordValidator
#Crea una @staticmethod validate(password) che ritorna True solo se: lunghezza ≥ 8
#contiene almeno una lettera maiuscola, contiene almeno un numero, contiene almeno un carattere speciale (!@#$%^&*)

class Password:
    def __init__(self, stringa):
        self.stringa = stringa

    @staticmethod
    def controllo_password(password):
        lettere = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        numeri = "0123456789"
        speciali = "!@#$%^&*."
        lunghezza = 8

        ha_lunghezza = False
        ha_lettera = False
        ha_numero = False
        ha_speciale = False

        if len(password) >= lunghezza:
            ha_lunghezza = True
        for c in password:
            if c in lettere:
                ha_lettera = True
            elif c in numeri:
                ha_numero = True
            elif c in speciali:
                ha_speciale = True

        return ha_lunghezza and ha_lettera and ha_numero and ha_speciale

password = Password("aBcDeFgHi123...")
print(password.controllo_password(password.stringa))

#ESERCIZI @classmethod

#Facile
#Classe: Counter, attributo di classe count = 0
#@classmethod increment() che aumenta count di 1. @classmethod reset() che riporta count a 0. Testa creando più istanze.

class Counter:
    count = 0
    def __init__(self):
        pass

    @classmethod
    def incrementa(cls):
        cls.count += 1
        pass

    @classmethod
    def decrementa(cls):
        cls.count -= 1
        pass

Counter.incrementa()
Counter.incrementa()
Counter.incrementa()
Counter.incrementa()
Counter.decrementa()
Counter.decrementa()

print(Counter.count)

#Medio
#Classe: Person, Attributi: name, age
#Crea una @classmethod from_string(cls, data) che: riceve una stringa tipo "Mario,25", ritorna un oggetto Person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))


p = Person.from_string("Mario,25")
print(p.name)
print(p.age)

#Difficile
#Classe: Product, Attributi: name, price, attributo di classe tax_rate = 0.22
#Crea una @classmethod set_tax_rate(cls, new_rate) che: cambia l’IVA per tutti i prodotti
#Poi: crea più prodotti, verifica che il nuovo valore venga applicato a tutti

class Prodotto:
    iva = 0.22
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    @classmethod
    def set_tax_rate(cls, nuova_iva):
        cls.iva = nuova_iva
        return

    def prezzo_con_iva(self):
        return self.prezzo + self.prezzo * self.iva

    def prezzo_senza_iva(self):
        return self.prezzo / (1 + self.iva)

Prodotto.set_tax_rate(0.30)
prodotto1 = Prodotto("Nutella", 5)
prodotto2 = Prodotto("Carta igienica", 3)
prodotto3 = Prodotto("Patate", 1.5)
prodotto4 = Prodotto("Pane", 1.25)

print(prodotto1.prezzo_con_iva())
print(prodotto2.prezzo_senza_iva())
print(prodotto3.prezzo_con_iva())
print(prodotto4.prezzo_senza_iva())

#Esercizio 1 – Veicoli
#Traccia
#Crea una classe Veicolo con:
#attributi: marca, velocita_max
#un @classmethod crea_standard() che restituisce un veicolo con valori predefiniti
#un @staticmethod km_in_miglia(km) che converte km in miglia
#Crea una sottoclasse Auto che:
#aggiunge l’attributo porte
#ridefinisce un metodo descrizione()
#Obiettivo: Capire come una sottoclasse estende una classe base e usa metodi di classe e statici.

#Esercizio 2 – Dipendenti
#Traccia
#Crea una classe Dipendente con:
#attributi: nome, stipendio
#un @classmethod da_stringa() che crea un dipendente partendo da "Mario,3000"
#un @staticmethod calcola_bonus(stipendio) che restituisce il 10% dello stipendio
#Crea una sottoclasse Manager che:
#aggiunge l’attributo team_size
#ridefinisce il metodo calcola_stipendio_totale() includendo un bonus extra
#Obiettivo
#Usare @classmethod come factory method e distinguere bene i metodi statici.

#Esercizio 3 – Animali
#Traccia
#Crea una classe Animale con:
#attributi: nome, eta
#un @classmethod cucciolo(nome) che crea un animale di 0 anni
#un @staticmethod is_maggiorenne(eta) che ritorna True se l’età ≥ 2
#Crea una sottoclasse Cane che:
#aggiunge l’attributo razza
#implementa il metodo verso() che stampa "Bau!"
#Obiettivo: Capire quando usare @classmethod rispetto al costruttore classico.