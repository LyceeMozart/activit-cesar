def identite(s : str) -> str :
    """ Renvoie la chaine s telle quelle """
    return s

assert identite("LU1IN011") == "LU1IN011"
assert identite("") == ""

def identite_texte(nom : str) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-copie.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-copie.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(identite(ligne))

def est_majuscule(c:str) ->  bool :
    """ c est un caractère"""
    return 65 <= ord(c) <= 90
assert est_majuscule("C")
assert not est_majuscule("c")
assert not est_majuscule(" ")
def est_minuscule(c:str) -> bool :
    """ c est un caractère"""
    return 97 <= ord(c) <= 122
assert est_minuscule("c")
assert not est_minuscule("C")
assert not est_minuscule(" ")
def carractere_decale(c:str,n:int)-> str:
    """c est un caractère et z un nombre entier"""
    if 65 <= ord(c) <= 90
        
    elif 97 <= ord(c) <=122

    else
    return chr(ord(c)) 
assert carractere_decale("a",0) == "a"
assert carractere_decale("a",3) == "d"


