import requests
from otrsconfig import config
from pprint import pprint
import json
import inspect

class otrsapi():

    def __init__(self):

        rt = self.session()

        if 'Error' in rt:
            raise SystemExit(rt)

        # save session
        self.token = rt

        self.headers = { 'Accept':'application/json' }
        
        
    def session(self):

        auth = { 'UserLogin': config['user'], 'Password': config['pw'] }
        url  = config['url'] + config['sessionroute']

        try: 
            r  = requests.get(url, params=auth)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)



    def ticketget(self, ticket):

        #myfunc = inspect.getframeinfo(inspect.currentframe()).function + 'route'
        token = self.token
        url   = config['url'] + config[inspect.getframeinfo(inspect.currentframe()).function + 'route'] + ticket['TicketID']
        try:
            r = requests.get(url, params=token, headers=self.headers)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

    def createticket(self, ticket):

        token = self.token
        url   = config['url'] + config[inspect.getframeinfo(inspect.currentframe()).function + 'route']
       
        try:
            r  = requests.post(
                        url,
                        params=token,
                        data=json.dumps(ticket),
                        headers=self.headers
                 )
            r.raise_for_status()
            return r.json()
            
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
