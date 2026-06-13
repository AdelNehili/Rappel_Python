#_________________________Rappel LIST/DICT
def generate_values():
    #yield = return + function state save
    k=1
    while True:
        yield 2**k
        k+=1

def generate_list(nbr_element:int):
    generator = generate_values()
    keys = [i for i in range(nbr_element)] #One liner : On remplit avec i, sachant que i prend toutes les valeurs de [0,nbr_element[
    values = [next(generator) for i in range(nbr_element)] #One liner : On remplit avec la prochaine valeur de generator, sachant que i prend toutes les valeurs de [0,nbr_element[
    return keys, values

def generate_dico(keys:list, values:list)->dict:
    #TODO : Vous devez parcourir les deux listes en MÊME temps. Indice : Toutes les liste travaillent avec les indices
    #   Vous devez remplir le dict avec chaque pairs clé-valeur
    my_dico = {}
    for i in range(len(keys)):
        current_key = keys[i]
        current_value = values[i]
        #Création de la pair clé-valeur
        my_dico[current_key] = current_value

    #ATTENTION : NE PAS OUBLIER DE RETURN
    return my_dico

#_________________________Rappel FILE ACCESS
def write_data(sentence:str, file_path:str)->None:
    #Pose le curseur d'écriture en DEBUT de text -> Pour éviter la corruption, on clean tout le file.txt
    file = open(file_path, "w")
    file.write(sentence+"\n")
    file.close()

def append_data(sentence:str, file_path:str)->None:
    #Pose le curseur d'écriture en FIN de text -> Permet de juste devoir ajouter la data
    file = open(file_path, "a")
    file.write(sentence+"\n")
    file.close()

def read_data(file_path:str)->list:
    #Seul accès permettant de choisir où placer le curseur (par défaut, en début) -> Permet de lire
    file = open(file_path, "r")
    all_lines = file.readlines() #Génère une liste de ligne
    file.close()
    return all_lines

