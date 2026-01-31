class Livre:
    def __init__(self, titre):
        self.titre = titre
        self.disponible = True


class Membre:
    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.disponible:
            livre.disponible = False
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté '{livre.titre}'")
        else:
            print(f"le livre '{livre.titre}' n'est pas disponible")

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)
            livre.disponible = True
            print(f"{self.nom} a retourné '{livre.titre}'")
        else:
            print(f"{self.nom} n'a pas emprunté '{livre.titre}'")

    def afficher_infos(self):
        print(f"membre: {self.nom}")
        print("livres empruntés:")
        if self.livres_empruntes:
            for livre in self.livres_empruntes:
                print(f" - {livre.titre}")
        else:
            print("aucun livre emprunté")


def gestionnaire_bibliotheque():
    livre1 = Livre("python")
    livre2 = Livre("algorithmique")

    nom = input("donner le nom du membre: ")
    membre = Membre(nom)

    while True:
        print("menu")
        print("1 - emprunter un livre")
        print("2 - retourner un livre")
        print("3 - afficher infos membre")
        print("4 - quitter")

        choix = input("Votre choix: ")

        if choix == "1":
            print("1 - python")
            print("2 - algorithmique")
            c = input("choisir livre: ")

            if c == "1":
                membre.emprunter_livre(livre1)
            elif c == "2":
                membre.emprunter_livre(livre2)
            else:
                print("choix invalide")

        elif choix == "2":
            print("1 - python")
            print("2 - algorithmique")
            c = input("choisir livre à retourner: ")

            if c == "1":
                membre.retourner_livre(livre1)
            elif c == "2":
                membre.retourner_livre(livre2)
            else:
                print("choix invalide")

        elif choix == "3":
            membre.afficher_infos()

        elif choix == "4":
            print(f"au revoir {membre.nom}")
            break

        else:
            print("choix invalide")


gestionnaire_bibliotheque()
