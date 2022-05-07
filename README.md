# mit_bitcoinexpo_hackathon
Creating a stacks-based recommender sytem for NFTs, with security measures to protect against washing.

## infrastructure 

Using the Stacksdata open API, the python request module is used to query a list of all NFT contracts. 

For each contract, the name, description, token ID and url of constituent NFTs are accumulated into a database. In total, the Stacksdata API queries ‘token’ , ‘transactions’ , and ‘volumes’ are called, and the responses are processed at the NFT level and tabularized.

etl.py provides the 'production' implementation that generated data for ingestion by the AI embedding process. Experimental versions, and the wash trade analytics, are stored in the *hackexpo* directory. 

![Image](figs/dataview.png)

## AI

State of the art neural networks for natural language processing and computer vision are used for embedding NFT text data and image data. The high dimensional representation of each NFT can be used for myriad use cases including NFT recommendation and targeted airdrops. The HTML files in the embedding directory contains preliminary work which can be loaded in a browser.  

embedding.py contains a text-only machine learning model using the pretrained sentence transformer, which yields representations with informative structure for our scoped uses. 

NFT_Neural_Network_Embedding_withimage.ipynb contains an image-based ML model that encodes url-retrieved images and creates an embedding on visual signals.


![Image](figs/embed_still.png)

## embedding

A directory of NFT-level embeddings visualized with t-stochastic neighbor embedding (t-SNE) and Principal Component Analysis (PCA). The html files may be loaded in a browser tab.  
