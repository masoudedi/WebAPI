import requests

class Genoks_api:
    def __init__(self):
        self.api_urls = {
            "customers": "http://178.233.176.141:52832/api/customers/",
            "samples": "http://178.233.176.141:52832/api/samples/",
            "variants": "http://178.233.176.141:52832/api/variants",
        }

    def Get(self, endpoint):
        r = requests.get(self.api_urls[endpoint])
        return r.json()

    def create(self, endpoint, dataJson):
        r = requests.post(self.api_urls[endpoint],
        data=dataJson,
        headers={
            'Content-Type': 'application/json'
        })
        return r.json()

    def update(self, endpoint, id, dataJson):
        r = requests.put(self.api_urls[endpoint] + str(id),
        data=dataJson,
        headers={
        'Content-Type': 'application/json'
        })

if __name__ == "__main__":
    api = Genoks_api()
    samples = api.Get("variants")
    print(samples)
