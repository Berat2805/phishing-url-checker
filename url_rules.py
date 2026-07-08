def rule1(url, begruendung):     #prueft ob in der url ein @ enthalten ist und gibt dementsprechend True oder False aus 
    if "@" in url:
        begruendung["@"] = 1 
    else: 
        begruendung["@"] = 0 
    
def rule2(url, begruendung):     #prueft ob http oder https benutzt wird 
    if url[:7] == "http://":
        begruendung["http"] = 1
    else: 
        begruendung["http"] = 0

def rule3(url, begruendung):     #prueft wie viele Punkte in der URL vorkommen falls es mehr als 5 sind wird es als verdaechtig gesehen
    anzPunkte = url.count(".")
    
    if anzPunkte >= 5:
        begruendung["zu Viele Punkte"] = 1
    else:
        begruendung["zu Viele Punkte"] = 0
    
def rule4(url, begruendung):
    liste_mit_verdaechtigen_woertern = ["login", "signin", "verify", "update", "secure", "account", "password", "bank", "service", "wallet", "transaction"]

    for i in liste_mit_verdaechtigen_woertern:
        if i in url:
            begruendung["verdaechtiges Wort"] = 1
            break
        else:
            begruendung["verdaechtiges Wort"] = 0

def pruefeURL(url):     #funktion die alle regeln durchgeht und für jedes True ein punkt addiert 
    begruendung = {}
    rule1(url, begruendung)
    rule2(url, begruendung)
    rule3(url, begruendung)
    rule4(url, begruendung)

    return begruendung