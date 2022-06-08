import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation


def si():
    i = 0
    n = 1
    
    with open("simple.stp", "r") as fa:
        f = fa.read().split()
        while f[i - 1 + n] != 'EOF':
            n = 0
            i = i + 1
            if f[i - 1].lower() == 'nodes':
                a = [ [] for i in range(int(f[i]))]
            if f[i - 1] == 'A' or f[i - 1] == 'E' :
                print(i)
                a[int(f[i])].append(int(f[i+1])) 
                a[int(f[i])].append(int(f[i+2]))
        return a

def vv():
    i = 1
    n = 1
    a = []
    with open("simple.stp", "r") as fa:
        f = fa.read().split()
        while f[i - 1 + n] != 'EOF':
            n = 0
            i = i + 1
            if f[i - 1] == 'A' :         
                a.append((int(f[i]), int(f[i + 1]), int(f[i + 2])))
            else :
                continue 
    return a 


elist = vv()
print(si())
G = nx.DiGraph()
G.add_weighted_edges_from(elist)

labels = nx.get_edge_attributes(G, 'weight')
# упаковка графа на плоскость. существует несколько возможных конфигураций (layout)
#pos = nx.spring_layout(G, seed=7)
pos =  nx.planar_layout(G) 
fig, ax = plt.subplots(figsize=(len(elist), 1))
def update(idx):
    ax.clear()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_edges(
        G, pos, edgelist=[elist[idx]], width=1, alpha=0.5, edge_color="r", style="dashed", ax=ax
    )

    nx.draw_networkx_edges(
        G, pos, edgelist=elist[:idx] + elist[idx + 1:], width=1, edge_color="b", ax=ax
    )

    # рендер меток вершин
    nx.draw_networkx_labels(G, pos, font_size=5, font_family="sans-serif", ax=ax)

    # рендер меток рёбер
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax, label_pos=0.6)

    ax.set_title(f'Frame {idx}')

ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(elist), interval=1000, repeat=True)
plt.show()
