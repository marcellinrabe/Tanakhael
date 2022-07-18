from re import search

def isMatched(text: str)-> bool:
    assert text.capitalize()
    text_clean = text.replace(" ","")
    text_find = search("[A-Z][a-z]{2}[1-9]{1,3}(:[1-9]{1,3}(-[1-9]{1,3})?)?", text_clean)
    if  text_find is None and text_clean == "Rechercher".capitalize():
        return False
    else:
        print(text_find.group(0))
        return False if len(text_clean) != len(text_find.group(0)) else True

    
    