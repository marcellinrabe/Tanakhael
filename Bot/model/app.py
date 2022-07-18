import requests
import json
from conf import Configuration



class Fetch():

    
    def verse(self, versets: str)-> dict:
        """
            returns the verses coming from the api in a dictionary
        """
        # verifier la syntaxe du versets

        response = requests.get(f'http://localhost:7000/mg/get/{versets}')
        return json.loads(response.text)

    def livres(self, testament: str)->dict:
        """
            retourne la liste des livres du testament
        """

        if testament in ["ancient", "new"]:
            response = requests.get(f'http://localhost:7000/mg/get/{testament}') 
            return json.loads(response.text)
        else:
            raise Exception("testament name not matching")

