"""
Une compagnie d'assurance automobile propose à ses clients quatre familles
de tarifs identifiables par une couleur, du moins au plus onéreux :
    tarifs bleu, vert, orange et rouge.
Le tarif dépend de la situation du conducteur :
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins
      de deux ans, se voit attribuer le tarif rouge, si toutefois
      il n'a jamais été responsable d'accident.
      Sinon, la compagnie refuse de l'assurer.
    - un conducteur de moins de 25 ans et titulaire du permis depuis
      plus de deux ans, ou de plus de 25 ans mais titulaire du permis
      depuis moins de deux ans a le droit au tarif orange s'il
      n'a jamais provoqué d'accident, au tarif rouge pour un accident,
      sinon il est refusé.
    - un conducteur de plus de 25 ans titulaire du permis depuis plus de
      deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun
      accident et du tarif orange pour un accident, du tarif rouge pour
      deux accidents, et refusé au-delà
    - De plus, pour encourager la fidélité des clients acceptés,
      la compagnie propose un contrat de la couleur immédiatement la plus
      avantageuse s'il est entré dans la maison depuis plus de cinq ans.
      Ainsi, s'il satisfait à cette exigence, un client normalement "vert"
      devient "bleu", un client normalement "orange" devient "vert",
      et le "rouge" devient "orange".

Ecrire l'algorithme permettant de saisir les données nécessaires
(sans contrôle de saisie) et de traiter ce problème.

  Données : - L'Age du conducteur
            - Le nombre d'année de permis
            - Le nombre d'accidents
            - Le nombre d'années d'assurance
  Résultats : Un message spécifiant la situation du client
"""

### Déclaration des variables
age_conducteur : int
nbr_annee_permis : int
nbr_accidents : int
nbr_annee_assurance : int

### Initialisation des variables
age_conducteur = 0
nbr_annee_permis = 0
nbr_accidents = 0
nbr_annee_assurance = 0

### Séquence d'opération
print("Entrez l'âge:")
age_conducteur = int(input())
print("Entrez le nombre d'année de permis:")
nbr_annee_permis = int(input())
print("Entrez le nombre d'accidents:")
nbr_accidents = int(input())
print("Entrez le nombre d'années d'assurance;")
nbr_annee_assurance = int(input())



if age_conducteur < 25:
    if nbr_annee_permis < 2:
        if nbr_accidents == 0:
            if nbr_annee_assurance > 5:
                print('Orange')
            else:
                print('Rouge')
        else:
            print('Assurance refusée')
    elif nbr_annee_permis >= 2:
        if nbr_accidents == 0:
            if nbr_annee_assurance >= 5:
                print('Vert')
            else:
                print('Orange')
        elif nbr_accidents == 1:
            if nbr_annee_assurance >= 5:
                print('Orange')
            else:
                print('Rouge')
        else:
            print('Assurance refusée.')

elif age_conducteur >= 25:
     if nbr_annee_permis < 2:
        if nbr_accidents == 0:
            if nbr_annee_assurance >= 5:
                print('Vert')
            else:
                print('Orange')
        elif nbr_accidents == 1:
            if nbr_annee_assurance >= 5:
                print('Orange')
            else:
                print('Rouge')
     elif nbr_annee_permis >= 2:
         if nbr_accidents == 0:
            if nbr_annee_assurance >= 5:
                 print('Bleu')
            else:
                 print('Vert')
         elif nbr_accidents == 1:
            if nbr_annee_assurance >= 5:
                 print('Vert')
            else:
                 print('Orange')
         elif nbr_accidents == 2:
             if nbr_annee_assurance >= 5:
                 print('Orange')
             else:
                 print('Rouge')
         else:
             print('Assurance refusée')
else:
    print('Indiquation invalide')



