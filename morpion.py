from random import randint



grille = [["?" for i in range(0, 3)][:] for i in range(0, 4)]
etat = "?"
joueur = randint(1, 2)



def afficher(matrice, mode = 0):
    """Affiche la grille"""
    
    trait = "-" * 13
    if mode:
        trait = "-" * 16
    print(trait)
    for i in matrice:
        ligne = "|"
        for h in i:
            ligne += " " + h + " |"
        print(ligne + "\n" + trait)
    print()


def saisir(num):
    """Saisie du jeu"""
    
    case = 0
    symbole = ""
    if num == 1:
        symbole = "X"
    else:
        symbole = "O"
    while 1:
        try:
            case = int(input("Joueur " + str(num) + " (" + symbole + ") : "))
        except ValueError:
            print("il faut un nombre")
            continue
        if case < 1 or case > 12:
            print("il faut un nombre entre 1 et 12")
            continue
        if grille[(case - 1) // 3][(case - 1) % 3] != "?":
            print("il faut une case libre")
            continue
        grille[(case - 1) // 3][(case - 1) % 3] = symbole
        break
    return case

def verifier():
    # lignes
    for i in range(4):
        if grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0] != "?":
            return grille[i][0]
    
    # colonnes
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != "?":
            return grille[0][i]
        elif grille[1][i] == grille[2][i] == grille[3][i] and grille[1][i] != "?":
            return grille[1][i]
    
    # diagonales
    for i in range(2):
        if grille[0 + i][0] == grille[1 + i][1] == grille[2 + i][2] and grille[1 + i][1] != "?":
            return grille[1 + i][1]
        elif grille[0 + i][2] == grille[1 + i][1] == grille[2 + i][0] and grille[1 + i][1] != "?":
            return grille[1 + i][1]
    
    # match nul
    for i in grille:
        for j in i:
            if j == "?":
                return "?"
    
    return "nul"



print("Vous devrez saisir chacun votre tour un numéro de case entre 1 et 12.")
afficher([["1 ", "2 ", "3 "], ["4 ", "5 ", "6 "], ["7 ", "8 ", "9 "], ["10", "11", "12"]], 1)
if joueur == 1:
    print("Le joueur 1 (X) a été tiré au sort pour commencer.")
else:
    print("Le joueur 2 (O) a été tiré au sort pour commencer.")



while True:
    case = saisir(joueur)
    afficher(grille)
    etat = verifier()
    if etat != "?":
        break
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1



if etat == "X":
    print("Le joueur 1 (X) a gagné !")
elif etat == "O":
    print("Le joueur 2 (O) a gagné !")
else:
    print("Match nul")
input()
