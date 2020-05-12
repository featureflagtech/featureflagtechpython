import requests 

class FeatureFlag:
    def __init__(self, opts):
        self.URL = "https://api.featureflag.tech"
        self.apikey = opts  # = {"fft-api-key": "38312f60-557a-11ea-8dfc-5976faa419b4"}
        self.flags = {}

    def getFlag(self):
        r = requests.get(url = self.URL, headers = self.apikey)
        self.flags = r.json()
        print(self.flags)

    def get(self, flagName):
        return self.flags.get(flagName)