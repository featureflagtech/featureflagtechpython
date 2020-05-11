import requests 

class Featureflagclient:
    def __init__(self):
        self.URL = "https://api.featureflag.tech"
        self.apikey = {"fft-api-key": "38312f60-557a-11ea-8dfc-5976faa419b4"}

    def get(self):
        r = requests.get(url = self.URL, headers = self.apikey)
        print(r.json())
