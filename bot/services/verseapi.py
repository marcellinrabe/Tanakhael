"""Service around getting verse"""

import requests


class VerseAPI:

    def __init__(self, proxy):
        self.proxy = proxy

    def _build_url(self, uri):
        return f"{self.proxy}{uri}"

    def get(self, uri: "str", params={}):
        url = self._build_url(uri)
        response = requests.get(url, params)
        if response.status_code == 200:
            data = response.json()
            return data
        return None
