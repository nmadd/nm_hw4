from hw4 import DirectedGraph, scaled_page_rank, graph_15_1_left, graph_15_1_right
import numpy as np

test = DirectedGraph(5)

for i in range(0, 5):
    test.add_node(i)

test.add_edge(0, 3)
test.add_edge(0, 4)
test.add_edge(1, 3)
test.add_edge(2, 0)
test.add_edge(2, 1)
test.add_edge(3, 2)
test.add_edge(4, 1)
test.add_edge(4, 0)
test.add_edge(4, 3)
test.add_edgeless_nodes()

# test.print_graph()
# print('Edges from 4:', test.edges_from(4))
# print('Number of nodes:', test.number_of_nodes())
# print('Scaled page rank:', scaled_page_rank(test, 50))
# test.create_matrix()

print(scaled_page_rank(graph_15_1_left(), 50))
print(scaled_page_rank(graph_15_1_right(), 50))
