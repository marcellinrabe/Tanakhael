import re
from getters import *

prefix= "^[1-3]"
template = "[A-Z][a-z]{2}[0-9]{1,3}(:[0-9]{1,3}(-[0-9]{1,3})?)?"

def isPrefixed(versets: str)->bool:
    return False if re.search(prefix, versets) is None else True

def count_separator(versets: str):

    """
        verifier la présence des caractères clés de réconnaissances ":" et "-"
    """

    # rare est la chance à ce que cette condition soit vraie
    if not valide_input(versets):
        return {"error": "syntaxe incorrecte"}

    parseList = list(versets)
    chars = re.findall("\w", versets)
    [parseList.remove(c) for c in chars]
    separators =  tuple(parseList)
    if len(separators) == int(0):
        return int(0)

    elif len(separators) == int(1) and separators[0] == ":":
        return int(1)
    
    elif len(separators) == 2:
        return 2

    else:
        return {"error": "source séparateur"}

def valide_input(versets: str):

    """
        verifie la syntaxe du verset si cela correspond les formats suivants(les espaces omis):
        Gen 3 / Gen 3:2 / Gen 3:2-4
    """

    try:
        regex = re.search(prefix+template, versets) if isPrefixed(versets) else re.search(template, versets)
        text_find = regex.group(0)
        
        if regex is None or len(versets) != len(text_find):
            raise Exception("syntaxe incorrecte")
    except:
        return False
    else:
        return True

def divide_verse(versets: str)-> tuple:
    chapter_name = str()
    toko = 0
    andininy = []

    chapter_name = versets[:4] if isPrefixed(versets) else versets[:3]
    all = versets[4:].split(":") if isPrefixed(versets) else versets[3:].split(":")

    if ":" not in versets:
        number_in = re.findall("\d", versets)
        toko = number_in[1] if isPrefixed(versets) else number_in[0]
        andininy = (0,)
    else:
        toko = all[0]
        ambiny = all[1]
        if "-" not in versets:
            andininy = (int(ambiny),)
        else:
            andininy = ambiny.split("-")
            andininy = tuple([int(andininy[0]), int(andininy[1])])

    print(andininy)
    return chapter_name, toko, andininy

def outpout(versets: str):
    """
        retourne les versets
        @param versets_clean str le(s) verset(s) demandés par le client
        @param number_sep int le nombre de separateur
        (le terme separateur ici va du sens des caractères clés ":" et "-" qui identifie la syntaxe du verset)
    """


    chapter_name, toko, andininy = divide_verse(versets)
    number_sep = count_separator(versets)

    if number_sep == int(0):
        return get_chapter(chapter_name, toko)

    elif number_sep == int(1):
        return get_verse(chapter_name, toko, andininy)

    elif number_sep == int(2):
        return get_verse_interval(chapter_name, toko, andininy)

    else:
        return {"error": "source séparateur"}



