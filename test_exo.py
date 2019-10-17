"""
Explication du programme:

-boucle sur la liste des coordonnees de 1 a 10 000 cela sera le point 1 choisi.
-on reproduit la meme chose pour obtenir le point 2 (cela permet de tester tous les points).
-calcul de la difference X et Y entre le point 2 et le point 1.
-on calcule le point 3 et on le cherche dans la liste.
-on calcule le point 4 et on le cherche dans la liste.
-on imagine un point1bis, on le calcul, si point1bis est egal au point1 alors ses 4 points forme un carre.
-on recupere les coordonnees de tous ses points ainsi que la difference pour verifier manuellement si besoin.
-on annonce le nombre de carre total.
                    -----------
Temps estime pour compiler le programme: 5 Heures.
Total de calcul environ: 10 000**4 = 1e16.
Total de carre: 224.
"""

filepath = 'exercice.txt'
liste = []

nbCarre = 0
cnt_nbLigne = 0

with open(filepath) as fp:
    line = fp.readline()
    while line:
        line_split = line.split()
        liste.append((int(line_split[0]), int(line_split[1])))
        line = fp.readline()

# Boucle 1-10 000 Point1
for point1 in liste:
    cnt_nbLigne = cnt_nbLigne + 1
    print(cnt_nbLigne, '/10000')

    # Boucle 1-10 000 Point2
    for point2 in liste:

        if point2 != point1:
            # Diference X
            valeur1 = point2[0] - point1[0]
            # Diference Y
            valeur2 = point2[1] - point1[1]
            # Point3
            point3 = (point2[0] + valeur2, point2[1] - valeur1)

            if liste.count(point3) > 0:
                # Point4
                point4 = (point3[0] - valeur1, point3[1] - valeur2)
                print('2')

                if liste.count(point4):
                    # Point1bis
                    point1bis = (point4[0] - valeur2, point4[1] + valeur1)
                    print('3')

                    if liste.count(point1bis) > 0:
                        if point1bis == point1:
                            nbCarre = nbCarre + 1
                            print('SQUARE')
                            print ('P1:', point1)
                            print ('P2:', point2)
                            print ('P3:', point3)
                            print ('P4:', point4)
                            print ('Valeur1:', valeur1)
                            print ('Valeur2:', valeur2)

print ('Il y a', nbCarre, 'carre')
