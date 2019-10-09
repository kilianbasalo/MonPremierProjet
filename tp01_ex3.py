"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1,
              le niveau de risque est faible. Sinon il est élevé.
"""
### Déclaration des variables
age: int
sexe: str
fumeur: str
sport: str
niveau_de_risque: int
### Initialisation des variables
age = 0
sexe = ""
fumeur = ""
sport = ""
niveau_de_risque = 0

### Séquence d'opération
print("Êtes-vous fumeur ? (oui ou non)")
fumeur = str(input())
print("Faîtes-vous du sport ? (oui ou non)")
sport = str(input())
print("Quel est votre sexe ? (h ou f)")
sexe = str(input())
print("Quel est votre âge ?")
age = int(input())
"""Les inputs ci-dessus sont utiles afin d'insérer les données de l'utilisateur.
Suite au calcule ci-dessous, le niveau de risque augmente ou diminue selon les insertions de l'utilisateur.
En effet, si la personne fume, ne fait pas de sport et est une personne agée de sexe masculin il aura un risque plus élevé que si c'est une jeune femme qui ne 
fume pas et fait du sport.
"""

if fumeur == "oui":
    niveau_de_risque += 2
if sport == "oui":
    niveau_de_risque -= 1
if sexe == 'h':
    if age > 50:
        niveau_de_risque += 1
if sexe == 'f':
    if age > 60:
        niveau_de_risque += 1
if niveau_de_risque <= 1:
    print('Niveau de risque faible.')
else:
    print('Niveau de risque élevé.')
