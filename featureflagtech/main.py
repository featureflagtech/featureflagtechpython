import requests 

class FeatureFlag:
    def __init__(self, key):
        
        self.apikey = {"fft-api-key": key.get("apiKey")}
        if not self.apikey.get("fft-api-key"):
            raise Exception("apiKey not given")

        r = (requests.get(url = "https://api.featureflag.tech",
        headers = self.apikey))

        if not r.ok:
            raise Exception("Invalid API key")

        else:
            self.flags = r.json()

    def get(self, flagName):
        if self.flags.get(flagName) is None:
            raise Exception("Flag not found")
        
        else:
            return self.flags.get(flagName)