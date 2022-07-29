import requests

class Authenticate:
    
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def jwt(self):
        r = requests.post("http://178.233.176.141:52832/api/auth/local", data=self.kwargs)
        r = r.json()
        if 'jwt' in r:
            return r['jwt']
        else:
            return 1

auth = Authenticate(**{'identifier':'edizadeh.masoud', 'password':'091197906940'})
