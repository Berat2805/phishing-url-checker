import url_rules

eingabe_url = input("Bitte geben sie die URL die sie ueberpruefen moechten ein:")

punkte_in_flensburg = 0

begruendung = url_rules.pruefeURL(eingabe_url)

for i in begruendung:
    if begruendung[i] >= 1:
        punkte_in_flensburg += begruendung[i]
        print(f"Regel {i}: ist ausgeschlagen mit {begruendung[i]} Punkten!!")
    elif begruendung[i] == 0:
        print(f"Regel {i}: ist nicht ausgeschlagen :))")

if punkte_in_flensburg >= 4:
    print("Daraus folgt: Die URL ist sehr verdaechtig!")
elif punkte_in_flensburg >= 2:
    print("Daraus folgt: Die URL ist verdaechtig und sollte ueberprueft werden!")
elif punkte_in_flensburg <= 1:
    print("Daraus folgt: Die URL ist sicher!")