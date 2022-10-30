import requests

def get_nfts(address):
    d = requests.get(f'https://api.rarible.org/v0.1/items/byOwner?owner=ETHEREUM:{address}')
    print(d.text)


get_nfts('0x0EEaa7FD870fd4862D006a01883b7e06DEE97d0f')