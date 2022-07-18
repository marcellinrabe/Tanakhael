import json
from sre_compile import isstring

def get_chapter(chapter: str, number: int):
    """
        retourne les versets d'un chapitre en entier
        @var cpt nous informe le numero de chapitre afin d'indenfier si c'est dans le nouveau testament ou l'ancien
        
    """
    with open("alias.json") as alias:
        alias_dict = json.load(alias)
        cpt = 0
        for alias in alias_dict:
            cpt += 1
            if chapter == alias.replace(" ", ""):
                key = alias_dict[alias]
                namefile = key.lower() if isstring(key) else key[-1]
                namefile = namefile+".json" # with extension
                
                # L'ancien testament compte 39 chapitre et le nouveau testament 27 donc si le compteur arrive a bouclé jusqu'à la 
                # 40eme fois alors c'est qu'il a passé en revue l'ancien testament
                if cpt <= 39:
                    prefix_path= "../baiboly-json/Testameta taloha/"

                else:
                    prefix_path="../baiboly-json/Testameta vaovao/"
                
                with open(prefix_path+namefile) as chapter:
                    
                    chapter_dict = json.load(chapter)

                    if number not in chapter_dict:
                        return {"error": "toko depassé"}
                    
                    return chapter_dict[number]

def get_verse(chapter: str, number: int, verse: int):
    """
        retourne un seule ligne de verset specifique
    """
    response = {}
    try:
        with open("alias.json") as alias:
            alias_dict = json.load(alias)
            cpt = 0

            for alias in alias_dict:
                cpt += 1
                if chapter == alias.replace(" ", ""):
                    key = alias_dict[alias]
                    namefile = key.lower() if isstring(key) else key[-1]
                    namefile = namefile+".json" # with extension
                
                    if cpt <= 39:
                        prefix_path= "../baiboly-json/Testameta taloha/"
                    else:
                        prefix_path="../baiboly-json/Testameta vaovao/"
                
                    with open(prefix_path+namefile) as chapter:
                        chapter_dict = json.load(chapter)
                        if number not in chapter_dict:
                            return {"error": "toko depassé"}

                    response[verse[0]] = chapter_dict[number][str(verse[0])]
    except KeyError:
        return {"error": "andininy tsy izy"}
    else:
        return response

def get_verse_interval(chapter: str, number: int, interval: tuple):
    """
        retourne un intervalle de versets d'un chapitre
    """

    andininy_1, andininy_2 = interval

    with open("alias.json") as alias:
        alias_dict = json.load(alias)
        cpt = 0
        response = {}

        for alias in alias_dict:
            cpt += 1
            if chapter == alias.replace(" ", ""):
                key = alias_dict[alias]
                namefile = key.lower() if isstring(key) else key[-1]
                namefile = namefile+".json" # with extension
                
                if cpt <= 39:
                    prefix_path= "../baiboly-json/Testameta taloha/"

                else:
                    prefix_path="../baiboly-json/Testameta vaovao/"
                
                with open(prefix_path+namefile) as chapter:
                    
                    chapter_dict = json.load(chapter)

                    if number not in chapter_dict:
                        return {"error": "toko depassé"}
                    for andininy in range(int(andininy_1), int(andininy_2)+1):
                        response[andininy] = chapter_dict[number][str(andininy)]
                    
                    return response
                
def get_chapters_name(testament: str)-> dict:
    """
        retourne le nom de tous le testament
        @param str testament soit "ancient" ou "new"
    """

    if testament == "ancient":
        with open("alias.json") as alias:
            response = {}
            cpt = 0
            alias_dict = json.load(alias)
        
            for alias in alias_dict:
                cpt += 1
                if cpt <= 39:
                    response[cpt] = {"sous-titre": alias, "nom": alias_dict[alias]}
            
            return response
    elif testament == "new":
        with open("alias.json") as alias:
            response = {}
            cpt = 0
            alias_dict = json.load(alias)
        
            for alias in alias_dict:
                cpt += 1
                if cpt > 39:
                    response[cpt] = {"sous-titre": alias, "nom": alias_dict[alias]}
            return response
        