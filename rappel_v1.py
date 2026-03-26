def exo1():
    #Rappel if-elif-else et if-if
    rempli_lvl = 0

    for i in range(0,15,1):
        rempli_lvl+= i
        #print(f"Pour la combi :\n\ti : {i}\n\trempli_lvl : {rempli_lvl}")
        
        if rempli_lvl==0:
            print("J'AI FAIIIIIIIIIIIIIIIM")
        elif rempli_lvl==1:
            print(".... J'ai faim")
        elif rempli_lvl==2:
            print(".... J'ai un ptit creux")
        elif rempli_lvl==5:
            print(".... J'ai envie de grignoter")
        else:
            print("Besoin de rien, envie de ça")
        
        if rempli_lvl>=5:
            print("Pourquoi je me suis print aussi?")


def and_or_exercise():
    #Rappel sur les priorirités des opérateurs logiques
        #and = *
        #or  = +
            #Donc priorité sur "and" puis sur "or"
        
    print(not((True or False) or not (False and True)))

    hungry_boolean = True
    is_spicy = True
    is_sour = False
    is_sweet = False

    if (is_spicy or is_sour) and hungry_boolean or is_sweet:
        print("Pas de bras")
    else:
        print("pas de chocolats")


def ex_concret(param1,param2):
    #Rappel return : permet de transformer une variable locale à la fonction
        #En une variable utilisable en dehors de la fonction
    result = param1+param2
    return result

def modify_int(value:int):
    #ATTENTION, la modification ne s'est faite que dans la copie du int value
    value+=1


def modify_list(my_list:list,index_to_pop):
    #ATTENTION, la modification a bien modifié la list initiale
    my_list[0]= 999
    

def comparaison_modification_arguments():
    my_value = 15
    my_list  = [9,12,3]
    print(f"""Before:
        -my_value : {my_value}
        -my_list  : {my_list}""")

    modify_int(my_value)
    modify_list(my_list,1)

    print(f"""After:
        -my_value : {my_value}
        -my_list  : {my_list}""")

comparaison_modification_arguments()