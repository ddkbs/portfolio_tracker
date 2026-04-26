portfolio = [ #Erstellt eine Liste von Dictionaries, die Informationen über Aktien enthält
    {
        "name": "AAPL", # Name der Aktien kann über portfolio[0]["name"] abgerufen werden
        "kaufpreis": 150.0, # Kaufpreis der Aktien kann über portfolio[0]["kaufpreis"] abgerufen werden
        "anzahl": 7, # Anzahl der Aktien kann über portfolio[0]["anzahl"] abgerufen werden
    },
    {
        "name": "GOOG", # Name der Aktien kann über portfolio[1]["name"] abgerufen werden
        "kaufpreis": 2800.0,
        "anzahl": 2,
    }
]

def berechne_gesamtwert():
    gesamtwert = 0
    einzelwerte = []

    for aktie in portfolio:
        auflistung = aktie["kaufpreis"] * aktie["anzahl"]
        gesamtwert += auflistung
        einzelwerte.append(aktie["name"] + ": " + str(auflistung))

    return gesamtwert, einzelwerte

def zeige_portfolio():
    wert, einzelwerte= berechne_gesamtwert()
    
    for eintrag in einzelwerte:
        print(eintrag)

    print("Gesamtwert:", wert)

zeige_portfolio() 
