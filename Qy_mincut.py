import sys
import random
import copy

def buildGraphfromFile(filename):
    graph = {}
    f = open(filename)
    for l in f:
        ### int list ###
        items = list(map(int,l.split()))
        ### find vertex ###
        vertex = items[0]
        ### store edges ###
        edges = items[1:]
        graph[vertex] = edges
    return graph

def computeMiniCut(graph):
    ### if we only have 2 vertex, problem is done ###
    if len(graph.keys()) <= 2:
        return graph
    
    ### Extract all edges from the graph ###
    E = []
    
    for k in graph.keys():
        for e in graph[k]:
            edge = (k,e)
            E.append(edge)
    print('E:',E)
    t = random.choice(E)
    v = t[0]
    v2merge = t[1]
    print('Random choice:',t)
    print('graph:',graph)
    print('v2merge:',v2merge)
    edge1 = graph[v]
    merged_vertex = v
    edge2 = graph[v2merge]
    
    ### find union of the 2 edges ###
    final_edges = list(filter(lambda x: x!= v and x!=v2merge, 
                        list(edge1 + edge2)))

    print('final_edges:',final_edges)
    ### delete the vertex which has been calculated ###
    del graph[v]
    del graph[v2merge]

    for k in graph.keys():
        cache_edge = []
        for edge in graph[k]:
            if edge == v or edge == v2merge:
                cache_edge.append(merged_vertex)
            else:
                cache_edge.append(edge)
        ### reset edges on current vertex without vertex deleted ###
        graph[k] = cache_edge

    graph[merged_vertex] = final_edges
    # print('graph:',graph)
    print('One is done')
    print('-'*100)
    return computeMiniCut(graph)
_test = 'small_test.txt'
gh = buildGraphfromFile(_test)
num_vertexes = len(gh.keys())
crossing_edges = 2 * num_vertexes

print('Original Graph:',gh)
i  =  30
minimun_cut = gh

while i > 0:
    _graph = copy.deepcopy(gh)
    print('='*10)
    local_minimum = computeMiniCut(_graph)
    print('local_minimum:',local_minimum)
    keys = local_minimum.keys()
    print('keys:',list(keys)[0])
    local_min_crossing_edges = len((local_minimum[list(keys)[0]]))
    # print(local_min_crossing_edges)
    # now count crossing edges
    if crossing_edges > local_min_crossing_edges:
        crossing_edges = local_min_crossing_edges
        minimun_cut = local_minimum
    i = i - 1
print('crossing_edges:',crossing_edges)
print ("crossing edges{0:2d}".format(crossing_edges))
print(minimun_cut)

