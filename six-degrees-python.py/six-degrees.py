import sys
from collections import deque
from collections import Counter
from typing import Any
import heapq

def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


'''
graf 1:
V = {(tt04, D, 7.0), (nm04, Dave)}
E = {(tt04, nm04)}

Adjacent list representasjon
{
    skuespiller_til_film = {nm04: [tt04], nm01: [tt01, tt02], nm02: [tt01, tt03], nm03: [tt01, tt03]}

    film_til_skuespiller = {tt04: [nm04], tt01: [nm01, nm02], tt02: [nm01, nm03], tt03: [nm02, nm03]}
}

V = {V1, V2, V3, V4, ..., Vn}
E = {(V1, V2), ..., (V1, Vk), ..., (Vn, Vm)} for n, m, k in Nat
'''

class Skuespiller:
    def __init__(self, id: int, navn: str):
        self.id = id
        self.navn = navn

class Film:
    def __init__(self, id: int, tittel: str, rating: float):
        self.id = id
        self.tittel = tittel
        self.rating = rating


alice = Skuespiller("nm01", "Alice")
bob   = Skuespiller("nm02", "Bob")
carol = Skuespiller("nm03", "Carol")
dave  = Skuespiller("nm04", "Dave")
A = Film("tt01", "A", 5.0)
B = Film("tt02", "B", 9.0)
C = Film("tt03", "C", 9.0)
D = Film("tt04", "D", 7.0)

g = {
    alice: [A, B], bob: [A, C], carol: [B, C], dave: [D],
    A: [alice, bob], B: [alice, carol], C: [bob, carol], D: [dave],
}

def adjacencyToSet(graph: dict):
    '''
    INPUT: graph, in the form of an adjacency list. For example
    g = {
        A: [B, C], 
        B: [A], 
        C: [A], : 
        D: [E], 
        E: [D]
    }
    OUTPUT: The set of nodes in the graph, and the set of edges in the graph
    ------------------------------------------------------------------------
    ASSUMPTION:
    1) the graph is undirected

    ''' 
    V = set()
    E = set()
    for key, values in graph.items():
        V.add(key)
        for value in values:
            edge = (min(key, value, key = lambda x: x.id), max(key, value, key = lambda x: x.id))
            E.add(edge)
    return V, E

def setToAdjacency(nodes: set, edges: set):
    adjacencyList = {node: [] for node in nodes}
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList


def DFSVisit(g: dict, s: Skuespiller | Film, visited: set):
    component = set()
    stack = deque()
    stack.append(s)
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            if isinstance(v, Skuespiller):
                component.add(v)
            for u in g[v]:
                if u not in visited:
                    stack.append(u)
    return component


def getComponents(g: dict):
    V, E = adjacencyToSet(g)
    visited = set()
    components = []
    for node in V:
        if isinstance(node, Skuespiller) and node not in visited:
            components.append(DFSVisit(g, node, visited))

    length_counts = Counter(len(sublist) for sublist in components)
    print(len(length_counts))
    for key, val in length_counts.items():
        print(f'There are {val} components of size {key}')

# Here is the second part: six degrees of IMDB

def BFSVisit(G: dict, s: Skuespiller | Film, visited: set):
    V, E = adjacencyToSet(G)
    visited.add(s)
    queue = deque()
    queue.append(s)
    while queue:
        u = queue.popleft()
        for (u, v) in E:
            if v not in visited:
                visited.add(v)
                queue.append(v)


def BFSFull(G: dict):
    V, E = adjacencyToSet(G)
    visited = set()
    for v in V:
        if v not in visited:
            BFSVisit(G, v, visited)


# We want to find the path from node a to node b

def ShortestPath_BFS(G: dict, a: Skuespiller, b: Skuespiller):
    '''
    INPUT: 
    1) G: The graph of interest
    2) a: The id of the initial node
    3) b: The id of the final node
    ------------------------------------------------------------------------
    This function, will find the shortest path between the nodes with id called a and b, in graph G.
    ------------------------------------------------------------------------
    ASSUMPTIONS
    1) The graph is unconnected.  
    '''
    if a == b:
        return []

    visited = {a}
    stack = deque([a])
    parent = {a: None}
    while stack:
        current = stack.popleft()
        if current == b:
            break
        for v in G[current]:
            if v not in visited:
                visited.add(v)
                parent[v] = current
                stack.append(v)

    if b not in visited:
        return None
    path = []
    current = b
    while current is not None:
        path.append(current.id)
        current = parent[current]
    return path[::-1]


def weight(u: Film, v: Film):
    return 10 - v.rating if isinstance(v, Film) else 0

def chillestShortestPath(G: dict, a: Skuespiller, b: Skuespiller, w: Any):
    '''
    INPUT: 
    1) G: The graph of interest
    2) a: The id of the initial node
    3) b: The id of the final node
    4) w: The weight function assigned to the edges between nodes
    ------------------------------------------------------------------------
    This function, will find the "chillest" shortest path between the nodes with id called a and b, in graph G. Its implemented by treating 
    ------------------------------------------------------------------------
    ASSUMPTIONS:
    1) The graph is unconnected.  
    '''
    heap = [(0, 0, a)]
    dist = {a: 0}
    predecessors = {a: None}
    counter = 1
    while heap:
        d, _, current = heapq.heappop(heap)
        if current == b:
            break
        if d > dist[current]:
            continue
        for nbd in G[current]:
            dnew = d + w(current, nbd)
            if nbd not in dist or dnew < dist[nbd]:
                dist[nbd] = dnew
                predecessors[nbd] = current
                heapq.heappush(heap, (dnew, counter, nbd)) 
                counter += 1

    if b not in predecessors:
        return None
    path = []
    current = b
    while current is not None:
        path.append(current.id)
        current = predecessors[current]
    return path[::-1]


# Chilleste vei


def getMovies():
    M = int(input())
    movies = []
    for _ in range(M):
        tt, name, rating = input().split("\t")
        movies.append(Film(tt, name, float(rating)))
    return movies

def getActors():
    A = int(input())
    actors = []
    for _ in range(A):
        nm, name = input().split("\t")
        actors.append(Skuespiller(nm, name))
    return actors

def getEdges():
    E = int(input())
    edges = []
    for _ in range(E):
        edge1, edge2 = input().split("\t")
        edges.append((edge1, edge2))
    return edges

def getShortestPath():
    SP = int(input())
    sps = []
    for _ in range(SP):
        actor1, actor2 = input().split("\t")
        sps.append((actor1, actor2))
    return sps

def getChillShortestPath():
    CSP = int(input())
    csps = []
    for _ in range(CSP):
        actor1, actor2 = input().split("\t")
        csps.append((actor1, actor2))
    return csps


def finalOutput():
    movies = getMovies()
    actors = getActors()
    edges = getEdges()
    shortestPaths = getShortestPath()
    chillShortestPaths = getChillShortestPath()

    byId = {}
    for m in movies:
        byId[m.id] = m
    for a in actors:
        byId[a.id] = a

    nodeSet = set(movies) | set(actors)
    edgeSet = set()
    for tt, nm in edges:
        if tt in byId and nm in byId:
            edgeSet.add((byId[tt], byId[nm]))

    Graph = setToAdjacency(nodeSet, edgeSet)
    getComponents(Graph)
    for a, b in shortestPaths:
        path = ShortestPath_BFS(Graph, byId[a], byId[b])
        print("\t".join(path))
    for a, b in chillShortestPaths:
        path = chillestShortestPath(Graph, byId[a], byId[b], weight)
        print("\t".join(path))
        

finalOutput()

exit()

def main():
    debug("Dette er et eksempel på å printe debug info. Du kan slette denne linjen")

    M = int(input())
    for i in range(M):
        parts = input().split("\t");
        # parts består av [ttid, tittel, rating]

    A = int(input())
    for i in range(A):
        parts = input().split("\t");
        # parts består av [id, navn]

    E = int(input())
    for i in range(E):
        parts = input().split("\t");
        # parts består av [ttid, nmid]

    # Finn komponenter
    print(0) # antall linjer (bytt ut 0)
    # print en linje per komponentstørrelse

    Qs = int(input())
    for i in range(Qs):
        parts = input().split("\t");
        # parts består av [nmid₁, nmid₂]

        # Finn korteste vei og print ut på en linje

    Qc = int(input())
    for i in range(Qc):
        parts = input().split("\t");
        # parts består av [nmid₁, nmid₂]

        # Finn chilleste vei og print ut på en linje

main()
