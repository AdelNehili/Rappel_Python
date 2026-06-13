import src.tools as t
from src.tools import generate_values 

#ATTENTION NESTED FUNCTIONS
def exo1_full_pipeline():
    #Cette exercice concentre toutes les notions centrales 
        #parcourir une liste via les indices
        #Créer un dictionnaire via les paires clé-valeur        
    my_keys, my_values = t.generate_list(10)
    my_dico = t.generate_dico(my_keys, my_values)

    for key in my_dico.keys():
        corresponding_value = my_dico[key]
        print(f"Test dico/{key}/{corresponding_value}")

def exo2_list_functions():
    lst = [87,6,83,2,14]
    print(f"lst : {lst}")

    lst.append(76)
    print(f"After : lst.append : {lst}")

    lst.insert(1,90)
    print(f"After : lst.insert : {lst}")

    lst.pop(0)
    print(f"After : lst.pop : {lst}")

    lst.remove(2)
    print(f"After : lst.remove : {lst}")

def exo3_file_access():
    data_path = "data_folder/data.txt"
    t.write_data("On va tous réussir l'exam!",data_path)
    t.append_data("On va tous EXPLOSER l'exam!",data_path)
    all_lines = t.read_data(data_path)

    print(all_lines)

def exo4_try_except():
    #Hehe QUE DEVIENT LE PRINT SI ON OUBLIE LE int() 🙃
    try:
        a = int(input("a : "))
        b = int(input("b : "))
        c = a+b
        print(f"{a}+{b}={c}")
    except ValueError:
        print("ValueError!")
    except TypeError:
        print("TypeError!")
    except ZeroDivisionError:
        print("ZeroDivisionError!")
    except Exception as e:
        print(f"Exception : {e}!")
    finally:
        print("Do i print?")

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

def switch_valeurs():
    a = 10
    b = 30
    print(f"a : {a}/b : {b}")

    temp = a
    a = b
    b = temp
    print(f"a : {a}/b : {b}")
#______________________Attention il faut encore parler de:
    #continue/break/yield/pass
    #Boolean -> And/Or/Xor/Not
    #Math    -> *  /+ /-  /!
    #Bitwise -> &  /| /^  /~

    #Division entière //, Modulo %,

    #Questions fourbes:
        #Que fait None/2 -> TypeError
        #Que fait 2.0==2
        #Que fait lst = [3,5,6,7], lst=lst[::-1]
        #Que fait range(1,10,-1) ->[], mais range(3,1,-1) = [3,2]
        #print(1,2,3,sep="!", end="~")

        #age = 36, pretty_sentence = f"Hello, j'ai {age} ans", print(pretty_sentence)