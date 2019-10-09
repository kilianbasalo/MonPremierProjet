"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration des variables
selection: int
montant: float
num_sandwich: int
num_chips: int
num_chocolat: int
num_bonbons: int
num_tea: int
num_limonade: int

prix_sandwich: float
prix_chips: float
prix_chocolat: float
prix_bonbons: float
prix_tea: float
prix_limonade: float

###Initialisation des variables
selection = 0
montant = 0
num_sandwich = 1
num_chips = 2
num_chocolat = 3
num_bonbons = 4
num_tea = 5
num_limonade = 6

prix_sandwich = 4.90
prix_chips = 2.50
prix_chocolat = 2.00
prix_bonbons = 3.30
prix_tea = 2.20
prix_limonade = 1.90

### Séquence d'opération
### Les prints servent à ce que l'utilisateur puisse voir quel numéro correspond à quel produit.
print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")
print("----------------------------------------------")
print("Veuillez insérer la monnaie ci-dessous")
montant = float(input())
### Les inputs sont utilisés afin que l'utilisateur puisse insérer le montant et le produit de son choix.
print("----------------------------------------------")
print("Veuillez indiquer le numéro de l'article souhaité.")
selection = int(input())

"""
J'ai utilisé les if par produit et ensuite selon les divers possibilités. Les calculs sont toujours les mêmes pour chaque produit.
En effet, si le montant est inférieur au prix du produit séléctrionné alors le message Montant insuffisant s'affiche.
Ensuite j'effectue le calcule afin de savoir combien le distributeur va devoir rendre à l'utilisateur.
J'ai du également utiliser les rounds afin d'arrondir le rendu.
Comme vous le verrez le Else en bas de feuille est utile si la personne selection un numero de produit ne correpondant à aucun produit.
"""
if selection == num_sandwich:
    if montant >= prix_sandwich:
        print("Transaction confirmée.")
        if montant - prix_sandwich >= 0:
            print("Veuillez prendre votre retour de", round(montant - prix_sandwich, 3), " CHF")
            print("Veuillez également prendre votre Sandwich au poulet et nous vous souhaitons un bon appétit.")
    elif montant < prix_sandwich:
        print("Montant insuffisant")

if selection == num_chips:
    if montant >= prix_chips:
        print("Transaction confirmée")
        if montant - prix_chips >= 0:
            print("Veuillez prendre votre retour de", round(montant - prix_chips, 3), " CHF")
            print("Veuillez également prendre vos Chips Paprika et nous vous souhaitons un bon appétit.")
    elif montant < prix_chips:
        print("Montant insuffisant")

if selection == num_chocolat:
    if montant >= prix_chocolat:
        print("Transaction confirmée")
        if montant - prix_chocolat >= 0:
            print("Veuillez prendre votre retour de", round(montant - prix_chocolat, 3), " CHF")
            print("Veuillez également prendre votre barre chocolatée et nous vous souhaitons un bon appétit.")
    elif montant < prix_chocolat:
        print("Montant insuffisant")

if selection == num_bonbons:
    if montant >= prix_bonbons:
        print("Transaction confirmée")
        if montant - prix_bonbons >= 0:
            print("Veuillez prendre votre retour de", round(montant - prix_bonbons, 3), " CHF")
            print("Veuillez également prendre vos bonbons et nous vous souhaitons un bon appétit.")
    elif montant < prix_bonbons:
        print("Montant insuffisant")

if selection == num_tea:
    if montant >= prix_tea:
        print("Transaction confirmée")
        if montant - prix_tea >= 0:
            print("Veuillez prendre votre retour de", round(montant - prix_tea, 3), " CHF")
            print("Veuillez également prendre votre Thé froid et nous vous souhaitons un bon appétit.")
    elif montant < prix_tea:
        print("Montant insuffisant")

if selection == num_limonade:
    if montant >= prix_limonade:
        print("Transaction confirmée")
        if montant - prix_limonade >= 0:
            print("Veuillez prendre votre retour de", round(montant - prix_limonade, 3), " CHF")
            print("Veuillez également prendre votre Limonade et nous vous souhaitons un bon appétit.")
    elif montant < prix_limonade:
        print("Montant insuffisant")

else:
    print('Selection invalide.')
