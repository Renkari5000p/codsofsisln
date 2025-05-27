from hashlib import md5
from requests import get
from datetime import datetime

class Restmarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    pub_key = 'eba85e226fe963244f31850f6d45966f' 
    priv_key = 'e0780eb15b95f6b559285845058210255e9b3524'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts':self.timestamp,'apikey':self.pub_key,'hash':self.hash_params()}
        result = get('https://gateway.marvel.com:443/v1/public/characters',
                     params=params)
                     
        data = result.json()
        print(data)
        print(data['status'])

rest=Restmarvel()
rest.get_heroes()