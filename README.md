![Image](figs/splash.png)


# Non-Fungible Analytics (MIT Bitcoin Hackathon 2022)
We present a stacks-based recommender sytem for NFTs that is powered by AI, with security measures to protect against washing.

Use cases include:
-NFT collection analysis on price anomalies and multiple-wallet-ownership
-Warning system integrated on top of recommendations and custom searches
-Protecting the users by reducing scams, fraud and financial loss

We fetched all NFT data from the Stacks Blockchain with python deployed APIs (e.g. collection name, prices, volume, description, attributes, images). After cleaning and processing this data, we ran Neural Networks and Principle Component Models to create NFT embeddings. Multidimensional mappings with many valuable use cases. 


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
