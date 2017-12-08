# Please enter here the netids of all memebers of your group (yourself included.)
authors = ['ncm64','dm458','mok24']

# Which version of python are you using? python 2 or python 3?
python_version = "python 3"

from random import randint, random
import numpy as np

# Important: You are NOT allowed to modify the method signatures (i.e. the arguments and return types each function takes).

# Implement the methods in this class as appropriate. Feel free to add other methods
# and attributes as needed.
# Assume that nodes are represented by indices between 0 and number_of_nodes - 1
class DirectedGraph:

    def __init__(self,number_of_nodes):
        # self.graph = {node: [edges]}
        self.graph = {}
        self.matrix = None
        self.size = number_of_nodes
        self.init_nodes(number_of_nodes)

    def init_nodes(self, number_of_nodes):
        for node in range(number_of_nodes):
            self.add_node(node)

    def init_seed_data(self, seed_data = {}):
        self.graph = seed_data

    def add_node(self, node):
        if node not in self.graph:
            # add an edge from each node to itself
            self.graph[node] = []

    def add_edgeless_nodes(self):
        for node in self.graph.keys():
            # if edges list is empty
            #   add node as an edge to itself
            if not self.edges_from(node):
                self.graph[node].append(node)

    def add_edge(self, origin_node, destination_node):
        if origin_node not in self.graph:
            self.add_node(origin_node)
        if destination_node not in self.graph:
            self.add_node(destination_node)
        self.graph[origin_node].append(destination_node)

    def edges_from(self, origin_node):
        ''' This method shold return a list of all the nodes u such that the edge (origin_node,u) is
        part of the graph.'''
        return self.graph[origin_node]

    def check_edge(self, origin_node, destination_node):
        ''' This method should return true is there is an edge between origin_node and destination_node
        and destination_node, and false otherwise'''
        if destination_node not in self.graph or origin_node not in self.graph:
            return False
        elif destination_node in self.graph[origin_node]:
            return True
        else:
            return False

    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return len(self.graph.keys())

    def create_matrix(self, eps = 1/7):
        matrix_size = self.number_of_nodes()
        # initialize empty matrix
        matrix = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
        # loop over all nodes j in graph
        for j in self.graph.keys():
            # loop over each node's edges i
            for i in self.edges_from(j):
                # if there is an edge from j -> i
                #   set corresponding matrix index to 1 / out-degree(j)
                if self.check_edge(j, i):
                    matrix[j][i] = 1 / len(self.edges_from(j))
                # else there is no edge from j -> i
                #   set corresponding matrix index to 0
                else:
                    matrix[j][i] = 0
        return np.matrix(matrix)
        self.matrix = np.matrix(matrix)
        print(self.matrix)



    def print_graph(self):
        print('Graph:', self.graph)


def scaled_page_rank(graph, num_iter, eps = 1/7.0):
    ''' This method, given a directed graph, should run the epsilon-scaled page-rank
    algorithm for num-iter iterations and return a mapping (dictionary) between a node and its weight.
    In the case of 0 iterations, all nodes should have weight 1/number_of_nodes'''
    graph_size = graph.number_of_nodes()
    matrix = graph.create_matrix()

    # initialize probabilities equally
    probabilities = np.array([[1/graph_size for n in range(graph_size)]]).transpose()
    for i in range(num_iter):
        evaporated_weight = 0
        probabilities_list = probabilities.T.tolist()[0]
        scaled_probabilities = []
        for prob in probabilities_list:
            scaled_probabilities.append(prob * (1 - eps))
            evaporated_weight += prob * eps
        scaled_probabilities_plus_evaporated_weight = [i + evaporated_weight/graph_size for i in scaled_probabilities]
        rounded_probabilities = [round(i, 4) for i in scaled_probabilities_plus_evaporated_weight]
        probabilities = np.array([rounded_probabilities]).transpose()
        # recalculate probabilties by multiplying graph matrix by probabilities vector
        new_probabilities = matrix.T * probabilities
        probabilities = new_probabilities

    # convert probabilities numpy vector to list
    probabilities_list = probabilities.T.tolist()[0]
    # convert probabilities list into mapping between node and its weight
    return dict(zip([x for x in range(graph_size)], probabilities_list))


def graph_15_1_left():
    ''' This method, should construct and return a DirectedGraph encoding the left example in fig 15.1
    Use the following indexes: A:0, B:1, C:2, Z:3 '''
    seed_data = {0: [1], 1: [2], 2: [3], 3: [3]}
    graph = DirectedGraph(4)
    graph.init_seed_data(seed_data)
    return graph

def graph_15_1_right():
    ''' This method, should construct and return a DirectedGraph encoding the right example in fig 15.1
    Use the following indexes: A:0, B:1, C:2, Z1:3, Z2:4'''
    seed_data = {0: [1], 1: [2], 2: [3], 3: [4], 4: [3]}
    graph = DirectedGraph(4)
    graph.init_seed_data(seed_data)
    return graph

def graph_15_2():
    ''' This method, should construct and return a DirectedGraph encoding example 15.2
        Use the following indexes: A:0, B:1, C:2, A':3, B':4, C':5'''
    pass

def extra_graph_1():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''
    seed_data = {0: [1, 9], 1: [2, 9], 2: [3, 9], 3: [4, 9], 4: [5, 9], 5: [6, 9], 6: [7, 9], 7: [8, 9], 8: [9], 9: [0]}
    graph = DirectedGraph(10)
    graph.init_seed_data(seed_data)
    return graph

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_1 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_1_weights = {0: 0.3176, 1: 0.14325, 2: 0.06855, 3: 0.0365, 4: 0.0228, 5: 0.0169, 6: 0.0144, 7: 0.0133, 8: 0.01285, 9: 0.35385}

def extra_graph_2():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''
    seed_data = {0: [1], 1: [2], 2: [3], 3: [4], 4: [5, 6], 5: [6, 4], 6: [4, 5], 7: [8], 8: [9], 9: [0]}
    graph = DirectedGraph(10)
    graph.init_seed_data(seed_data)
    return graph

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_2 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_2_weights = {0: 0.037, 1: 0.046, 2: 0.0537, 3: 0.0603, 4: 0.2848, 5: 0.2386, 6: 0.2386, 7: 0.0, 8: 0.0143, 9: 0.0265}


def facebook_graph(filename = "facebook_combined.txt"):
    ''' This method should return a DIRECTED version of the facebook graph as an instance of the DirectedGraph class.
    In particular, if u and v are friends, there should be an edge between u and v and an edge between v and u.'''
    graphData = []
    data = open(filename)
    lines = data.read().splitlines()
    for line in lines:
        graphData.append(line.split())
    new_graph = DirectedGraph(4031)
    for pair in graphData:
        node1 = int(pair[0])
        node2 = int(pair[1])
        new_graph.add_edge(node1, node2)
        new_graph.add_edge(node2, node1)
    return new_graph


# The code necessary for your measurements for question 8b should go in this function.
# Please COMMENT THE LAST LINE OUT WHEN YOU SUBMIT (as it will be graded by hand and we do not want it to interfere
# with the automatic grader).
def question8b():
    result = scaled_page_rank(facebook_graph(), 20)
    results_list = [[key, val] for key,val in result.items()]
    # write highest and lowest hundred nodes to highest.txt and lowest.txt
    lowest = sorted(results_list, key=lambda pair: pair[1])
    lowest_hundred = lowest[0:100]
    highest = list(reversed(lowest))
    highest_hundred = highest[0:100]
    f = open('highest.txt','a')
    f.write('Highest:')
    for x in highest_hundred:
        f.write('\n' + 'node: {} weight {}'.format(x[0], x[1]))
    f.close()
    g = open('lowest.txt','a')
    g.write('Lowest:')
    for y in lowest_hundred:
        g.write('\n' + 'node: {} weight {}'.format(y[0], y[1]))
    g.close()

question8b()
