import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

df = pd.DataFrame({
    'name':['karate','as-22july06','cnr-2000','eu-2005','in-2004','roadcentral','uk-2002','roadusa'],
    'Louvain':[0,0.036,4.594,14.106,26.646,123.028,433.468,183.516],
    'RG,k=9':[0,0.072,4.040,24.676,21.396,114.824,600,196.072],
    'our,k=75%':[0,0.028,0.792,3.844,3.156,36.612,70.976,53.036],
    'our,k=50%':[0,0.036,0.768,4.448,3.516,36.016,71.256,48.552],
    'our,k=25%':[0,0.044,0.932,4.748,4.368,44.392,70.880,49.852]

})

df2 = pd.DataFrame({
    'name':['karate','as-22july06','cnr-2000','eu-2005','in-2004','roadcentral','uk-2002','roadusa'],
    'Louvain':[0.41452,0.66230,0.91274,0.93822,0.98020,0.99738,0.98973,0.99804],
    'RG,k=9':[0.39423,0.64839,0.91051,0.92746,0.96735,0.99723,2.5,0.99791],
    'our,k=75%':[0.35528,0.61879,0.91073,0.92280,0.97707,0.99509,0.94453,0.99623],
    'our,k=50%':[0.36037,0.59751,0.90602,0.89709,0.97012,0.99205,0.93721,0.99370],
    'our,k=25%':[-0.04980,0.48388,0.88533,0.85685,0.93383,0.98569,0.94389,0.99382]

})


ax = plt.gca()

df.plot(kind='line',x='name',y='Louvain',ax=ax)
df.plot(kind='line',x='name',y='RG,k=9', color='red', ax=ax)
df.plot(kind='line',x='name',y='our,k=75%', color='green', ax=ax)
df.plot(kind='line',x='name',y='our,k=50%', color='yellow', ax=ax)
df.plot(kind='line',x='name',y='our,k=25%', color='pink', ax=ax)

plt.show()

# # load the karate club graph
# G = nx.karate_club_graph()
#
# #first compute the best partition
# partition = community_louvain.best_partition(G)
#
# # compute the best partition
# partition = community_louvain.best_partition(G)
#
# # draw the graph
# pos = nx.spring_layout(G)
# # color the nodes according to their partition
# cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
# nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
#                        cmap=cmap, node_color=list(partition.values()))
# nx.draw_networkx_edges(G, pos, alpha=0.5)
# plt.show()


