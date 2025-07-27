# LHS_DataAnalysisCapstoneProject Python Script

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    data = response.json()
    print("Current Bitcoin Price (USD):", data['bpi']['USD']['rate'])
else:
    print("Failed to fetch data:", response.status_code)