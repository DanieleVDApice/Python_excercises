# 1)Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. Aggiungi un metodo “presentati”
# che stampi una frase di presentazione della persona, ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.
class Persona:
    def __init__(self, nome, eta, sesso):
        self.nome = nome
        self.eta = eta
        self.sesso = sesso

    def presentati(self):
        presentazione = f"Ciao sono {self.nome}, ho {self.eta}, e sono {self.sesso}"
        return presentazione

persona = Persona("Daniele Vittorio D'Apice", 29, "maschio")

print(persona.presentati())
print()

# 2)Creare una classe Animale che abbia gli attributi “nome” e “specie”. Aggiungi un metodo “emetti_suono”
# che stampi un suono specifico per ogni specie. Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”,
# se è un cane “Bau!”.

class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def emetti_suono(self):
        specie = self.specie.lower()
        if specie == "gatto":
            return "Miao!"
        if specie == "cane":
            return "Bau!"

animale1 = Animale("Sally", "cane")
animale2 = Animale("Stivaletto", "gatto")

print(animale1.emetti_suono())
print(animale2.emetti_suono())
print()

# 3)Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”. Aggiungi un metodo “descrivi”
# che stampi una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.

class Automobile:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi(self):
        return f"Questa è una {self.marca} {self.modello} del {self.anno}"

auto1 = Automobile("Subaru", "Baracca", 1999)
auto2 = Automobile("Fiat", "Panda", 2025)

print(auto1.descrivi())
print(auto2.descrivi())
print()

# 4)Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”.
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo “stampa_dettagli”
# che stampi tutti i dettagli dell’impiegato, ad esempio “Impiegato: Marco Rossi, matricola 12345, stipendio: 3000 Euro”.

class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendi(self):
        nuovo_stipendio = self.stipendio + (self.stipendio * 10/100)
        return nuovo_stipendio

    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}\nMatricola: {self.matricola}\nStipendio:{self.stipendio} euro - "
              f"Nuovo stipendio: {self.aumenta_stipendi()} euro")

impiegato = Impiegato("Marco", "Rossi", "matricola 12345",3000)

impiegato.stampa_dettagli()

# 5)Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
# Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
# Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
# La classe dovrà avere i seguenti metodi:
# Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
# Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
# Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
# Crea inoltre una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.

class Prodotto:
    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta

class GestoreMagazzino:
    def __init__(self, costo_magazzinaggio):
        self.costo_magazzinaggio = costo_magazzinaggio
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto):
        self.prodotti[prodotto.nome] = prodotto

    def rimuovi_prodotto(self, nome_prodotto):
        if nome_prodotto in self.prodotti:
            self.prodotti.pop(nome_prodotto)
        else:
            print(f"Prodotto '{nome_prodotto}' non presente in magazzino")

    def calcola_costi_magazzinaggio(self):
        costi = 0
        for nome, prodotto in self.prodotti.items():
            costi += prodotto.scorta * self.costo_magazzinaggio
        return costi

prodotto1 = Prodotto("Pane", 1.5, 30)
prodotto2 = Prodotto("Latte", 1.2, 20)
prodotto3 = Prodotto("Pasta", 0.9, 50)
prodotto4 = Prodotto("Sapone", 2.3, 15)
prodotto5 = Prodotto("Dentifricio", 2.8, 10)
prodotto6 = Prodotto("Carta igienica", 4.5, 25)


magazzino = GestoreMagazzino(10)

magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)
magazzino.aggiungi_prodotto(prodotto4)
magazzino.aggiungi_prodotto(prodotto5)
magazzino.aggiungi_prodotto(prodotto6)

print("Costo totale magazzinaggio: ", magazzino.calcola_costi_magazzinaggio())

magazzino.rimuovi_prodotto("Carta igienica")

print("Costo totale magazzinaggio: ", magazzino.calcola_costi_magazzinaggio())

#Esercizio 1
# Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno.
# Aggiungi poi i metodi accellera e frena. Creare poi una classe Auto che eredita da Veicolo ma aggiunge
# la proprietà colore ed il metodo cambia_colore().
# Modifica la classe Auto in modo che erediti anche il metodo __str__() dalla classe Veicolo,
# in modo da stampare le informazioni sull’auto in questo formato: “Marca: Ferrari, Modello: Enzo, Anno: 2004,
# Colore: Rosso”.

class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def accellera(self):
        print("l'auto accellera")

    def frena(self):
        print("l'auto frena")

    def __str__(self):
        stringa = f"Marca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}\n"
        return stringa


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, colore):
        super().__init__(marca, modello, anno)
        self.colore = colore

    def cambia_colore(self, cambio_colore):
        self.colore = nuovo_colore
        return self.colore

    def __str__(self):
        stringa = super().__str__()
        stringa += f"Colore: {self.colore}\n"
        return stringa

veicolo = Auto("Ferrari", "Enzo", 2004, "Rosso")
print(veicolo)

veicolo.accellera()
veicolo.frena()
print()

nuovo_colore = "Nero"
veicolo.cambia_colore(nuovo_colore)
print(veicolo)

#Esercizio 2
# Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma. Poi crea le classi Quadrato e
# Cerchio che ereditino dalla classe Forma e che implementino il metodo area() in modo appropriato per ogni forma.
# Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.

class Forma:
    def area(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        self.area = self.lato * self.lato
        return self.area

    def __str__(self):
        stringa = f"L'area del quadrato è {self.area}"
        return stringa

class Cerchio(Forma):
    def __init__(self, diametro):
        self.diametro = diametro

    def area(self):
        self.area = 3.14 * self.diametro * self.diametro
        return self.area

    def __str__(self):
        stringa = f"L'area del cerchio è {self.area}"
        return stringa

quadrato = Quadrato(4)
quadrato.area()
print(quadrato)
print()

cerchio = Cerchio(5)
cerchio.area()
print(cerchio)