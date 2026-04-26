portfolio = []

def aktie_hinzufuegen():
    while True:
        name = input("Name der Aktie: ")
        kaufpreis = float(input("Kaufpreis der Aktie: "))
        anzahl = int(input("Anzahl der Aktien: "))
        portfolio.append({"name": name, "kaufpreis": kaufpreis, "anzahl": anzahl})
        eingabe = input("Weiter? (j/n): ")
        if eingabe == "n":
            break
aktie_hinzufuegen() #Funktion wird ausgeführt, um eine Aktie hinzuzufügen

def berechne_gesamtwert(): #Funktion wird erstellt
    gesamtwert = 0 #Variable erstellt
    info_positionen = [] #Liste erstellt

    for aktie in portfolio:
        wert_berechnung = aktie["kaufpreis"] * aktie["anzahl"] #Berechnung des Wertes
        gesamtwert += wert_berechnung # Gesamtwert wird mit jedem Durchgang um wert der aktuellen Aktie erhöt
        info_positionen.append(aktie["name"] + ": " + str(wert_berechnung)) # Informationen werden in Liste gespeichert

    return gesamtwert, info_positionen # Funktion gibt Gesamtwert und Informationen zurück

def zeige_portfolio(): #Funktion wird erstellt
    wert, info_positionen= berechne_gesamtwert() # wert wird gesamtwert zugewiesen, info_positionen werden die Informationen zugewiesen
    
    for eintrag in info_positionen: #Einträge in Info_positionen werden durchlaufen
        print(eintrag) #Einträge werden ausgegeben

    print("Gesamtwert:", wert) #Gesamtwert wird ausgegeben

zeige_portfolio() #Funktion wird ausgeführt
