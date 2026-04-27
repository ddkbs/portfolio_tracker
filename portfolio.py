import json
portfolio = [] # Leere Liste wird erstellt, um die Aktien zu speichern

def speichere_portfolio(): #Funktion wird erstellt, um das Portfolio in einer JSON-Datei zu speichern
    with open("portfolio.json", "w") as datei: # Öffnet die Datei "portfolio.json" im Schreibmodus ("w") und weist sie der Variablen "datei" zu
        json.dump(portfolio, datei) # Die Funktion json.dump() wird verwendet, um die Daten aus der "portfolio"-Liste in die geöffnete Datei zu schreiben. Das Portfolio wird als JSON-Format gespeichert.

def lade_portfolio(): #Funktion wird erstellt, um das Portfolio aus einer JSON-Datei zu laden
    global portfolio # Die Variable "portfolio" wird als global deklariert, damit sie innerhalb der Funktion geändert werden kann
    try: # Try-Except Block wird verwendet, um Fehler beim Laden der Datei zu behandeln
        with open("portfolio.json", "r") as datei: # Öffnet die Datei "portfolio.json" im Lesemodus ("r") und weist sie der Variablen "datei" zu
            portfolio = json.load(datei) # Die Funktion json.load() wird verwendet, um die Daten aus der geöffneten Datei zu lesen und in die Variable "portfolio" zu laden. Das Portfolio wird als JSON-Format erwartet.
    except FileNotFoundError: # Wenn die Datei "portfolio.json" nicht gefunden wird, wird eine FileNotFoundError-Ausnahme ausgelöst. In diesem Fall wird die "portfolio"-Liste auf eine leere Liste gesetzt, um sicherzustellen, dass das Programm weiterhin funktioniert, auch wenn die Datei nicht existiert.
        portfolio = [] # Wenn die Datei nicht gefunden wird, wird die "portfolio"-Liste auf eine leere Liste gesetzt

lade_portfolio() #Funktion wird ausgeführt, um das Portfolio zu laden, bevor neue Aktien hinzugefügt werden

def aktie_hinzufuegen(): #Funktion für das Hinzufügen von Aktien wird erstellt
    while True: #While Schleife, um mehrere Aktien hinzuzufügen
        name = input("Name der Aktie: ") #Eingabe für den Namen der Aktie
        kaufpreis = float(input("Kaufpreis der Aktie: ")) #Eingabe für den Kaufpreis der Aktie, wird in float umgewandelt
        anzahl = int(input("Anzahl der Aktien: ")) #Eingabe für die Anzahl der Aktien, wird in int umgewandelt
        portfolio.append({"name": name, "kaufpreis": kaufpreis, "anzahl": anzahl}) #Die Informationen der Aktie werden als Dictionary in die Portfolio-Liste hinzugefügt
        eingabe = input("Weiter? (j/n): ") #Eingabe, ob weitere Aktien hinzugefügt werden sollen
        if eingabe == "n": #Wenn n (Nein) dann endet Eingabe
            break

aktie_hinzufuegen() #Funktion wird ausgeführt, um Aktien hinzuzufügen

def berechne_gesamtwert(): #Funktion wird erstellt
    gesamtwert = 0 #Variable erstellt
    info_positionen = [] #Liste erstellt

    for aktie in portfolio:
        wert_berechnung = aktie["kaufpreis"] * aktie["anzahl"] #Berechnung des Wertes
        gesamtwert += wert_berechnung # Gesamtwert wird mit jedem Durchgang um wert der aktuellen Aktie erhöt
        info_positionen.append(aktie["name"] + ": " + str(wert_berechnung)) # Informationen werden in Liste gespeichert

    return gesamtwert, info_positionen # Funktion gibt Gesamtwert und Informationen zurück

def zeige_portfolio(): #Funktion wird erstellt
    wert, info_positionen = berechne_gesamtwert() # wert wird gesamtwert zugewiesen, info_positionen werden die Informationen zugewiesen
    
    for eintrag in info_positionen: #Einträge in Info_positionen werden durchlaufen
        print(eintrag) #Einträge werden ausgegeben

    print("Gesamtwert:", wert) #Gesamtwert wird ausgegeben

speichere_portfolio() #Funktion wird ausgeführt
zeige_portfolio() #Funktion wird ausgeführt
