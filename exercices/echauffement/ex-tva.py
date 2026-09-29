# ============================================================
# Exercice : Le panier TTC
# Catégorie : 🔥 Échauffement
# Fait dans PyLearn — publié le 2026-09-29
#
# Énoncé :
#   Un article coûte ht = 150 € hors taxes, avec une TVA de 20 % (tva =
#   0.20).
#   Calcule le prix TTC dans une variable ttc, puis affiche-le. (Attendu :
#   180.0.)
# ============================================================

ht = 150
tva = 0.20

ttc =  ht * (1  + tva  )
print(ttc)
