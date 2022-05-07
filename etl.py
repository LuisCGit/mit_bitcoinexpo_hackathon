from urllib import response
import requests
import pandas as pd
import json
import pprint
import seaborn as sns
import matplotlib.pyplot as plt

def query(url, request_params ):
    if request_params:
        resp = requests.get(url,
                    params = request_params
                    )
    else:
        resp = requests.get(url)
    try:
        response_dict = resp.json() 
    # results = response_dict['results']
    except:
        return []
        
    return response_dict 





url = "https://api.stacksdata.info/nft/contracts"


# url = "https://stacks-node-api.mainnet.stacks.co/extended/v2/tokens/nft/metadata"
#"https://stacks-node-api.mainnet.stacks.co/extended/v1/tokens/{contractId}/nft/metadata" #'https://stacks-node-api.mainnet.stacks.co/extended/v1/tokens/ft/metadata'
# request_params = {
#     'contractId' : "SP3PN1GRGNNV6KKS47XN34TJZ6MGBGC40G7KFEGMW.cash-cow",
    # 'offset' : 10
# }

request_params={
'limit': 100,
'offset': 0
}


contract_df = query( url, request_params )
contract_df = [ c['contractName'] for c in contract_df ]
# print(contract_df)
# print(contract_df.columns)
# contract_df.to_csv('contracts.csv')


query_list = [
'https://api.stacksdata.info/nft/contracts/{}/tokens',
# 'https://api.stacksdata.info/nft/contracts/{}/transactions',
# 'https://api.stacksdata.info/nft/contracts/{}/volume',

]

# print(contract_df)

all_nfts = []

import numpy as np 


for ind, contract in enumerate(contract_df):
    print(contract)
    contract_features = []
    
    
    for command in query_list:
        command = command.format( contract )
        print(command)
        # exit()

        request_params={
        'address': contract 
        }


        resp = query( command, request_params )
        
        # if 'volume' in resp:
        #     resp = [ r['transactions'] for r in resp ] 
        #     print(resp)

        # if 'transactions' in resp:
        #     resp = [ r['transactions'] for r in resp ] 
        #     print(resp)


        if type(resp) != list:
            continue 

        if len(resp) == 0:
            continue 
        
        contract_features += resp
        print(contract_features)


        # if type(resp[0]) == dict:
        #     print(resp[0])
        
        # print(resp)
        all_nfts += contract_features


    print(ind) 

    if ind % 100 == 0:

        
        nfts_df = pd.DataFrame(all_nfts)
        nfts_df.to_csv('nfts_{}.csv'.format(ind) )
        all_nfts = []            