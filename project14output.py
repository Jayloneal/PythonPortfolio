import networkx as nx
import matplotlib.pyplot as plt
import random 

# Define the grid size
grid_size = 10

# Generate the grid graph
G = nx.grid_2d_graph(grid_size, grid_size)

# Assign random weights to edges
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 10)

# Select start and finish points
start = (0, 0)
finish = (grid_size - 1, grid_size - 1)

# Use Dijkstra's algorithm to find the shortest path
path = nx.dijkstra_path(G, start, finish, weight='weight')

# Draw the graph
pos = {(x, y): (y, -x) for x, y in G.nodes()}
nx.draw(G, pos, with_labels=True, node_size=700, node_color="w")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=3, alpha=0.5)
nx.draw_networkx_nodes(G, pos, nodelist=path, node_size=700, node_color="b")

# Highlight the shortest path
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=6, alpha=0.8, edge_color="r")

# Show weights
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#Display the graph
plt.axis('off')
plt.show()

# Notify the user about the shortest path found
print(f"The shortest path from {start} to {finish} is:")
print(path)

print("\nRun the game again to create a new random grid.")
