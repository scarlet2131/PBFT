import pandas as pd

import networkx as nx
import matplotlib.pyplot as plt

class getPlot:
    def __init__(self,X,Y,W,diff=[]):
        self.X = X
        self.Y = Y 
        self.W = W
        self.diff = diff
   
        self.edge = []
        for i in range(len(self.X)):
            self.edge.append([self.X[i],self.Y[i]])
        
    def show(self,title):
        
        plt.figure(figsize=(7,6))
        plt.title(title)
        G = nx.Graph()
        for i in range(len(self.X)):
            x,y,w = self.X[i],self.Y[i],self.W[i]
            if [x,y] in self.diff or [y,x] in self.diff:
                # print("changeCOlor")
                G.add_edge(x,y,color="red",weight='4')
            else:
                G.add_edge(x, y,color="black",weight='1')
        pos = nx.circular_layout(G) # positions for all nodes
        

        # print(pos)
        edge_info = {}
       
        E = G.edges()
        colors = [ G[u][v]['color'] for u,v in E ]
        W = [ G[u][v]['weight'] for u,v in E ]

        for i in range(len(self.X)):
            x,y = self.X[i],self.Y[i]
            edge_info[(x,y)] = self.W[i]

        nx.draw_networkx(G,pos,with_labels = True, edge_color=colors, node_color='g', node_size = 500, width=W)

        # labels
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif',\
            font_color='white')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_info, font_size=10, font_family='sans-serif',\
            font_color='red')
        
        plt.axis('off')
        # plt.show()