import networkx as nx
import matplotlib.pyplot as plt
import collections
from collections import Counter
from math import log

def createGraph(file):
    G = nx.read_edgelist(file, create_using = nx.Graph(), nodetype = int)
    return G

def degreeDistribution(G1, G2, G3):
	cl1 = degreesCounter(G1)
	plt.plot(list(cl1.keys()), list(cl1.values()), label = 'social')

	cl2 = degreesCounter(G2)
	plt.plot(list(cl2.keys()), list(cl2.values()), label = 'infrastructure')

	cl3 = degreesCounter(G3)
	plt.plot(list(cl3.keys()), list(cl3.values()), label = 'biological')
	plt.legend()

	plt.xscale('log')
	plt.yscale('log')
	plt.xlabel('Degree Value')
	plt.ylabel('Nodes Count')
	plt.title('Degree Distribution')
	plt.show()

def degreesCounter(G):

	deg = G.degree()
	degVec = []
	
	for tp in deg:
		degVec.append(log(tp[1]))

	aux = {i:degVec.count(i) for i in degVec}
	degreesCounter = collections.OrderedDict(sorted(aux.items()))

	return degreesCounter

#Centralities calculations
def betweennessCentrality(G):
    betweenessCentrality = nx.betweenness_centrality(G, k = None, normalized = True, weight = None, endpoints = False, seed = None)
    betweennessList = list(betweenessCentrality.values())
    aux = {i:betweennessList.count(i) for i in betweennessList}
    betweennessCentrality = collections.OrderedDict(sorted(aux.items()))
    return betweennessCentrality

def closenessCentrality(G):
    closenessCentrality = nx.closeness_centrality(G, u = None, distance = None)
    closenessList = list(closenessCentrality.values())
    aux = {i:closenessList.count(i) for i in closenessList}
    closenessCentrality = collections.OrderedDict(sorted(aux.items()))
    return closenessCentrality

def eigenvectorCentrality(G):
    eigenvectorCentrality = nx.eigenvector_centrality(G)
    eigenvectorList = list(eigenvectorCentrality.values())
    aux = {i:eigenvectorList.count(i) for i in eigenvectorList}
    eigenvectorCentrality = collections.OrderedDict(sorted(aux.items()))
    return eigenvectorCentrality



#Plot Distributions functions
def plotBetweennessCentralityDist(G1, G2, G3):
    betw = betweennessCentrality(G1)
    plt.plot(list(betw.keys()), list(betw.values()), 'bo', label = 'social')

    betw = betweennessCentrality(G2)
    plt.plot(list(betw.keys()), list(betw.values()), 'go', label = 'infrastructure')


    betw = betweennessCentrality(G3)
    plt.plot(list(betw.keys()), list(betw.values()), 'ro', label = 'biological')

    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.legend()
    plt.title('Betweenness Centrality Distribution')
    plt.show()


def plotClosenessCentralityDist(G1, G2, G3):
    cl1 = closenessCentrality(G1)
    plt.plot(list(cl1.keys()), list(cl1.values()), 'bo', label = 'social')

    cl2 = closenessCentrality(G2)
    plt.plot(list(cl2.keys()), list(cl2.values()), 'go',label = 'infrastructure')

    cl3 = closenessCentrality(G3)
    plt.plot(list(cl3.keys()), list(cl3.values()), 'ro', label = 'biological')
    plt.xlabel('Probability')
    plt.ylabel('Nodes Count')
    plt.legend()
    plt.title('Closeness Centrality Distribution')
    plt.show()


def plotEigenvectorCentralityDist(G1, G2, G3):
    eig1 = eigenvectorCentrality(G1)
    plt.plot(list(eig1.keys()), list(eig1.values()), 'bo', label = 'social')

    eig2 = closenessCentrality(G2)
    plt.plot(list(eig2.keys()), list(eig2.values()), 'go', label = 'infrastructure')

    eig3 = closenessCentrality(G3)
    plt.plot(list(eig3.keys()), list(eig3.values()), 'ro', label = 'biological')

    plt.xlabel('Probability')
    plt.ylabel('Nodes Count')
    plt.legend()
    plt.title('Eigenvector Centrality Distribution')
    plt.show()


#main
gSW = createGraph('edges_social.txt')
gAIR = createGraph('edges_infra.txt')
gBIO = createGraph('edges_bio.txt')
