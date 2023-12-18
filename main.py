#Créé par Enzo Sanchez Valero
#Créé le 14/12/23
#Introduction à Arcade
import random
#Partie 2

from random import randint

class NPC:
    def attribut_aleatoire(self):
        de_un = randint(1, 6)
        de_deux = randint(1, 6)
        de_trois = randint(1, 6)
        de_quatre = randint(1, 6)
        attribut = 0

        if de_un > de_quatre and de_deux > de_quatre and de_trois > de_quatre:
            attribut = de_un + de_deux + de_trois
        elif de_un > de_trois and de_deux > de_trois and de_quatre > de_trois:
            attribut = de_un + de_deux + de_quatre
        elif de_un > de_deux and de_trois > de_deux and de_quatre > de_deux:
            attribut = de_un + de_trois + de_quatre
        elif de_deux > de_un and de_trois > de_un and de_quatre > de_un:
            attribut = de_deux + de_trois + de_quatre

        return attribut

    def __init__(self, nom, race, espece, profession):
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
        print('')
        print('Force:', self.force)
        print('Agilité:', self.agilite)
        print('Constitution:', self.constitution)
        print('Intelligence:', self.intelligence)
        print('Sagesse:', self.sagesse)
        print('Charisme:', self.charisme)

        print('Classe armure:', self.classe_armure)
        print('Nom:', self.nom)
        print('Race:', self.race)
        print('Espece:', self.espece)
        print('HP:', self.hp)
        print('Profession:', self.profession)

class Kobold(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        pass

    def subir_dommage(self, dommage):
        if dommage >= self.classe_armure:
            self.hp = self.hp - (dommage - self.classe_armure)

        elif dommage < self.classe_armure:
            pass

        else:
            pass

class Hero(NPC):
    def __init__(self):
        super.__init__()

    def attaquer(self, cible):
        self.attaquer = randint(1,20)
        if self.attaquer == 20:
            pass

        elif self.attaquer == 1:
            print('Attaque ratée')

        elif self.attaquer <= 19 and self.attaquer >= 2:
            self.cible(random.randint(1,6))

        else:
            pass

    def subir_dommage(self, dommage):
        self.dommage = randint(1,6)


npc = NPC('nom', 'race', 'espece', 'profession')
npc.afficher_caracteristiques()

kobold = NPC('nom', 'race', 'espece', 'profession')
kobold.afficher_caracteristiques()
