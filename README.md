# gps_radius_berechnen
 
Dieser Code ist eine Python-Implementierung, die verwendet werden kann, um zu überprüfen, ob eine geografische Koordinate (Breitengrad und Längengrad) innerhalb eines bestimmten Radius um eine andere Koordinate liegt. Hier ist eine schrittweise Erklärung:

1. **Importieren der math-Bibliothek**: Zuerst importiert der Code die `math`-Bibliothek, die mathematische Funktionen bereitstellt, die später verwendet werden.

2. **Definition der `haversine_distance`-Funktion**: Die Haversine-Formel ist eine Methode, um die Entfernung zwischen zwei Punkten auf einer Kugel (wie der Erde) zu berechnen. Die Funktion `haversine_distance` erhält vier Argumente: die Breitengrade (`lat1`, `lat2`) und Längengrade (`lon1`, `lon2`) der beiden Punkte. Diese Funktion berechnet die Entfernung in Metern zwischen den beiden Koordinaten mithilfe der Haversine-Formel.

3. **Umwandlung von Grad in Bogenmaß**: Da die Haversine-Formel Bogenmaß verwendet, werden die Breiten- und Längengrade der Koordinaten von Grad in Bogenmaß umgewandelt.

4. **Berechnung der Haversine-Formel**: Die Haversine-Formel wird verwendet, um die Entfernung zwischen den beiden Koordinaten in Metern zu berechnen. Dabei werden trigonometrische Funktionen und die Kugelgeometrie genutzt.

5. **Definition der `is_within_radius`-Funktion**: Diese Funktion überprüft, ob eine gegebene Koordinate (`lat2`, `lon2`) innerhalb eines bestimmten Radius (`radius`) um eine andere Koordinate (`lat1`, `lon1`) liegt. Sie nutzt die zuvor definierte `haversine_distance`-Funktion, um die Entfernung zwischen den Koordinaten zu berechnen. Wenn die Entfernung kleiner oder gleich dem Radius ist, wird `True` zurückgegeben, andernfalls wird `False` zurückgegeben.

6. **Hauptprogramm (if __name__ == "__main__")**: Hier werden Beispielkoordinaten (`lat1`, `lon1`) und eine Radiuslänge in Metern (`radius_meters`) festgelegt. Dann wird die `is_within_radius`-Funktion aufgerufen, um zu überprüfen, ob die zweite Koordinate (`lat2`, `lon2`) innerhalb des gegebenen Radius um die erste Koordinate liegt.

7. **Ausgabe der Ergebnisse**: Abhängig davon, ob die Koordinate innerhalb oder außerhalb des Radius liegt, wird eine entsprechende Nachricht auf der Konsole ausgegeben.

Zusammengefasst ermöglicht dieser Code die Überprüfung, ob eine geografische Koordinate innerhalb eines bestimmten Radius um eine andere Koordinate liegt, und gibt entsprechende Ausgaben basierend auf dem Ergebnis aus.