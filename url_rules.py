from urllib.parse import urlsplit

def url_ueberpruefen(url):

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url

def split_host(host_name):
    if host_name is None:
        return []
    
    host = host_name.lower()

    for i in [".", "-", "_"]:
        host = host.replace(i, ".")

    teile = host.split(".")

    return teile        

def rule_at(url, begruendung):     #prueft ob in der url ein @ enthalten ist und gibt dementsprechend True oder False aus 
    if "@" in url:
        begruendung["@"] = 1
    else: 
        begruendung["@"] = 0 
    
def rule_http(url, begruendung):     #prueft ob http oder https benutzt wird 
    if url[:7] == "http://":
        begruendung["http"] = 2
    else: 
        begruendung["http"] = 0

def rule_dots(url, begruendung):     #prueft wie viele Punkte in der URL vorkommen falls es mehr als 5 sind wird es als verdaechtig gesehen
    anzPunkte = url.count(".")
    
    if anzPunkte >= 5:
        begruendung["zu Viele Punkte"] = 2
    else:
        begruendung["zu Viele Punkte"] = 0
    
def rule_words_host(host, begruendung):

    if host is None:
        return
    
    host = host.lower()

    liste_mit_verdaechtigen_woertern = ["login", "signin", "verify", "update", "secure", "account", "password", "bank", "service", "wallet", "transaction", "security", "reset", "support", "scam", "phishing"]
    begruendung["verdaechtiges Wort im Host Namen"] = 0

    for i in liste_mit_verdaechtigen_woertern:
        if i in host:
            begruendung[f"verdaechtiges Wort im Host Namen: {i}"] = 2
            break

def rule_words_path(path, begruendung):

    if path is None:
        return
    
    path = path.lower()
    woerter = []
      
    liste_mit_verdaechtigen_woertern = ["login", "signin", "verify", "update", "secure", "password", "bank", "service", "wallet", "transaction", "reset", "scam", "phishing"]
    begruendung["verdaechtiges Wort im Pfad"] = 0
    zaehler = 0

    for i in liste_mit_verdaechtigen_woertern:
        if i in path:
            zaehler += 1
            woerter.append(i)

    if zaehler >= 2:
        begruendung[f"verdaechtige Woerter im Pfad: {woerter}"] = 1

def rule_number(host_name, begruendung):
    zahlen = ["1","2","3","4","5","6","7","8","9","0"]

    if host_name is None:
        return
    
    begruendung["Zahl im Host Teil der URL"] = 0

    for i in zahlen:
        if i in host_name:
            begruendung["Zahl im Host Teil der URL"] = 1
            break

def rule_lookalike(host_name, begruendung):

    if host_name is None:
        return

    teile = split_host(host_name)

    liste_mit_originalwoerter = ["paypal", "amazon", "login", "secure", "netflix"]

    begruendung["Lookalike gefunden"] = 0

    for x in teile:
        x = x.lower()
        for i in liste_mit_originalwoerter:
            zaehler = 0
            i = i.lower()
            
            if (i[0] == x[0] and len(i) == len(x)) or (i[-1] == x[-1] and len(i) == len(x)):
                
                for x , y in zip(i, x):
                    if x != y:
                        zaehler += 1
                
            if zaehler == 1:
                begruendung["Lookalike gefunden"] = 2
                return

def pruefeURL(url):     #funktion die alle regeln durchgeht und für jedes True ein punkt addiert 
    begruendung = {}
    url = url_ueberpruefen(url)
    url_teile = urlsplit(url)
    host_name_url = url_teile.hostname
    path_name_url = url_teile.path

    rule_at(url, begruendung)
    rule_http(url, begruendung)
    rule_dots(url, begruendung)
    rule_words_host(host_name_url, begruendung)
    rule_words_path(path_name_url, begruendung)
    rule_number(host_name_url, begruendung)
    rule_lookalike(host_name_url, begruendung)

    return begruendung