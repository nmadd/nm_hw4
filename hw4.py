# Please enter here the netids of all memebers of your group (yourself included.)
authors = ['ncm64','netID2']

# Which version of python are you using? python 2 or python 3?
python_version = "python 3"

from random import randint
import numpy as np

# Important: You are NOT allowed to modify the method signatures (i.e. the arguments and return types each function takes).

# Implement the methods in this class as appropriate. Feel free to add other methods
# and attributes as needed.
# Assume that nodes are represented by indices between 0 and number_of_nodes - 1
class DirectedGraph:

    def __init__(self,number_of_nodes):
        # self.graph = {node: set([edges])}
        self.graph = {}
        self.matrix = None

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
        self.graph[origin_node].append(destination_node)

    def edges_from(self, origin_node):
        ''' This method shold return a list of all the nodes u such that the edge (origin_node,u) is
        part of the graph.'''
        return self.graph[origin_node]

    def check_edge(self, origin_node, destination_node):
        ''' This method should return true is there is an edge between origin_node and destination_node
        and destination_node, and false otherwise'''
        if destination_node in self.graph[origin_node]:
            return True
        else:
            return False

    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return len(self.graph.keys())

    def create_matrix(self):
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


# TODO: update to include SCALED ranking
def scaled_page_rank(graph, num_iter, eps = 1/7.0):
    ''' This method, given a directed graph, should run the epsilon-scaled page-rank
    algorithm for num-iter iterations and return a mapping (dictionary) between a node and its weight.
    In the case of 0 iterations, all nodes should have weight 1/number_of_nodes'''
    graph_size = graph.number_of_nodes()
    ending_nodes = []
    matrix = graph.create_matrix()

    # take a random walk of num_steps steps
    starting_node = randint(0, graph_size - 1)
    current_node = starting_node
    # initialize probabilities equally
    probabilities = np.array([[1/graph_size for n in range(graph_size)]]).transpose()
    print('initial probabilities: ', probabilities)
    for i in range(0, num_iter):
        print('iteration: ', i)
        print('starting node: ', starting_node)
        if i == num_iter - 1:
            ending_node = current_node
            ending_nodes.append(ending_node)
        edges = graph.edges_from(current_node)
        print('edges: ', edges)
        random_step = edges[randint(0, len(edges) - 1)]
        print('random step: ', random_step)
        current_node = random_step
        print('current node: ', current_node)
        new_probabilities = matrix.T * probabilities
        print('new probs', new_probabilities)
        probabilities = new_probabilities
        print('probabilities: ', probabilities)

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
    pass

def graph_15_2():
    ''' This method, should construct and return a DirectedGraph encoding example 15.2
        Use the following indexes: A:0, B:1, C:2, A':3, B':4, C':5'''
    pass

def extra_graph_1():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''
    pass

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_1 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_1_weights = {1 : 0, 2: 0, 3 : 0, 4: 0, 5 : 0, 6: 0, 7 : 0, 8: 0, 9 : 0}

def extra_graph_2():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''
    pass

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_2 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_2_weights = {1 : 0, 2: 0, 3 : 0, 4: 0, 5 : 0, 6: 0, 7 : 0, 8: 0, 9 : 0}


def facebook_graph(filename = "facebook_combined.txt"):
    ''' This method should return a DIRECTED version of the facebook graph as an instance of the DirectedGraph class.
    In particular, if u and v are friends, there should be an edge between u and v and an edge between v and u.'''
    pass


# The code necessary for your measurements for question 8b should go in this function.
# Please COMMENT THE LAST LINE OUT WHEN YOU SUBMIT (as it will be graded by hand and we do not want it to interfere
# with the automatic grader).
def question8b():
    pass
question8b()
