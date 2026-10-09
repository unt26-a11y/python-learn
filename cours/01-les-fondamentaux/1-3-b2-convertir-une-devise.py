# ============================================================
# Convertir une devise
# Module : Les fondamentaux · Les nombres et les calculs
# Validé dans PyLearn — mis à jour le 2026-10-09
#
# Énoncé :
#   Le taux de change donne combien vaut un euro en dollars : à 1.08, un
#   euro vaut 1,08 dollar.
#   Écris en_dollars(euros, taux) qui convertit un montant en euros vers des
#   dollars.
#
# Refait 7 fois de mémoire, depuis un éditeur vide, sur des données différentes à chaque passage.
# Puis 5 passages bonus, facultatifs, pour m'entraîner encore — chacun
# sur des données jamais vues.
# ============================================================

# ------------------------------------------------------------
# Passage 1/7 — 2026-10-02
# Vérifié sur : (50, 1.08) → 54 · (0, 1.08) → 0 · (100, 1) → 100
# ------------------------------------------------------------

def en_dollars(euros, taux) :
    return euros * taux
print(en_dollars(50 , 1.08))


# ------------------------------------------------------------
# Passage 2/7 — 2026-10-02
# Vérifié sur : (100, 0.54) → 54 · (3, 3.24) → 9.72 · (50, 3) → 150
# ------------------------------------------------------------

def en_dollars(euros , taux ) :
    return euros * taux
print(en_dollars(100 , 0.54))


# ------------------------------------------------------------
# Passage 3/7 — 2026-10-02
# Vérifié sur : (101, 3.24) → 327.24 · (1, 2.16) → 2.16 · (102, 2) → 204
# ------------------------------------------------------------

def en_dollars( euros , taux ) :
    return euros * taux 
print(en_dollars(101 , 3.24))


# ------------------------------------------------------------
# Passage 4/7 — 2026-10-02
# Vérifié sur : (25, 1.35) → 33.75 · (1, 1.94) → 1.94 · (75, 3) → 225
# ------------------------------------------------------------

def en_dollars(euros , taux ) :
    return euros * taux 
print(en_dollars(25 , 1.35))


# ------------------------------------------------------------
# Passage 5/7 — 2026-10-02
# Vérifié sur : (52, 0.81) → 42.120000000000005 · (1, 1.94) → 1.94 · (201, 2) → 402
# ------------------------------------------------------------

def en_dollars( euros , taux ) :
    return euros * taux 
print(en_dollars(52 , 0.81))


# ------------------------------------------------------------
# Passage 6/7 — 2026-10-02
# Vérifié sur : (38, 1.94) → 73.72 · (1, 2.16) → 2.16 · (51, 4) → 204
# ------------------------------------------------------------

def en_dollars(euros, taux ) :
    return euros * taux 
print(en_dollars(38, 1.94))


# ------------------------------------------------------------
# Passage 7/7 — 2026-10-02
# Vérifié sur : (101, 0.65) → 65.65 · (1, 1.94) → 1.94 · (103, 2) → 206
# ------------------------------------------------------------

def en_dollars(euros , taux) :
    return euros * taux 
print(en_dollars(101 , 0.65))


# ------------------------------------------------------------
# Bonus n°1 (facultatif) — 2026-10-05
# Vérifié sur : (49, 1.33) → 65.17 · (0, 1.35) → 0 · (81, 1) → 81
# ------------------------------------------------------------

def en_dollars(euros, taux) :
    return euros * taux
print(en_dollars(49, 1.33))


# ------------------------------------------------------------
# Bonus n°2 (facultatif) — 2026-10-05
# Vérifié sur : (55, 0.98) → 53.9 · (0, 1.24) → 0 · (121, 1.8) → 217.8
# ------------------------------------------------------------

def en_dollars(euros, taux):
    return euros * taux 
print(en_dollars(55, 0.98))


# ------------------------------------------------------------
# Bonus n°3 (facultatif) — 2026-10-07
# Vérifié sur : (64, 1.43) → 91.52 · (269, 1) → 269 · (0, 0.7) → 0
# ------------------------------------------------------------

def en_dollars(euros, taux) :
    return euros * taux
print(en_dollars(64, 1.43))


# ------------------------------------------------------------
# Bonus n°4 (facultatif) — 2026-10-08
# Vérifié sur : (62, 1.44) → 89.28 · (0, 1.31) → 0 · (199, 1.7) → 338.3
# ------------------------------------------------------------

def en_dollars(euros, taux):
    return euros * taux 
print(en_dollars(62, 1.44))


# ------------------------------------------------------------
# Bonus n°5 (facultatif) — 2026-10-09
# Vérifié sur : (148, 1.5) → 222 · (0, 0.95) → 0 · (64, 1) → 64
# ------------------------------------------------------------

def en_dollars(euros, taux):
    return euros * taux
print(en_dollars(148, 1.5))
