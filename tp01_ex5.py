"""
Programme de calcul du prix d'un billet de cinéma selon plusieurs rabais possible.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais membre : 3chf
    Forfait famille : 1chf
    Carte mensuelle : L'entrée est gratuite

Indications :
    - Il est possible de bénéficier d'un rabais membre et étudiant en même temps
    - Il n'est pas possible de bénéficier d'un rabais famille et étudiant
    - Il est possible de bénéficier d'un rabais membre et famille
    - Il est possible d'avoir une carte mensuelle permettant
      l'accès gratuitement à ce film
    - Si une personne possède la carte membre et étudiante ainsi que le rabais famille,
      le rabais membre et étudiant s'applique (car le rabais étudiant est plus grand)

Contrainte : Si la personne possède la carte mensuelle,
             il ne faut pas lui demander d'autres informations."
"""
### Déclaration des variables
carte_mensuelle : str
carte_membre : str
carte_etudiant : str
forfait_famille : str
prix_a_payer : int
### Initialisation des variables
carte_mensuelle = ""
carte_membre = ""
carte_etudiant = ""
forfait_famille = ""
prix_a_payer = 10
### Séquence d'opération
print("Possédez-vous la carte mensuelle? (oui ou non)")
carte_mensuelle = str(input())
if carte_mensuelle == 'oui':
    print('Le prix a payer est : 0CHF')
else:
    print("Possédez-vous la carte membre? (oui ou non)")
carte_membre = str(input())
print("Possédez-vous la carte étudiante? (oui ou non)")
carte_etudiant = str(input())
print("Bénéficiez-vous du forfait famille? (oui ou non)")
forfait_famille = str(input())

if carte_membre == 'oui':
    if carte_etudiant == 'oui':
        if forfait_famille == 'oui':
            prix_a_payer = prix_a_payer -5
        else:
            prix_a_payer = prix_a_payer -5
    elif carte_etudiant == 'non':
        if forfait_famille == 'oui':
            prix_a_payer = prix_a_payer -4
elif carte_membre == 'non':
    if carte_etudiant == 'oui':
        if forfait_famille == 'oui':
            prix_a_payer = prix_a_payer -2
        if forfait_famille == 'non':
            prix_a_payer = prix_a_payer -2
    if carte_etudiant == 'non':
        if forfait_famille == 'oui':
            prix_a_payer = prix_a_payer -1
        else:
            prix_a_payer = prix_a_payer

print('Le prix a payer est :', (prix_a_payer),' CHF')
