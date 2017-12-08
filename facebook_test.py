from hw4 import DirectedGraph, scaled_page_rank, graph_15_1_left, graph_15_1_right, facebook_graph

def facebook_trial():
    result = scaled_page_rank(facebook_graph(), 20)
    results_list = [[key, val] for key,val in result.items()]
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


facebook_trial()
