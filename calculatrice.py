def calcul(a,b,signe):
    if signe=="+":
            return(a+b)
            
    elif signe=="-":
            return(a-b)

    elif signe=="x":
            return(a*b)
        
    elif signe=="/":
        if b==0:
             return "Division par 0 impossible !"
        else:
            return(a/b)
        
    elif signe=="%":
            return(a%b)




def calculatrice():

    operation=["+","-","x","/","%"]

    print("Bonjour et bienvenue à toi !😊")

    while True:

        while True:
            signe=input("""Entre + pour effectuer une addition,
                            - pour une soustraction,
                            x pour une multiplication,
                            / pour une division,
                            et % pour connaître le reste d'une division""")
            
            if signe not in operation:
                print("Uh-oh, ton signe d'operation ne semble pas valide!")
                continue
            break


        while True:
            try:
                nombre1=int(input("Entre la première opérande"))
            except ValueError:
                print("Uh-oh...il faut entrer un nombre! 😉")
                continue
            break

        while True:
            try:
                nombre2=int(input("Entre la seconde opérande"))
            except ValueError:
                print("Bien tenté..mais il faut entrer un nombre!😉 ")
                continue

            if signe=="/" and nombre2==0:
                print("Division par 0 impossible!")
                continue
            break

   

        print(f"Le resultat de {nombre1} {signe} {nombre2} est {calcul(nombre1,nombre2,signe)}")

        reponse=input("Veux-tu effectuer un autre calcul ?")

        if reponse.lower() not in ["oui","o"]:
            print("Merci d'avoir utilisé ma calculatrice et à bientôt 😎")
            break




#ajouter ouais, yes, y dans la liste des rep positives pour reutiliser calculatrice