from road_map import *
from shortest_path import *
from pbft import *
from get_plot import *

G = road_map("road_graph.txt")
G.gen_graph()
print("User has requested for a shortest path from source to destination")
path = shortest_path(G,7,3)
path.get_path()

GPLOT = getPlot(G.X, G.Y , G.W)
SPLOT = getPlot(G.X, G.Y, G.W,path.edge)
pb = pbft(G,path,GPLOT,SPLOT,7,3,3)

pb.controller()