#!/usr/bin/python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

#generate graph 
G = nx.Graph() 
G.clear() 
G.add_weighted_edges_from([('0','1',2),('0','2',7),('1','2',3),('1','3',8),('1','4',5),('2','3',1),('3','4',4)]) 
 
#Info of nodes and edge 
edge_labels = nx.get_edge_attributes(G,'weight')  
labels={'0':'0','1':'1','2':'2','3':'3','4':'4'} 
 
#generate nodes position  
pos=nx.spring_layout(G)  
  
#draw nodes  
nx.draw_networkx_nodes(G,pos,node_color='g',node_size=500,alpha=0.8)  
 
#draw edges 
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5,edge_color=['b','r','b','r','r','b','r'])  
  
#draw lables of nodes  
nx.draw_networkx_labels(G,pos,labels,font_size=16)  
  
#deaw wheight of edges  
nx.draw_networkx_edge_labels(G, pos, edge_labels)  
 
#display graph 
plt.title('Wheited Graph') 
plt.axis('on') 
plt.xticks([]) 
plt.yticks([]) 
plt.show() 