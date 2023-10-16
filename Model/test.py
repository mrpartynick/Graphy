from GraphManager import Model
from DataStructures import Graph

N =  [[0,1,1,1,1,1,0,0], # a
	 [0,0,1,0,1,0,0,0], # b
	 [0,0,0,1,0,0,0,0], # c
	 [0,0,0,0,1,0,0,0], # d
	 [0,0,0,0,0,1,0,0], # e
	 [0,0,1,0,0,0,1,1], # f
	 [0,0,0,0,0,1,0,1], # g
	 [0,0,0,0,0,1,1,0]] # h

def check_for_nodes(graph):
	dict_of_nodes = {}

	value_of_nodes = len(graph)

	for node_index in range(value_of_nodes):
		dict_of_nodes[node_index] = graph[node_index].keys()

	return dict_of_nodes


m = Model()
m.build_graph_from_incidence(N)
m.draw()