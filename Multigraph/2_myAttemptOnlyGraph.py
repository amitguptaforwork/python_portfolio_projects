# To import package
# to draw we also need pip install matplotlib


import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# To add a node
# G.add_node("betsy")
# G.add_node("SAP")
# G.add_node("TRAX")

# G.add_edge("betsy","SAP")
# G.add_edge("betsy","TRAX")

#The above five lines can be accomplished in one line.
G.add_edges_from([("betsy","SAP"), ("betsy","TRAX")])


  
plt.figure(figsize =(9, 9))
pos = nx.circular_layout(G)
nx.draw_networkx(G,pos)
ax = plt.gca()
# Set margins for the axes so that nodes aren't clipped
ax.margins(0.20)
plt.axis("off")
plt.show()
