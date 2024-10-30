#https://stackoverflow.com/questions/14943439/how-to-draw-multigraph-in-networkx-using-matplotlib-or-graphviz

# You can use pyvis package.
# I just copy-paste this code from my actual project in Jupyter notebook.

from pyvis import network as pvnet
import networkx as nx

def plot_g_pyviz(G, name='out.html', height='300px', width='500px'):
    g = G.copy() # some attributes added to nodes
    net = pvnet.Network(notebook=True, directed=True, height=height, width=width)
    opts = '''
        var options = {
          "physics": {
            "forceAtlas2Based": {
              "gravitationalConstant": -100,
              "centralGravity": 0.11,
              "springLength": 100,
              "springConstant": 0.09,
              "avoidOverlap": 1
            },
            "minVelocity": 0.75,
            "solver": "forceAtlas2Based",
            "timestep": 0.22
          }
        }
    '''

    net.set_options(opts)
    # uncomment this to play with layout
    # net.show_buttons(filter_=['physics'])
    net.from_nx(g)
    return net.show(name)

# G = nx.MultiDiGraph()
# [G.add_node(n) for n in range(5)]
# G.add_edge(0, 1, label=1)
# G.add_edge(0, 1, label=11)
# G.add_edge(0, 2, label=2)
# G.add_edge(0, 3, label=3)
# G.add_edge(3, 4, label=34)

G = nx.MultiDiGraph()
edges = [(1, 2), (1, 3), (3, 1),(3, 1),(3, 1),(3, 1),(3, 1)]

G.add_edges_from(edges)

plot_g_pyviz(G)