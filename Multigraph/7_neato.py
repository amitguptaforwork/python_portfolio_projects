import networkx as nx
from networkx.drawing.nx_pydot import write_dot

nx.MultiGraph ([(1,2),(1,2),(1,2),(3,1),(3,2)])
nx.write_dot(Gm,'multi.dot')
#!neato -T png multi.dot > multi.png