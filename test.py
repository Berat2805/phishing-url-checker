from urllib.parse import urlsplit

def split_host(host_name):
    if host_name is None:
        return
    
    host = host_name.lower()

    for i in [".", "-", "_"]:
        host = host.replace(i, ".")

    teile = host.split(".")

    return teile  

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
            
            if i[0] == x[0] and len(i) == len(x) or i[-1] == x[-1] and len(i) == len(x):
                
                for x , y in zip(i, x):
                    if x != y:
                        zaehler += 1
                
            if zaehler == 1:
                begruendung["Lookalike gefunden"] = 2
                return

url = "https://amazon-s3cure.com/login"
begruendung = {}
url_teile = urlsplit(url)
host_name_url = url_teile.hostname
path_name_url = url_teile.path

rule_lookalike(host_name_url, begruendung)

print(begruendung)