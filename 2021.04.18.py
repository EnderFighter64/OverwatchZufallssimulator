from random import randint
import math

# Definitionen (Variablen weiter unten)
def ListenErsteller(AnzahlZwischenschritte, Differenz):
    MerkeZwischenschritte = AnzahlZwischenschritte
    ListeZwischenschritte = list()
    NotierListe = list()
    while AnzahlZwischenschritte < Differenz:    
        ListeZwischenschritte.append(AnzahlZwischenschritte)
        NotierListe.append(0)
        AnzahlZwischenschritte += MerkeZwischenschritte
    return(ListeZwischenschritte, NotierListe)

def Listenrechner(ListeZwischenschritte, NotierListe, Zahl):
    Index = 0
    while Index < len(NotierListe):
        if Zahl >= ListeZwischenschritte[Index]:
            NotierListe[Index] += 1
        Index += 1
    return(NotierListe)
    
    
def Randomgenerator(Rangverteilung):
    Zahl = randint(0, Rangverteilung[len(Rangverteilung)-1])
    Index = 0
    while True:
        if Zahl > Rangverteilung[Index]:
            Index += 1
        else:
            return(Index)
        
def StandartabweichungRechner(Zahlenhistorie, Zahlenaddition, GesamtWdh):
    Durchschnitt = Zahlenaddition / GesamtWdh
    Index = 0
    Varianz = 0
    while Index < len(Zahlenhistorie):
        Varianz += (Zahlenhistorie[Index] - Durchschnitt) ** 2
        Index += 1
    Varianz /= len(Zahlenhistorie)
    return(Durchschnitt, math.sqrt(Varianz))
        
# Variablen zum Ändern
Rangverteilung = [25, 12, 35, 10, 0, 0, 0, 0]
Differenz = 59
Matches = 18
AnzahlZwischenschritte = 10
StandartabweichungBerechnen = True
StandartabweichungStop = 250000
AnzeigeEnd = 10
EndlosWhd = True
WdhEnde = 5000 # wenn endlich, dann Anzahl der Wiederholungen; wenn endlos dann Wiederholungen bis zur Nachricht

# Code
Index = 1
while Index < len(Rangverteilung):
    Rangverteilung[Index] += Rangverteilung[Index-1]
    Index += 1
Weiter = True
GesamtWdh = 0
Wdh = 0
Erfolge = 0
MaxZahl = 0
StandartabweichungBerechnenMerke = StandartabweichungBerechnen
Zahlenhistorie = list()
Zahlenaddition = 0
(ListeZwischenschritte,NotierListe)=ListenErsteller(AnzahlZwischenschritte, Differenz)
Berechnungsvorgang = True
while Berechnungsvorgang:
    while Wdh < WdhEnde:
        Zahl = 0
        Matchesgerechnet = 0
        while Matchesgerechnet < Matches * 6:
            Zahl+=Randomgenerator(Rangverteilung)
            Matchesgerechnet += 1
        while Matchesgerechnet > 0:
            Zahl-=Randomgenerator(Rangverteilung)
            Matchesgerechnet -= 1
        NotierListe=Listenrechner(ListeZwischenschritte, NotierListe, Zahl)
        if Zahl >= Differenz:
            Erfolge += 1
        if Zahl > MaxZahl:
            MaxZahl = Zahl
        if StandartabweichungBerechnen == True:
            Zahlenhistorie.append(Zahl)
            Zahlenaddition += Zahl
            if StandartabweichungStop == GesamtWdh:
                (Durchschnitt,Standartabweichnung)=StandartabweichungRechner(Zahlenhistorie, Zahlenaddition, GesamtWdh)
                StandartabweichungBerechnen = False
        Wdh += 1
        GesamtWdh += 1
    Wdh = 0
    print()
    print()
    print('-----------------------------')
    print()
    print()
    print('Anzahl der Wiederholungen: ' + str(GesamtWdh))
    Index = 0
    while Index < len(NotierListe):
        print('mind. ' + str(ListeZwischenschritte[Index]) + ': ' + str(NotierListe[Index]) + ' (' + str(100*NotierListe[Index]/GesamtWdh)[:AnzeigeEnd] + '%)')
        Index += 1
    print('mind. ' + str(Differenz) + ': ' + str(Erfolge) + ' (' + str(100*Erfolge/GesamtWdh)[:AnzeigeEnd] + '%)')
    print('Höchste Zahl: ' + str(MaxZahl))
    if StandartabweichungBerechnenMerke:
        print()
        if StandartabweichungBerechnen == True:
            (Durchschnitt,Standartabweichung)=StandartabweichungRechner(Zahlenhistorie, Zahlenaddition, GesamtWdh)
        if StandartabweichungStop > GesamtWdh:
            print('Aus ' + str(GesamtWdh) + ' Berechnungen ergibt sich:')
        else:
            print('Aus ' + str(StandartabweichungStop) + ' Berechnungen ergibt sich:')
        print('Durchschnitt: ' + str(Durchschnitt)[:AnzeigeEnd])
        print('Standartabweichung: ' + str(Standartabweichung)[:AnzeigeEnd])
    if not Weiter:
        Berechnungsvorgang = False