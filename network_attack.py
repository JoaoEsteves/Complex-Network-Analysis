import networkx as nx
from random import randint
from operator import itemgetter
import matplotlib.pyplot as plt

N_FRACTION = 2/100

def unt_choose_node(graph):
    nodes = list(graph.nodes())
    index = randint(0, len(nodes)-1)
    return nodes[index]

def tar_choose_node(graph):
    degrees = graph.degree()
    n_maxdegree = max(degrees,key=itemgetter(1))[0]
    return n_maxdegree

def remove_nodes(attack_type,fraction,graph):
    n_remainingnodes = nx.number_of_nodes(graph)
    if fraction > n_remainingnodes:
        fraction = n_remainingnodes
    for i in range(fraction):
        if attack_type == 'U':
            graph.remove_node(unt_choose_node(graph)) 
        elif attack_type == 'T':
            graph.remove_node(tar_choose_node(graph))  
    return graph

def attack(attack_type,graph):
    nodes_removed = N_FRACTION
    nodes_fraction = round(nx.number_of_nodes(graph) * N_FRACTION) 
    fraction_removed = []
    gcc_diameter = []
    for i in range(0, int(100 / (N_FRACTION * 100))):
        if i == 49:
            graph = remove_nodes(attack_type, nx.number_of_nodes(graph), graph)
        else:
            graph = remove_nodes(attack_type,nodes_fraction,graph)
        fraction_removed.append(nodes_removed)
        try:
            n_diameter = nx.diameter(max(list(nx.connected_component_subgraphs(graph)), key = len))
        except ValueError:
            n_diameter = 0
        gcc_diameter.append(n_diameter)
        nodes_removed += N_FRACTION
        nodes_removed = round(nodes_removed, 2)
    results = []
    results.append(fraction_removed)
    results.append(gcc_diameter)
    
    return results
        
def generate_attacks(attack_type):
	starWars = nx.read_edgelist('sw_edges.txt', create_using = nx.Graph(), nodetype = int)
	swRes = attack(attack_type, starWars)
	usAIR = nx.read_edgelist('air_edges.txt', create_using = nx.Graph(), nodetype = int)
	infraRes = attack(attack_type, usAIR)
	neuralNet = nx.read_edgelist('nn_edges.txt', create_using = nx.Graph(), nodetype = int)
	nnRes = attack(attack_type, neuralNet)
	
	plt.plot(swRes[0], swRes[1], label = 'social')
	plt.plot(infraRes[0], infraRes[1], label = 'infrastructural')
	plt.plot(nnRes[0], nnRes[1], label = 'biological')

	plt.xlabel('Nodes Percentage')
	plt.ylabel('Graph Diameter')
	plt.legend()

	plt.show()

#generate_attacks('U')
#generate_attacks('T')