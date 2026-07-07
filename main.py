import url_rules

eingabe_url = input("Bitte geben sie die URL die sie ueberpruefen moechten ein:")

if url_rules.pruefeURL(eingabe_url) == True:
    print("\nDie von ihnen eingegeben URL ist verdaechtig!! :(")
elif url_rules.pruefeURL(eingabe_url) == False:
    print("\nDie von ihnen eingegeben URL ist sicher!! :)")
else:
    print("\nFehler Bitte erneut versuchen")