#type var
my_int = 12
my_float = 1.2
my_boolean = False
my_string = f"hehe j'ai vu {my_int} chat{'s' if my_int >= 2 else ''}" #One-Liner
#Operators
def operator_exo(a:int, b:int = 9):
    my_modulo = a%b #reste de la division
    my_div = a/b
    my_full_div = a//b
    my_full_div_equivalent = int(a/b)

    my_mult = a*b
    my_power = a**b
    pretty_sentence = f"""Pour a = {a} et b = {b}:
        -a%b = {my_modulo}
        -a/b = {my_div}
        -a//b = {my_full_div}
        -int(a/b) = {my_full_div_equivalent}
        -a*b = {my_mult}
        -a**b = {my_power}
    """
    print(pretty_sentence)
def call_operator_exo():
    operator_exo(3,7) #assignation automatique
    operator_exo(a=3,b=7) #assignation manuelle
    operator_exo(b=7,a=3) #assignation manuelle
    operator_exo(3) #assignation manpar défaut

#Operators with strings
def operator_str_exo(a:str= "chat", b:str= "tortue", mult:int= 25):   
    my_concat = a+" "+b
    my_str_repetition = a+"_"*mult+b
    pretty_sentence = f"""Pour a = {a}, b = {b} et mult = {mult}:
        -a+" "+b = {my_concat}
        -a+"_"*{mult}+b = {my_str_repetition}
    """
    print(pretty_sentence)    
def call_operator_str_exo():
    operator_str_exo("Poule", "Poussin",20) #assignation automatique
    operator_str_exo(a="Poule", b="Poussin",mult=20) #assignation manuelle
    operator_str_exo(mult=20,b="Poule", a="Poussin") #assignation automatique

#Bitwise operators
def bitwise_operators_exo():
    a = 0b11011
    b = 0b00001

    print(f"a : {a}")
    print(f"b : {b}")
    my_NOT = ~a #Symbol : ~
    my_AND = a&b #Symbol : &
    my_NAND = ~(a&b) #Symbol : ~& = NOT AND
    my_OR = a|b #Symbol : |
    my_NOR = ~(a|b) #Symbol : ~|
    my_XOR = a^b #Symbol : ^


    my_Left_Shift = a<<b #Symbol : <<
    my_Right_Shift = a>>b #Symbol : >>
    pretty_sentence = f"""Pour a = {a} et b = {b}:
        A CONNAITRE:
            -my_AND = {my_AND}
            -my_OR = {my_OR}
            -my_XOR = {my_XOR}
            -my_Left_Shift = {my_Left_Shift}
            -my_Right_Shift = {my_Right_Shift}

        BONUS:
            -my_NOT = {my_NOT}
            -my_NAND = {my_NAND}
            -my_NOR = {my_NOR}
        """
    print(pretty_sentence)

#Statements (if/elif/else)
def if_statements_exo():
    #ATTENTION : SI PLUSIEURS IF S'ENCHAINENT, on les lit TOUS!
    #          : SI on a IF/ELIF/ELSE, on s'arrete au PREMIER CORRECT!!
    a = True
    b = False
    if a == True:
        print("First!")

    if (a and b):
        print("Second!")
    elif (a or b):
        print("Third!")
    else:
        print("Fourth!")

#Data Architecture - List, Tuple, Dictionary
my_dict = {"chaussures" : 3,
        "lettres" : 6,
        "vestes" : 4,
        "chats" : 3}

#List : ATTENTION UNE LISTE COMMENCE A L'INDICE ZEROOOOOOOOOOO
def exo_archi():
    my_list = [12,3,4,5.67,89,0]
    index = 0
    pretty_sentence = f"""Pour index = {index}:
        my_list[{index}] = {my_list[index]}
    """
    print(pretty_sentence)

    for i in range(0,len(my_list),1):
        print(f"my_list[{i}] = {my_list[i]}")

    for i in range(-2,4,1):
        print(f"my_list[{i}] = {my_list[i]}")

    #Tuple : ATTENTION, ON NE PEUT PAS LES MODIFIER
    my_tuple = (12,3,4,5.67,89,0)
    my_complete_copy_tuple = my_tuple[0:len(my_tuple)]
    my_partial_copy_tuple = my_tuple[2:5]
    my_modified_tuple = my_tuple[0:3]+(999,)+my_tuple[5:] #ATTENTION : A UN DETAIL

    pretty_sentence = f"""Pour my_tuple = {my_tuple}:
        my_complete_copy_tuple = {my_complete_copy_tuple}
        my_partial_copy_tuple = {my_partial_copy_tuple}
        my_modified_tuple = {my_complete_copy_tuple}
    """
    print(pretty_sentence)


#WRITING/READING/APPENDING

with open("temp_1.txt","r") as file_reader:
    for line in file_reader.readlines():
        print(line)

with open("temp_2.txt","w") as file_writer:
    #LE WRITE AJOUTE DU TEXTE ET SUPPRIME TOUT CE QU'IL Y AVAIT!!!!
    pretty_sentence = f"Ce rappel a ete un peu long mais peut-etre qu il a ete utile\n"
    file_writer.write(pretty_sentence)

with open("temp_3.txt","a") as file_appender:
    #LE APPEND AJOUTE DU TEXTE SANS SUPPRIMER CE QU'IL Y AVAIT
    pretty_sentence = f"Ce rappel a ete un peu long mais peut-etre qu il a ete utile\n"
    file_appender.write(pretty_sentence)