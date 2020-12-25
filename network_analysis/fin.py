import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#Read data
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
#create graphs
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)
#Net stats: nodes, edges and degrees
def basic_net_stats(G):
    print("Number of nodes: %d" %G.number_of_nodes())
    print("Number of edges: %d" %G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))
#Plot degree of Distribution
def plot_degree_distribution(G):
     degree_sequence = [d for n, d in G.degree()]
     plt.hist(degree_sequence, histtype="step")
     plt.xlabel("Degree $k$")
     plt.ylabel("Degree $P(k)$")
     plt.title("Degree Distribution")

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)

#Get basic Network stats
basic_net_stats(G1)
basic_net_stats(G2)
#Get Degree of distribution
plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")

gen = connected_component_subgraphs(G1)
g = gen.__next__()
print(g.number_of_nodes())
#not really used
print(len(gen.__next__()))
G1_LCC = max(connected_component_subgraphs(G1), key=len)
G2_LCC = max(connected_component_subgraphs(G2), key=len)

print(len(G1_LCC))
print(G1_LCC.number_of_nodes())
print(len(G2_LCC))
print(G2_LCC.number_of_nodes())

print(G1_LCC.number_of_nodes()/ G1.number_of_nodes())
print(G2_LCC.number_of_nodes()/ G2.number_of_nodes())
"""
plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")
"""
print(len(G1))
