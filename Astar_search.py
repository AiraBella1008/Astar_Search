import math
from heapq import heappush, heappop
import matplotlib.pyplot as plt

def astar(nodes, edges, start, goal, heuristic):
    open_heap = []
    heappush(open_heap, (heuristic(start), 0.0, start)) 
    came_from = {}
    g_scores = {n: math.inf for n in nodes}
    g_scores[start] = 0.0

    closed = set()

    while open_heap:
        f, g, current = heappop(open_heap)
        if current in closed:
            continue

        if current == goal:
           
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return g_scores[goal], path

        closed.add(current)

        for neighbor, cost in edges.get(current, []):
            tentative_g = g_scores[current] + cost
            if tentative_g < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                f_neighbor = tentative_g + heuristic(neighbor)
                heappush(open_heap, (f_neighbor, tentative_g, neighbor))

    return math.inf, []



nodes = {
    "Start": (0, 0),
    "Design": (2, 1),
    "Procure": (2, -1),
    "ImplementA": (4, 2),
    "ImplementB": (4, 0),
    "ImplementC": (4, -2),
    "Integrate": (6, 0.5),
    "Test": (8, 0.5),
    "Fixes": (9, -0.5),
    "Release": (10, 0),
}

edges = {
    "Start": [("Design", 3), ("Procure", 2)],
    "Design": [("ImplementA", 5), ("ImplementB", 3)],
    "Procure": [("ImplementB", 2), ("ImplementC", 4)],
    "ImplementA": [("Integrate", 3)],
    "ImplementB": [("Integrate", 2)],
    "ImplementC": [("Integrate", 3)],
    "Integrate": [("Test", 2)],
    "Test": [("Fixes", 2), ("Release", 3)],
    "Fixes": [("Release", 1)],
}

goal = "Release"
def h(node):
    (x1, y1) = nodes[node]
    (x2, y2) = nodes[goal]
    return math.hypot(x2 - x1, y2 - y1)


total_cost, path = astar(nodes, edges, "Start", goal, h)

print("A* result")
print("----------")
print(f"Path: {' -> '.join(path)}")
print(f"Total cost: {total_cost:.2f}")


path_edges = set()
for i in range(len(path) - 1):
    path_edges.add((path[i], path[i+1]))

plt.figure(figsize=(9, 5))

for u, nbrs in edges.items():
    x1, y1 = nodes[u]
    for v, w in nbrs:
        x2, y2 = nodes[v]

        if (u, v) in path_edges:
            arrow_style = dict(arrowstyle="->", lw=2.5, color="red")
        else:
            arrow_style = dict(arrowstyle="->", lw=1.0, color="gray")

        plt.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=arrow_style)

    
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        plt.text(mx, my, f"{w}", fontsize=8, color="blue")

g_scores = {n: math.inf for n in nodes}
g_scores["Start"] = 0.0
came_from = {"Start": None}

for i in range(1, len(path)):
    prev, curr = path[i-1], path[i]
    cost = [c for (nbr, c) in edges[prev] if nbr == curr][0]
    g_scores[curr] = g_scores[prev] + cost
    came_from[curr] = prev

for n, (x, y) in nodes.items():
    g = g_scores[n]
    h_val = h(n)
    f_val = g + h_val if g < math.inf else math.inf

    plt.scatter([x], [y], s=100, color="lightblue", edgecolors="black", zorder=3)
    plt.text(x + 0.15, y + 0.15, n, fontsize=9, fontweight="bold")

    if g < math.inf:
        plt.text(x - 0.2, y - 0.3, f"g={g:.1f}", fontsize=7, color="black")
        plt.text(x - 0.2, y - 0.5, f"h={h_val:.1f}", fontsize=7, color="black")
        plt.text(x - 0.2, y - 0.7, f"f={f_val:.1f}", fontsize=7, color="darkred")

plt.title("A* Graph with g(n), h(n), f(n) Labels\nShortest Path Highlighted", fontsize=12)
plt.axis("equal")
plt.axis("off")
plt.show()
