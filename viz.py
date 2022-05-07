import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go


def get_df(file_path = './nfts_{}.csv'):

    nftdf = []
    for ind in range(100, 900, 100):
        fp = file_path.format(ind)
        nftdf.append( pd.read_csv(fp).drop(columns=['Unnamed: 0']) )

    nftdf = pd.concat(nftdf) 
    # nftdf = nftdf.drop(columns = ['tokenId','url','attributes','recipient'])
    nftdf = nftdf.dropna().reset_index().drop(columns=['index'])
    return nftdf 

nftdf = get_df()

nft_tsne = pd.read_csv('nft_tsne.csv').values

fig = px.scatter_3d(
    nft_tsne, x=0, y=1, z=2,
    color=nftdf.contract ,
    hover_data= [nftdf.tokenId, nftdf.name, nftdf.description], 
    )

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

fig.show()
