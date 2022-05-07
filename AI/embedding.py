import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import os 

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('bert-base-nli-mean-tokens')


from sklearn.metrics.pairwise import cosine_similarity

def get_df(file_path = './nfts_{}.csv'):
    nftdf = []
    for ind in range(100, 900, 100):
        fp = file_path.format(ind)
        nftdf.append( pd.read_csv(fp).drop(columns=['Unnamed: 0']) )

    nftdf = pd.concat(nftdf) 

    # nftdf = nftdf.drop(columns = ['tokenId','url','recipient'])
    nftdf = nftdf.dropna().reset_index().drop(columns=['index'])
    # nftdf = nftdf[:10]
    return nftdf 

nftdf = get_df()

nftdf['d+n'] = nftdf.name.str.cat(nftdf.description)

nftdf3 = model.encode(nftdf['attributes'], 
                      show_progress_bar=True, 
                      batch_size=2*64, 
                    #   normalize_embeddings=True, 
                      device='cuda')

nftdf2 = model.encode(nftdf['d+n'], 
                      show_progress_bar=True, 
                      batch_size=2*64, 
                    #   normalize_embeddings=True, 
                      device='cuda')


nftdf2 = pd.concat([pd.DataFrame(nftdf2),pd.DataFrame(nftdf3)],axis=1)

pd.DataFrame(nftdf2).to_csv('nftdf2.csv',index=False)


from sklearn.decomposition import PCA

nft_tsne = PCA(n_components =3, ).fit_transform(nftdf2)
# nft_tsne = TSNE(n_components=3, n_jobs=-1).fit_transform(nftdf2)



pd.DataFrame(nft_tsne).to_csv('nft_tsne.csv',index=False)

fig = px.scatter_3d(
    nft_tsne, x=0, y=1, z=2,
    color=nftdf.contract ,
    hover_data= [nftdf.tokenId, nftdf.name, nftdf.description] )

fig.update_layout(xaxis=dict(showspikes=False) , 
        width=2000,
        height=1000,
        margin=dict(
            l=2,
            r=2,
            b=2,
            t=2,
            pad=4
        ), )


fig.update_traces(marker_size = 3 )
fig.update_coloraxes(showscale=False)
fig.update_scenes(xaxis_visible=False, yaxis_visible=False,zaxis_visible=False )

fig.write_html("attributes+description_pca.html")
fig.show()
