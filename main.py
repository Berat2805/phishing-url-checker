import url_rules

eingabe_url = input("Bitte geben sie die URL die sie ueberpruefen moechten ein:")
punkte_in_flensburg = 0

begruendung = url_rules.pruefeURL(eingabe_url)

for i in begruendung:
    if begruendung[i] == 1:
        punkte_in_flensburg += 1
        print(f"Regel {i}: ist ausgeschlagen!!")
    elif begruendung[i] == 0:
        print(f"Regel {i}: ist nicht ausgeschlagen :))")

if punkte_in_flensburg > 1:
    print("Daraus folgt das die gesamte URL verdaechtig ist!")
else:
    print("Daraus folgt das die gesamte URL sicher ist!")