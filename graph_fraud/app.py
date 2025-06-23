# graph_fraud/app.py

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Graph Fraud Detector", layout="wide")
st.title("🕸️ Graph-Based Fraud Ring Detector")

st.markdown("This module identifies suspicious fraud rings using relationship graphs (e.g. IPs, reviews, transactions).")

# Step 1: Simulate a graph
G = nx.Graph()

users = [f"user_{i}" for i in range(1, 16)]
for user in users:
    G.add_node(user)

# Add suspicious relationships
edges = [
    ("user_1", "user_2"), ("user_2", "user_3"), ("user_3", "user_1"),  # Fraud triangle
    ("user_4", "user_5"), ("user_4", "user_6"), ("user_5", "user_6"),  # Another ring
    ("user_7", "user_8"), ("user_7", "user_9"),
    ("user_10", "user_11"), ("user_12", "user_13"), ("user_14", "user_15")
]

# Add random additional connections
edges += random.sample([(u1, u2) for u1 in users for u2 in users if u1 != u2], 10)

G.add_edges_from(edges)

# Step 2: Community Detection (Using connected components as a proxy)
communities = list(nx.connected_components(G))
suspicious_communities = [c for c in communities if len(c) >= 3]

# Step 3: Visualize
fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, ax=ax, node_size=500, node_color="skyblue")
nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.5)
nx.draw_networkx_labels(G, pos, ax=ax, font_size=10)

for i, community in enumerate(suspicious_communities, start=1):
    st.warning(f"🚩 Suspicious Ring #{i}: {', '.join(sorted(community))}")

st.pyplot(fig)
