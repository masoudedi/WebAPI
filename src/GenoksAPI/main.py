import requests
import json

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

    def Post(self, endpoint, dataJson):
        r = requests.post(self.api_urls[endpoint],
        data=json.dumps(dataJson),
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
class Post_sample:
    pass

if __name__ == "__main__":
    api = Genoks_api()
    samples = api.Get("samples")
    data={
    "data": {
        "sample_id": "842-G-AlUmBar",
        "patient_name": "Alias Umu Barbara",
        "result_date": "2022-07-26T11:15:36.559Z",
        "save_date": "2022-07-26T11:15:36.559Z",
        "sequencing_technique": "WES",
        "sequencing_type": "NovaSeq",
        "customer_id": 1,
        "status": 0,
        "run_id": "123456789"
    }
    }
    posSample = api.Post("samples", data)
    print(posSample)
