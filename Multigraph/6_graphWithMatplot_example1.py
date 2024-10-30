

# https://www.geeksforgeeks.org/directed-graphs-multigraphs-and-visualization-in-networkx/

import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()
edges = [(1, 2), (1, 3), (3, 1),(3, 1),(3, 1),(3, 1),(3, 1)]

G.add_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw_networkx(G,pos , connectionstyle="arc3,rad=0.4")
#nx.draw_networkx(G,pos , connectionstyle="arc3,rad=0.4",node_size=5, node_color='w', alpha=0.4);
#nx.draw_networkx_nodes(G,pos , node_size=5, node_color='w', alpha=0.4);


ax = plt.gca()
# Set margins for the axes so that nodes aren't clipped
ax.margins(0.20)
plt.axis("off")
plt.show()