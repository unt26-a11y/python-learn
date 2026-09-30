# ============================================================
# Deux lignes qui ne font rien
# Module : Les fondamentaux · La moyenne de deux nombres
# Fait dans PyLearn — publié le 2026-09-30
#
# Énoncé :
#   Écris solde_apres(depart, gain, perte) : le solde de départ, augmenté du
#   gain, diminué de la perte.
#
# J'ai fait cet exercice 7 fois, de mémoire, sur des données différentes
# à chaque passage. Il ne reste que ma dernière version : les 6 essais
# d'avant n'étaient pas encore sauvegardés à ce moment-là.
# ============================================================

def solde_apres(depart, gain, perte) :
    return depart + gain - perte 
calcul = solde_apres(100, 50, 30)
print(calcul)
