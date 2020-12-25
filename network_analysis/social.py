import networkx as nx

"""
G = nx.Graph()

#adding nodes to network
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])

#finding nodes in Graph
print(G.nodes())

#adding edges to network
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
G.add_edge("u","w")

print(G.edges())
G.remove_node(2)
print(G.edges())
G.remove_nodes_from([4,5])
G.remove_edge(1,3)
print(G.edges())
G.remove_edges_from([(1,2),("u","w")])
print(G.edges())
"""

import matplotlib.pyplot as plt
"""
G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
#plt.savefig("karate_graph.pdf")
#print(G.degree())
#print degree at node 33
#print(G.degree()[33])
#print degree at node 33
#print(G.degree(33))
print(len(G.nodes()),len(G.edges()))
print(G.degree(0) is G.degree()[0])
"""
import scipy
import scipy.stats
from scipy.stats import bernoulli

N = 20
p = 0.2

def er_graph(N, p):
    """Generate an ER Graph"""
    #Create enpty Graph
    G = nx.Graph()
    #add all N nodes in the Graph
    G.add_nodes_from(range(N))
    #loop over all pairs of nodes
    for node1 in G.nodes():
        for node2 in G.nodes():
        #add an edge with prob p
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

#nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
#plt.savefig("graph.pdf")

"""
G = nx.erdos_renyi_graph(10,0)
nx.draw(G)
plt.savefig("graph2.pdf")
"""

def plot_degree_distribution(G):
     degree_sequence = [d for n, d in G.degree()]
     plt.hist(degree_sequence, histtype="step")
     plt.xlabel("Degree $k$")
     plt.ylabel("Degree $P(k)$")
     plt.title("Degree Distribution")
"""
G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
plt.savefig("hist1.pdf")
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
plt.savefig("hist2.pdf")
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist3.pdf")
"""
"""
D = {1:1, 2:2, 3:3}
plt.hist(D)
plt.show()
"""
G1 = nx.erdos_renyi_graph(100, 0.03)
plot_degree_distribution(G1)
plt.savefig("hist4.pdf")
G2 = nx.erdos_renyi_graph(100, 0.30)
plot_degree_distribution(G2)
plt.savefig("hist5.pdf")
