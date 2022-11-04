from email.header import Header
from symbol import parameters
import symbol
from wsgiref import headers
from requests import session
from pprint import pprint as pp 
import requests
import secrets

# https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview


class CMC: 
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.header = {"Accepts" : "Application/Json" ,'X-CMC_PRO_API_KEY' : token,}
        self.session = session()
        self.session.headers.update(self.headers)

        def getALLcoins(self):
            url = self.apiurl + '/v1/cryptocurrency/map'
            r = self.session.get(url)
            data = r.json()['data']
            return data

            def getprice(sels, symbol):
                url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
                parameters = {'symbol' : symbol}
                r = self.session.get(url, params = parameters)
                data = json()['data']
                return data



        pass
    

cmc = CMC(secrets.api_key)

pp(cmc.getAllcoins())
pp(cmc.getprice('BTC'))





