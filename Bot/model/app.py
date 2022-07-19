import requests
import json
from ampalibe import Model


class Fetch(Model):

    def __init__(self, conf):
        super().__init__(conf)

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

