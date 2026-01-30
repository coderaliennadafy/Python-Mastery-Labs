
# 1. Création de la classe Voiture
class Voiture:
    nombre_de_vehicules = 0  # Attribut de classe pour compter les voitures

    def __init__(self, matricule):
        self.matricule = matricule
        Voiture.nombre_de_vehicules += 1  

    def __str__(self):
        # info about car
        return f"Voiture (Matricule: {self.matricule} )"

# 3 & 4. Création de la classe Parking et son constructeur
class Parking:
    def __init__(self, capacite):
        self.capacite = capacite  
        self.voitures = []        

    # 5. Méthode pour ajouter une voiture
    def ajouter_voiture(self, voiture):
        if len(self.voitures) < self.capacite:
            self.voitures.append(voiture)
            print(f"Voiture {voiture.matricule} ajoutée au parking.")
        else:
            print(" Erreur : Le parking est plein !")

    # 6. Méthode pour retirer une voiture par son matricule
    def retirer_voiture(self, matricule):
    # search about car in th list
        for v in self.voitures:
            if v.matricule == matricule:
              self.voitures.remove(v) #remove
              print(f"Retirée {matricule}")
              return 
        print(" Non trouvée")
    # 7. Méteode pour retourner le nombre de places disponibles
    def places_disponibles(self):
        return self.capacite - len(self.voitures)

    # 8. Méthode pour afficher les voitures garées
    def afficher_voitures(self):
        if not self.voitures:
            print("Le parking est vide.")
        else:
            print(" Liste des voitures garées :")
            for v in self.voitures:
                print(v)

# 9. TEST DU SYSTÈME
print("Test du Système de Gestion de Parking")

#creat parking for 2 place
mon_parking = Parking(2)

# creation and add car
v1 = Voiture("ABC-123")
v2 = Voiture("DEF-456")
v3 = Voiture("GHI-789")

mon_parking.ajouter_voiture(v1)
mon_parking.ajouter_voiture(v2)
mon_parking.ajouter_voiture(v3)

#afficher la voilture qui parke
mon_parking.afficher_voitures()

#ikhraj voiture par ce matrucule
mon_parking.retirer_voiture("DEF-456")

mon_parking.afficher_voitures()

def get_capacite(self):
    return self.__capacite

def set_capacite(self, capacite):
    if capacite > 0:
        self.__capacite = capacite
    else:
        print(" Erreur : La capacité doit être supérieure à zéro.")

print(f"Places restantes : {mon_parking.places_disponibles()}")
print(f" Nombre total de voitures créées dans le système : {Voiture.nombre_de_vehicules}")
