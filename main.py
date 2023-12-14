#Créé par Enzo Sanchez Valero
#Créé le 14/12/23
#Introduction à Arcade

#Partie 2

from random import randint

class NPC:
    def attribut_aleatoire(self):
        de_un = randint(1, 6)
        de_deux = randint(1, 6)
        de_trois = randint(1, 6)
        de_quatre = randint(1, 6)
        attribut = 0

        if de_un & de_deux & de_trois > de_quatre:
            attribut = de_un + de_deux + de_trois
        elif de_un & de_deux & de_quatre > de_trois:
            attribut = de_un + de_deux + de_quatre
        elif de_un & de_trois & de_quatre > de_deux:
            attribut = de_un + de_trois + de_quatre
        elif de_deux & de_trois & de_quatre > de_un:
            attribut = de_deux + de_trois + de_quatre

        return attribut

    def __init__(self):
        self.force = self.attribut_aleatoire()
        self.agilite = self.attribut_aleatoire()
        self.constitution = self.attribut_aleatoire()
        self.intelligence = self.attribut_aleatoire()
        self.sagesse = self.attribut_aleatoire()
        self.charisme = self.attribut_aleatoire()

        self.classe_armure = randint(1,12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.hp = randint(1,20)
        self.profession = profession

    def afficher_caracteristiques(self):
        print('Force:', self.force)
        print('Agilité:', self.agilite)
        print('Constitution:', self.constitution)
        print('Intelligence:', self.intelligence)
        print('Sagesse:', self.sagesse)
        print('Charisme:', self.charisme)

        print('Classe armure:', self.classe_armure)
        print('Nom:', self.nom)
        print('Race:', self.race)
        print('HP:', self.hp)
        print('Profession:', self.profession)

class Kobold(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        pass

    def subir_dommage(self, dommage):
        self.dommage = randint(1, 6)

class Hero(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        pass

    def subir_dommage(self, dommage):
        self.dommage = randint(1,6)

npc = NPC()
npc.afficher_caracteristiques()


