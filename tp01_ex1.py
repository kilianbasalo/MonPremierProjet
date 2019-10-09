"""
Programme testant si une année, saisie par l'utilisateur,est bissextile ou non
  Données : Une année saisie par l'utilisateur
  Indications:
        - Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        - Si elle est multiple de 4, on regarde si elle est multiple de 100.
          - Si c'est le cas, on regarde si elle est multiple de 400.
            - Si c'est le cas, l'année est bissextile.
            - Sinon, elle n'est pas bissextile.
          - Sinon, elle est bissextile.
  Résultats : Un message spécifiant si l'année entrée est bissextile ou non
"""

### Déclaration des variables
chiffre: int
var1: int
var2: int
var3: int
### Initialisation des variables
chiffre = 0
var1 = 4
var2 = 100
var3 = 400
print("Saisissez une année:")
chiffre = int (input())

### Séquence d'opération
### La fonction ci-dessous nous permet dans un premier temps de contrôler si le nombre inséré est un multiple de 4, ensuite nous regardons si il est multiple de 100 et ensuite de 400, Sinon l'année inséré n'est pas bissextile.
if chiffre % var1 == 0:
    if chiffre % var2 == 0:
        if chiffre % var3 == 0:
             print("Elle est bissextile")
        else:
            print("Elle n'est pas bissextile")
    else:
        print("Elle est bissextile")
else:
    print("Elle n'est pas bissextile")
