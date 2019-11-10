import json

import requests
import datetime
from django.conf import settings


class NearestAirport():
    def update_token(self):
        data = {'client_id': settings.API_KEY_LUFTHANSA_ID,
                'client_secret': settings.API_KEY_LUFTHANSA_SECRET,
                'grant_type': 'client_credentials'}
        response = requests.post(url='https://api.lufthansa.com/v1/oauth/token', data=data)
        dec_resp = json.loads(response.content)
        # dec_resp = {key.decode(): val.decode() for key, val in response.content}
        self.token = dec_resp['access_token']
        self.timer = datetime.datetime.now()

    token = ""
    timer = datetime.datetime.now()

    def get_airport(self, location):
        if self.token == "" or self.timer < datetime.datetime.now():
            self.update_token()
        # Our API key needs manual approval, apaprently. Faking functionality until we receive it
        airports = {'Bucharest': 'Bucharest Henri Coandă International Airport',
                     'Bremen': 'Bremen Airport'}

        return airports[location]
