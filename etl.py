from urllib import response
import requests
import pandas as pd
import json
import pprint
import seaborn as sns
import matplotlib.pyplot as plt



base_url = 'https://stacks-node-api.mainnet.stacks.co/extended/v1/tokens/nft/holdings' 
# "https://stacks-node-api.testnet.stacks.co/" # #"https://cat-fact.herokuapp.com"
facts = "principal=SPNWZ5V2TPWGQGVDR6T7B6RQ4XMGZ4PXTEE0VQ0S.marketplace-v3"

first_response = requests.get(base_url+facts)
response_list=first_response.json()
print(response_list)
