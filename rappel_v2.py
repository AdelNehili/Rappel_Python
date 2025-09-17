my_matrix = [[1,2,3],[1,2,3],[1,2,3]]


def decrement_list(my_list,value):
    #Comment itérer sur TOUT les éléments d'une liste
    for i in range(0,len(my_list),1):
        my_list[i] -=value

    print(my_list)

def how_does_modulo_works():
    my_list = [1,2,3,4,5,6,7,8]
    output = [True]*len(my_list)
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            output[i]=True
        elif my_list[i]%2==1:
            output[i]=False
        else:
            print("Am i a joke to you?")
    print(my_list)
    print(output)


"""Comment gérer les shifts?
    0101 1110 1101
    shift de 3 vers la gauche
    shift de 1 vers la droite
    Est- ce que la nouvelle valeur est la meme que la valeur initiale?
"""


def bien_print_matrice(my_matrix):
    for i in range(len(my_matrix)):
        print(my_matrix[i])


def dict_exo():
    #Que se passe-t-il lorsqu'on utilise deux fois la même clef dans le même dictionnaire?
    my_dict = {"PassePartout":12,"PassePasPartout":1,"PasseParDessus":2,"PasseParDessous":3}

    print(my_dict.get("PassezPartout")) #POURQUOI c'est MIEUX d'utiliser la fonction .get() du dict?
    my_dict["PassezPartout"] = 19 
    print(my_dict)

    del my_dict["PasseParDessous"] #delete element
    print(my_dict)

    my_dict["PassezPartout"] +=2 #On peut incrémenter la valeur correspondant à une clef?
    print(my_dict)


    """Rappel : Comment itérer sur TOUT les éléments d'une liste pour comprendre l'itération sur les dictonnaires
        my_list = [10,20,30,40,50,60,70,80]
        for i in range(0,len(my_list),1):
            print(f"{i} : {my_list[i]}")
    """
    for key in my_dict.keys(): #Que return la fonction .keys()? Une liste de clefs
        print(f"{key} : {my_dict[key]}")

    for key,value in my_dict.items(): #Que return la fonction .items()? Une liste de paires clefs/valeurs
        print(f"{key} : {value}")
    

def appel_recursif(param):
    print(f"Stage : {param}")
    if param==0:
        return "Voila!"
    else:
        return appel_recursif(param-1)

res = appel_recursif(5)
print(f"Voici le resultat : {res}")


def try_except():
    try:
        res = 1/0
    except ZeroDivisionError:
        print("ERROR: ZeroDivisionError")
    except:
        print("ERROR: Other")

    print("Choco")


def switch_valeurs():
    a = 10
    b = 30
    print(f"a : {a}/b : {b}")

    temp = a
    a = b
    b = temp
    print(f"a : {a}/b : {b}")


def print_end_param():
    for i in range(5):
        for j in range(10):
            print("C", end='')
        print()

def selectionner_element_dans_matric():
    info = [[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]
    result = ""
    for k in range(0,len(info),1):
        result += str(info[k][1])
    print(result)
