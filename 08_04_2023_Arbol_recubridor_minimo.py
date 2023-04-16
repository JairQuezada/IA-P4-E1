import networkx as nx
import matplotlib.pyplot as plt
import random 

# Se crea un grafo con nx.Graph y a los vertices se le da un valor random
G = nx.Graph()
vertices = [random.randint(1,10)for _ in range(15)]
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
G.add_edge('A', 'B', weight=vertices[0])
G.add_edge('A', 'C', weight=vertices[1])
G.add_edge('A', 'D', weight=vertices[2])
G.add_edge('B', 'C', weight=vertices[3])
G.add_edge('B', 'F', weight=vertices[4])
G.add_edge('B', 'H', weight=vertices[5])
G.add_edge('C', 'D', weight=vertices[6])
G.add_edge('C', 'E', weight=vertices[7])
G.add_edge('C', 'H', weight=vertices[8])
G.add_edge('D', 'E', weight=vertices[9])
G.add_edge('E', 'H', weight=vertices[10])
G.add_edge('E', 'G', weight=vertices[11])
G.add_edge('F', 'H', weight=vertices[12])
G.add_edge('F', 'G', weight=vertices[13])
G.add_edge('H', 'G', weight=vertices[14])

# Se necesita conocer cual es el nodo inicial, en este caso se va a iniciar desde el nodo A
start_node = 'A'

# Se necesita saber en que nodos hemos estado previamente
visited_nodes = set()
distances = {node: float('inf') for node in G.nodes}
distances[start_node] = 0
previous_nodes = {node: None for node in G.nodes}

# Con el while hacemos que se ejecute el programa hasta que no queden nodos por visitar
while len(visited_nodes) != len(G.nodes):
    # Se busca el nodo con el cual se tiene menor distancia
    current_node = min((node for node in G.nodes if node not in visited_nodes), key=lambda node: distances[node])
    visited_nodes.add(current_node)
    for neighbor in G.neighbors(current_node):
        if neighbor not in visited_nodes:
            # Se checa si la distancia entre el nodo actual al nodo vecino es menor a la distancia ya recorrida
            if G[current_node][neighbor]['weight'] < distances[neighbor]:
                distances[neighbor] = G[current_node][neighbor]['weight']
                previous_nodes[neighbor] = current_node

# Se imprime el arbor parcial minimo y tambien decidimos que fuera a un nodo especifico, asi que este va al nodo G
partial_tree = nx.Graph()
for node, previous_node in previous_nodes.items():
    if previous_node is not None:
        partial_tree.add_edge(node, previous_node, weight=G[node][previous_node]['weight'])
path = nx.shortest_path(partial_tree, start_node, 'G')
print('Árbol parcial mínimo:', sorted(partial_tree.edges))
print('Peso total:', sum([G[node1][node2]['weight'] for node1, node2 in partial_tree.edges]))
print('Camino más corto desde a hasta g:', path)

# Se crea nuestro grafico con Networkx, en donde usamos los datos previamente creados
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='#03ac13')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5,edge_color='#795c34')
nx.draw_networkx_edges(partial_tree, pos, width=2.0, edge_color='#795c34')
labels = nx.get_edge_attributes(partial_tree, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.show()