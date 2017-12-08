from hw4 import DirectedGraph, scaled_page_rank, graph_15_1_left, graph_15_1_right, graph_15_2, extra_graph_1, extra_graph_2

print('Graph 15.1 Left: ', scaled_page_rank(graph_15_1_left(), 50))
print('Graph 15.1 Right: ', scaled_page_rank(graph_15_1_right(), 50))
print('Graph 15.2 : ', scaled_page_rank(graph_15_2(), 50))
print('Extra Graph 1: ', scaled_page_rank(extra_graph_1(), 50))
print('Extra Graph 2: ', scaled_page_rank(extra_graph_2(), 50))
