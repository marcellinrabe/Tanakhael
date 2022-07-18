from utils.functions import *
from getters import get_chapters_name
from fastapi import *
import uvicorn


app = FastAPI()

@app.get("/mg/get/{testament}")
async def get_name(testament):
    if testament == "ancient":
        return get_chapters_name(testament) 
    elif testament == "new":
        return get_chapters_name(testament)


@app.get("/mg/get/{versets}")
async def get(versets):
    versets_clean = versets.replace(" ","")
    versets_cap = versets_clean[0]+versets_clean[1].capitalize()+versets_clean[2:] if isPrefixed(versets_clean) else versets_clean.capitalize()
    return outpout(versets_cap) if valide_input(versets_cap) else {"error": "syntaxe incorrecte"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)