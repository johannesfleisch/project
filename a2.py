#!/usr/bin/env python
"""
Aufgabe 2: Pythonskripts
"""

# Eingabe der Länge und Breite mittels input() und einer Typkonvertierung
L = int(input("Geben Sie die Länge ein: "))
B = int(input("Geben Sie die Breite ein: "))

# Flächeninhalt und Umfang als Variablen definieren
A = L*B
U = 2*(L+B)

# Ausgabe eines Antwortsatzes für Flächeninhalt und Umfang
print("Der Flächeninhalt des Rechtecks beträgt: {} m²".format(A))
print("Der Umfang des Rechtecks beträgt: {} m".format(U))
