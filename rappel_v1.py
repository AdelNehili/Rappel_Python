def exo1():
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
        elif rempli_lvl==6:
            print("Besoin de rien, envie de ça")


def and_or_exercise():
    print(not((True or False) or not (False and True)))

    hungry_boolean = True
    if True or False and hungry_boolean or False:
        print("Pas de bras")
    else:
        print("pas de chocolats")


def ex_concret(param1,param2):
    result = param1+param2
    return result

def modify_value(value):
    value+=1
    return value


my_value = 15
print(f"my_value : {my_value}")
my_value = modify_value(my_value)
print(f"my_value : {my_value}")