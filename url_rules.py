def rule1(url):     #prueft ob in der url ein @ enthalten ist und gibt dementsprechend True oder False aus 
    if "@" in url:
        return True
    else: 
        return False
    
def rule2(url):     #prueft ob http oder https benutzt wird 
    if url[:7] == "http://":
        return True
    else: 
        return False

def rule3(url):     #prueft wie viele Punkte in der URL vorkommen falls es mehr als 5 sind wird es als verdaechtig gesehen
    anzPunkte = url.count(".")
    
    if anzPunkte >= 5:
        return True 
    else:
        return False
    
def pruefeURL(url):     #funktion die alle regeln durchgeht und für jedes True ein punkt addiert 
    punkte_in_flensburg = 0
    if rule1(url) == True:
        punkte_in_flensburg += 1
        print("-Es wurde ein @ in der URL entdeckt!")
    if rule2(url) == True:
        punkte_in_flensburg += 1
        print("-In der URL wird http:// statt https:// verwendet!")
    if rule3(url) == True:
        punkte_in_flensburg += 1 
        print("-Es sind mehr als 4 Punkte in der URL vorhanden!")

    if punkte_in_flensburg < 2:      #falls die url mehr als 1 punkt in flensburg hat ist sie verdaechtig 
        return False 
    else: 
        return True