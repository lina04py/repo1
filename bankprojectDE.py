__author__ = "lina04py"

# Dieses Programm berechnet die IBAN und die Prüfsumme der Person,
# die ihre Bankleitzahl und ihre Kontonummer eingibt.

# 1. Das Programm nimmt die Bankleitzahl und die Kontonummer des Benutzers:

BLZ = input("Bitte geben Sie Ihre 8-stellige Bankleitzahl ein: ")
if not BLZ.isdigit():
    raise ValueError("BLZ darf nur Zahlen enthalten.")
BLZ = BLZ.zfill(8)
konto = input("Bitte geben Sie Ihre 10-stellige Kontonummer ein: ")
if not konto.isdigit():
    raise ValueError("Kontonummer darf nur Zahlen enthalten.")
konto = konto.zfill(10)

# 2. Es erfolgt die Erstellung der Länderkennung "DE":

laenderkennung = "DE"

# 3. Die IBAN wird mit einem Platzhalter für die
# später berechnete Prüfsumme vorbereitet:

iban_mit_platzhalter = BLZ + konto + "131400"

# Erklärung:
# - Länderkennung "DE" wird umgewandelt: D = 13, E = 14.
# - Allgemein wird angefangen bei A = 10 und aufgehört bei Z = 35.
# - Der Platzhalter "00" ist bereits in der Umwandlung (DE → 1314) enthalten.
# - Reihenfolge: (BLZ + Konto + DE00)

# 4. Modulo 97 berechnen, um den Rest für die Berechnung der Prüfsumme zu erhalten:
rest = int(iban_mit_platzhalter) % 97

# 5. Prüfsumme berechnen:
pruefsumme_berechnet = 98 - rest

# 6. Wenn die Prüfsumme einstellig ist, mit 0 auffüllen:
pruefsumme_berechnet = str(pruefsumme_berechnet).zfill(2)

# 7. Vollständige IBAN zusammensetzen:
iban_voll = laenderkennung + pruefsumme_berechnet + BLZ + konto

# 8. Ausgabe
print("\n-----------------------------------")
print("Berechnete IBAN:")
print(iban_voll)
print("-----------------------------------")
print("Erläuterung:")
print(f"Länderkennung: {laenderkennung}")
print(f"Prüfsumme: {pruefsumme_berechnet}")
print(f"Bankleitzahl: {BLZ}")
print(f"Kontonummer: {konto}")
print("Berechnungsverfahren:")
print("1. Länderkennung (DE) wird durch Zahlen ersetzt (D=13, E=14).")
print("2. Diese Zahlen werden hinter BLZ und Kontonummer gestellt.")
print("3. Es ergibt sich: (BLZ + Konto + 131400).")
print("4. Diese Zahl wird modulo 97 gerechnet.")
print("5. Prüfsumme = 98 - (Zahl mod 97).")
print("6. Ergebnis ist die vollständige IBAN.")
