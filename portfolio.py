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

print(portfolio[0]) #Gibt das gesamte Dictionary der ersten Aktie (AAPL) aus
print(portfolio[0]["name"]) #Gibt den Namen der ersten Aktie (AAPL) aus
print(portfolio[1]["anzahl"]) #Gibt die Anzahl der zweiten Aktie (GOOG) aus

gesamtwert = 0

for aktie in portfolio:
    auflistung = aktie["kaufpreis"] * aktie["anzahl"]
    gesamtwert += auflistung
    print(aktie["name"], "," , auflistung) 

print("Gesamtwert:", gesamtwert)