# ============================================================
# Un échange qui perd une valeur en route
# Module : Les fondamentaux · Un 25 qui n'est pas un nombre
# Fait dans PyLearn — publié le 2026-09-30
#
# Énoncé :
#   On a a = 5 et b = 10. Échange leurs contenus : à la fin, a doit valoir
#   10 et b doit valoir 5.
#
# J'ai fait cet exercice 7 fois, de mémoire, sur des données différentes
# à chaque passage. Il ne reste que ma dernière version : les 6 essais
# d'avant n'étaient pas encore sauvegardés à ce moment-là.
# ============================================================

a = 42
b = 24
a ,b = b,a
print(a,b)
