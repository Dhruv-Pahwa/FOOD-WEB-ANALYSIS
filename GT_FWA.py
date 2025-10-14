import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()

producers = ["Grass"]
primary_consumers = ["Rabbit", "Deer", "Frog"]
secondary_consumers = ["Snake", "Eagle"]
tertiary_consumers = ["Tiger", "Lion"]

all_nodes = producers + primary_consumers + secondary_consumers + tertiary_consumers
G.add_nodes_from(all_nodes)

edges = [
    ("Grass", "Rabbit"),
    ("Grass", "Deer"),
    ("Rabbit", "Snake"),
    ("Rabbit", "Eagle"),
    ("Frog", "Snake"),
    ("Deer", "Tiger"),
    ("Snake", "Eagle"),
    ("Snake", "Tiger"),
    ("Tiger", "Lion"),
    ("Eagle", "Lion")
]
G.add_edges_from(edges)

pos = nx.spring_layout(G, k=3, iterations=50, seed=42)

level_y = {
    "Grass": 2,
    "Rabbit": 1, "Deer": 1, "Frog": 1,
    "Snake": 0, "Eagle": 0,
    "Tiger": -1, "Lion": -1
}

for node, (x, y) in pos.items():
    pos[node] = (x, level_y[node])

plt.figure(figsize=(14, 10))

node_colors = []
for node in G.nodes():
    if node in producers:
        node_colors.append("#90EE90")
    elif node in primary_consumers:
        node_colors.append("#FFB6C1")
    elif node in secondary_consumers:
        node_colors.append("#87CEEB")
    else:
        node_colors.append("#FFA07A")

nx.draw_networkx_nodes(
    G, 
    pos, 
    node_color=node_colors,
    node_size=2000,
    edgecolors="black",
    linewidths=2,
    alpha=0.9
)

nx.draw_networkx_edges(
    G,
    pos,
    edge_color="#404040",
    arrows=True,
    arrowsize=25,
    arrowstyle='-|>',
    connectionstyle='arc3,rad=0.2',
    width=2,
    alpha=0.7,
    min_source_margin=15,
    min_target_margin=15
)

nx.draw_networkx_labels(
    G, 
    pos, 
    font_size=11, 
    font_weight='bold',
    font_family='sans-serif'
)

trophic_levels = {
    2: "Producers",
    1: "Primary Consumers", 
    0: "Secondary Consumers",
    -1: "Tertiary Consumers"
}

for level, label in trophic_levels.items():
    plt.text(1.2, level, label, fontsize=12, fontweight='bold', 
             ha='left', va='center', bbox=dict(boxstyle="round,pad=0.3", 
             facecolor="lightgray", alpha=0.7))

plt.text(-1.5, -1.5, 
         f"Graph Metrics:\n"
         f"Nodes: {G.number_of_nodes()}\n"
         f"Edges: {G.number_of_edges()}\n"
         f"Density: {nx.density(G):.3f}",
         fontsize=10,
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.8))

plt.title("Directed Ecosystem Food Web\n(Trophic Levels)", 
          fontsize=18, fontweight='bold', pad=20)
plt.axis("off")
plt.tight_layout()

legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#90EE90', 
               markersize=10, label='Producers'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFB6C1', 
               markersize=10, label='Primary Consumers'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#87CEEB', 
               markersize=10, label='Secondary Consumers'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFA07A', 
               markersize=10, label='Tertiary Consumers')
]

plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))

plt.show()

print("\n" + "="*50)
print("FOOD WEB ANALYSIS")
print("="*50)
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Graph density: {nx.density(G):.3f}")
print(f"Is strongly connected: {nx.is_strongly_connected(G)}")
print(f"Is weakly connected: {nx.is_weakly_connected(G)}")

print("\nTrophic levels:")
for level, organisms in enumerate([producers, primary_consumers, secondary_consumers, tertiary_consumers]):
    print(f"Level {level}: {', '.join(organisms)}")
    
print("\nTop predators (no outgoing edges):")
top_predators = [node for node in G.nodes() if G.out_degree(node) == 0]
print(f"{', '.join(top_predators)}")

print("\nBase organisms (no incoming edges):")
base_organisms = [node for node in G.nodes() if G.in_degree(node) == 0]
print(f"{', '.join(base_organisms)}")
