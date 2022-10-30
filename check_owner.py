import requests

url = "https://deep-index.moralis.io/api/v2/0x0EEaa7FD870fd4862D006a01883b7e06DEE97d0f/nft?chain=eth&format=decimal"

headers = {
    "accept": "application/json",
    "X-API-Key": "vXUymcPVetrpjeM26X4rfHhZqlg9WjfJ9SDgvYf5Hvd02BtRl8UV1GbOgBpiuiFe"
}

response = requests.get(url, headers=headers)

print(response.text)