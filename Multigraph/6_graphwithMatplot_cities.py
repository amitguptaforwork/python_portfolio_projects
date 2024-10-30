import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Kolkata Mumbai 2031
# Mumbai Pune 155

G = nx.read_weighted_edgelist('edge_list.txt', delimiter =" ")

population = {
		'Kolkata' : 4486679,
		'Delhi' : 11007835,
		'Mumbai' : 12442373,
		'Guwahati' : 957352,
		'Bangalore' : 8436675,
		'Pune' : 3124458,
		'Hyderabad' : 6809970,
		'Chennai' : 4681087,
		'Thiruvananthapuram' : 460468,
		'Bhubaneshwar' : 837737,
		'Varanasi' : 1198491,
		'Surat' : 4467797,
		'Goa' : 40017,
		'Chandigarh' : 961587
		}

# We have to set the population attribute for each of the 14 nodes
for i in list(G.nodes()):
	G.nodes[i]['population'] = population[i]

#pos = nx.circular_layout(G)

# Draw the graph G using Matplotlib.
#nx.draw_networkx(G,pos)
nx.draw_networkx(G)
# This line allows us to visualize the Graph

# The GCA() function is used to get the current Axes instance on the
#current figure matching the given keyword args or create one.

ax = plt.gca()
# Set margins for the axes so that nodes aren't clipped
ax.margins(0.20)
plt.axis("off")
plt.show()

df = pd.DataFrame(G);
print(df)
