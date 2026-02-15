import os
import random

def dictionnaire(): #pour récupérer les mots contenus dans le fichier et en faire une liste de mots sans espace ni \n

    if os.path.exists("liste.de.mots.francais.frgut.txt"):

        dictionnaire=[]
        temp=""

        with open("liste.de.mots.francais.frgut.txt","r",encoding="utf-8") as fichier: #je précise l'encodage car si l'encodage du fichier est mal interprete par python ca peut causer erreurs
            mots=fichier.readlines() #donne liste de mots (qui est en fait une liste des lignes du fichier) avec retours à la ligne et/ou espaces

            for mot in mots:
                for caractere in mot:
                    if caractere!=" " and caractere!="\n":
                        temp+=caractere
                    elif temp!="":
                        dictionnaire+=[temp]
                        temp=""
                if temp!="": #reinitialisation de temp à la fin de chaque ligne 
                    dictionnaire+=[temp]
                temp=""

            return dictionnaire
    
    else:
        print("Fichier introuvable, impossible de créer le dictionnaire.")


def normalise():
    accents_a = ["à", "â", "ä"]
    accents_e = ["é", "è", "ê", "ë"] 
    accents_i = ["î", "ï"] 
    accents_o = ["ô", "ö"] 
    accents_u = ["ù", "û", "ü"] 
    accent_c = ["ç"]

    lst=dictionnaire()
    dico=[]
    temp=""

    for i in range(len(lst)):
        dico+=[lst[i].lower()]

    for i in range(len(dico)):
        for j in range(len(dico[i])):
            if dico[i][j] in accents_a:
                temp+="a"
            elif dico[i][j] in accents_e:
                temp+="e"
            elif dico[i][j] in accents_i:
                temp+="i"
            elif dico[i][j] in accents_o:
                temp+="o"
            elif dico[i][j] in accents_u:
                temp+="u"
            elif dico[i][j] in accent_c:
                temp+="c"
            else:
                temp+=dico[i][j]
            
        dico[i]=temp
        temp=""
    
    return dico

def choix_aleatoire(lst):
    return random.choice(lst)

def encodage(mot):
    return "_"*len(mot)


def decodage(secret,affiche,lettre):
    chaine=""
    for i in range(len(affiche)):
        if secret[i]==lettre:
            chaine+=lettre
        else:
            chaine+=affiche[i]
    return chaine

def validite(mot):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return True if mot.lower() in alphabet and len(mot)==1 else False

def suite(reponse):
    positive=["o","oui"]
    reponse_min=reponse.lower()


def pendu():
    dico_normalise=normalise()
    mot_secret=choix_aleatoire(dico_normalise)
    affichage=encodage(mot_secret)

    faux=[] #liste des lettres déjà essayées qui ne sont pas dans le mot
    vrai=[] #liste des lettres dans le mot ayant été trouvées, faux et vrai renvoient msg d'erreur si ils contiennent ce que l'user tape

    nb_vies=7

    print("Bonjour et bienvenue dans mon jeu de pendu! Vas-tu réussir à trouver toutes les lettres secrètes avant que la mort ne t'attrapes?")


    while True:
        print(f"Le mot à décoder est {affichage}")
        print(f"Il te reste {nb_vies} essais avant de mourir!")

        reponse=input("Entre une lettre.").lower()

        if validite(reponse)==False:
            print("Uh-Oh, il faut entrer une lettre, et rien d'autre ;)")
            continue
        if reponse in faux:
            print("Uh-oh, tu as déjà essayé cette lettre..Elle n'est pas dans le mot!")
            continue
        if reponse in vrai:
            print("Tu as déjà trouvé cette lettre!")
            continue

        if reponse in mot_secret:
            affichage=decodage(mot_secret,affichage,reponse)
            vrai+=[reponse]

            if mot_secret==affichage:
                print(f"Félicitations, mission accomplie! Le mot à trouver était {mot_secret} !")
                refaire=input("Veux-tu rejouer ?")
                if refaire.lower() in ["oui","o"]:
                    return pendu()
                else:
                    print("Merci d'avoir joué et à bientôt!")
                    break
            else:
                print("Bonne réponse!")
                continue            
    
        else: #la reponse n'est pas dans le mot
            nb_vies-=1
            if nb_vies==0:
                print(f"Uh-oh..tu as perdu toutes tes vies. Mission échouée! Le mot à trouver était {mot_secret}")
                refaire=input("Veux-tu rejouer et retenter ta chance?")
                if refaire.lower() in ["oui","o"]:
                    return pendu()
                else:
                    print("Merci d'avoir joué et à bientôt!")
                    break

            else:
                faux+=[reponse]
                print("Mauvaise réponse !")
                continue

           
                

        

    


#pendu()
#faire docstring pour chaque fonction