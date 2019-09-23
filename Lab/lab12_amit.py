# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:37:11 2019

@author: Amit
"""

def build_graph(file_name,number_of_nodes):
    parent = [node_id for node_id in range(number_of_nodes)]
        
    # read from file and construct a graph
    f = open(file_name).readlines()
    
    edges = []
    for index,value in enumerate(f):
        node_list = value.strip().split(" ") # Second element is neighbor
        node = int(node_list[0])
        child = int(node_list[1])
        weight= int(node_list[2])
        edges.append((node, child, weight))
        # graph[node1].add_neighbour(node2)
    return parent, edges


def find(node_id):
    # The parent and node_id will be equal when that vertex is the root of 
    # the that tree (there can be multiple trees)
    if parent[node_id] != node_id: 
        parent[node_id] = find(parent[node_id])
    return parent[node_id]


def union(u,v,parent):
    # Make v's parent a child of u
    parent[find(v)] = u
    return parent


# =============== Main ================
parent, edges = build_graph("lab12_test_mst.txt",500)

# Testcase 
#parent = [i for i in range(6)]
#edges = [(0,1,1),(0,3,3),(1,2,2),(4,5,2)]

# Sort the edges so we pick the min. possible edge everytime
edges.sort(key=lambda x: x[2])

mst_weight = 0

for e_tup in edges:
    node1 = e_tup[0]
    node2 = e_tup[1]
    weight = e_tup[2]
    
    # if the two nodes do not belong to the same parent
    # then add this edge to the mst
    if find(node1) != find(node2):
        parent = union(node1,node2,parent)
        mst_weight += weight
        

print(mst_weight)
        