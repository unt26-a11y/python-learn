# ============================================================
# Juste, tant que la donnée est déjà propre
# Module : Les fondamentaux
# Validé le 2026-10-04 dans PyLearn
#
# Énoncé :
#   Écris presentation(langage) qui rend la phrase J'apprends PYTHON — le
#   nom du langage en capitales, quelle que soit la façon dont il arrive.
#
# Refait 7 fois de mémoire, depuis un éditeur vide, sur des données différentes à chaque passage.
# ============================================================

# ------------------------------------------------------------
# Passage 1/7 — 2026-10-04
# Vérifié sur : ("python") → "J'apprends PYTHON" · ("PYTHON") → "J'apprends PYTHON" · ("Java") → "J'apprends JAVA"
# ------------------------------------------------------------

def presentation(langage):
    return f"J'apprends {langage.upper()}"

print(presentation("python"))


# ------------------------------------------------------------
# Passage 2/7 — 2026-10-04
# Vérifié sur : ("mardi") → "J'apprends MARDI" · ("nord") → "J'apprends NORD" · ("vert") → "J'apprends VERT"
# ------------------------------------------------------------

def presentation(mardi) :
    return f"J'apprends {mardi.upper()}"
print(presentation("mardi"))


# ------------------------------------------------------------
# Passage 3/7 — 2026-10-04
# Vérifié sur : ("nord") → "J'apprends NORD" · ("jaune") → "J'apprends JAUNE" · ("alpha") → "J'apprends ALPHA"
# ------------------------------------------------------------

def presentation(language):
    return f"J'apprends {language.upper()}"
print(presentation("nord"))


# ------------------------------------------------------------
# Passage 4/7 — 2026-10-04
# Vérifié sur : ("jaune") → "J'apprends JAUNE" · ("delta") → "J'apprends DELTA" · ("ouest") → "J'apprends OUEST"
# ------------------------------------------------------------

def presentation(language):
    return f"J'apprends {language.upper()}"
print(presentation("jaune"))


# ------------------------------------------------------------
# Passage 5/7 — 2026-10-04
# Vérifié sur : ("delta") → "J'apprends DELTA" · ("vert") → "J'apprends VERT" · ("jeudi") → "J'apprends JEUDI"
# ------------------------------------------------------------

def presentation(langage):
    return f"J'apprends {langage.upper()}"
print(presentation("delta"))


# ------------------------------------------------------------
# Passage 6/7 — 2026-10-04
# Vérifié sur : ("vert") → "J'apprends VERT" · ("alpha") → "J'apprends ALPHA" · ("sud") → "J'apprends SUD"
# ------------------------------------------------------------

def presentation(vert):
    return f"J'apprends {vert.upper()}"
print(presentation("vert"))


# ------------------------------------------------------------
# Passage 7/7 — 2026-10-04
# Vérifié sur : ("alpha") → "J'apprends ALPHA" · ("ouest") → "J'apprends OUEST" · ("lundi") → "J'apprends LUNDI"
# ------------------------------------------------------------

def presentation(alpha):
    return f"J'apprends {alpha.upper()}" 
print(presentation("alpha"))
