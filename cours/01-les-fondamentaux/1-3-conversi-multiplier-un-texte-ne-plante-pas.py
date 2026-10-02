# ============================================================
# Multiplier un texte ne plante pas
# Module : Les fondamentaux · La moyenne de deux nombres
# Validé le 2026-10-02 dans PyLearn
#
# Énoncé :
#   Une quantité arrive sous forme de texte — c'est ce que rend un
#   formulaire ou un fichier. Écris total_commande(quantite_texte, prix) qui
#   rend le montant total, un nombre.
#
# Refait 7 fois de mémoire, depuis un éditeur vide, sur des données différentes à chaque passage.
# ============================================================

# ------------------------------------------------------------
# Passage 1/7 — 2026-10-02
# Vérifié sur : ("7", 3) → 21 · ("1", 1) → 1 · ("2", 5) → 10
# ------------------------------------------------------------

def total_commande(quantite_texte , prix) :
    return int(quantite_texte) * prix

print(total_commande("7" , 3))


# ------------------------------------------------------------
# Passage 2/7 — 2026-10-02
# Vérifié sur : ("14", 7) → 98 · ("3", 2) → 6 · ("1", 7) → 7
# ------------------------------------------------------------

def total_commande(quantite_texte, prix) :
    return int(quantite_texte) * prix
print(total_commande("14" , 7))


# ------------------------------------------------------------
# Passage 3/7 — 2026-10-02
# Vérifié sur : ("15", 2) → 30 · ("2", 3) → 6 · ("4", 4) → 16
# ------------------------------------------------------------

def total_commande(quantite_texte, prix) :
    return int(quantite_texte) * prix 
print(total_commande("15" , 2))


# ------------------------------------------------------------
# Passage 4/7 — 2026-10-02
# Vérifié sur : ("4", 5) → 20 · ("3", 2) → 6 · ("3", 11) → 33
# ------------------------------------------------------------

def total_commande(quantite_texte, prix) :
    return int(quantite_texte) * prix
print(total_commande("4" , 5))


# ------------------------------------------------------------
# Passage 5/7 — 2026-10-02
# Vérifié sur : ("9", 2) → 18 · ("2", 3) → 6 · ("5", 4) → 20
# ------------------------------------------------------------

def total_commande(quantite_texte, prix) :
    return int(quantite_texte) * prix
print(total_commande("9" , 2 ))


# ------------------------------------------------------------
# Passage 6/7 — 2026-10-02
# Vérifié sur : ("5", 7) → 35 · ("3", 2) → 6 · ("3", 8) → 24
# ------------------------------------------------------------

def total_commande(quantite_texte, prix) : 
    return int(quantite_texte) * prix
print(total_commande("5" , 7))


# ------------------------------------------------------------
# Passage 7/7 — 2026-10-02
# Vérifié sur : ("15", 4) → 60 · ("2", 4) → 8 · ("5", 7) → 35
# ------------------------------------------------------------

def total_commande(quantite_texte, prix) :
    return int(quantite_texte) * prix
print(total_commande("15" , 4))
