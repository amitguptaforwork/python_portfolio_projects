
import networkx as nx
import matplotlib.pyplot as plt



#G = nx.DiGraph()
#G = nx.MultiGraph()
G = nx.MultiDiGraph()
G.add_edges_from([(1, 1), (1, 7), (2, 1), (2, 2), (2, 3), 
                  (2, 6), (3, 5), (4, 3), (5, 4), (5, 8),
                  (5, 9), (6, 4), (7, 2), (7, 6), (8, 7)])
  
plt.figure(figsize =(9, 9))
pos = nx.circular_layout(G)
nx.draw_networkx(G,pos)
ax = plt.gca()
# Set margins for the axes so that nodes aren't clipped
ax.margins(0.20)
plt.axis("off")
plt.show()

 