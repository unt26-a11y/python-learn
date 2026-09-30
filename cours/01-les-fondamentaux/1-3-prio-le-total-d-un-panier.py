# ============================================================
# Le total d'un panier
# Module : Les fondamentaux · La moyenne de deux nombres
# Fait dans PyLearn — publié le 2026-09-30
#
# Énoncé :
#   Écris total_panier(prix_unitaire, quantite, frais) : le coût de quantite
#   articles au prix unitaire donné, plus les frais de livraison (une seule
#   fois, pas par article).
#
# Refait 7 fois de mémoire, depuis un éditeur vide, sur des données différentes à chaque passage.
# ============================================================

# ------------------------------------------------------------
# Passage 1/7 — 2026-09-30
# Vérifié sur : (10, 3, 5) → 35 · (10, 3, 0) → 30 · (0, 5, 7) → 7
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais):
    return prix_unitaire * quantite + frais
total = total_panier(10, 3, 5)
print(total)


# ------------------------------------------------------------
# Passage 2/7 — 2026-09-30
# Vérifié sur : (12, 2, 7) → 31 · (12, 7, 1) → 85 · (1, 10, 14) → 24
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais) :
    return prix_unitaire * quantite + frais
total = total_panier(12, 2, 7 ) 
print(total)
#31


# ------------------------------------------------------------
# Passage 3/7 — 2026-09-30
# Vérifié sur : (12, 2, 7) → 31 · (12, 6, 3) → 75 · (2, 6, 8) → 20
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais) :
    return  prix_unitaire * quantite + frais
total = total_panier(12,2,7)


# ------------------------------------------------------------
# Passage 4/7 — 2026-09-30
# Vérifié sur : (12, 6, 11) → 83 · (12, 7, 4) → 88 · (3, 4, 10) → 22
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais) :
    return prix_unitaire * quantite + frais
total = total_panier(12,6,11)
print(total)


# ------------------------------------------------------------
# Passage 5/7 — 2026-09-30
# Vérifié sur : (12, 2, 11) → 35 · (8, 7, 3) → 59 · (2, 4, 10) → 18
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais) :
    return prix_unitaire * quantite + frais
prix = total_panier(12,2,11)
print(prix)


# ------------------------------------------------------------
# Passage 6/7 — 2026-09-30
# Vérifié sur : (14, 4, 8) → 64 · (13, 6, 3) → 81 · (3, 8, 10) → 34
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais):
    return prix_unitaire * quantite + frais
prix = total_panier(14, 4, 8)
print(prix)


# ------------------------------------------------------------
# Passage 7/7 — 2026-09-30
# Vérifié sur : (14, 4, 8) → 64 · (14, 7, 4) → 102 · (4, 7, 13) → 41
# ------------------------------------------------------------

def total_panier(prix_unitaire, quantite, frais):
    return prix_unitaire * quantite + frais
prix= total_panier(14, 4, 8)
print(prix)
