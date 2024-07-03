import networkx as nx
import copy
from database.DAO import DAO


class Model():
    def __init__(self):
        self._costBest = 0
        self.bilancio = {}
        self._solBest = []
        self._graph = nx.DiGraph()
        self._idMap = {}

    def creaGrafo(self, n):
        self.nodi = DAO.getAlbum(n)
        self._graph.add_nodes_from(self.nodi)
        self._idMap={}
        for v in self.nodi:
            self._idMap[v.AlbumId] = v
        self.addEdges()

    def addEdges(self):
        self._graph.clear_edges()
        for n1 in self._graph.nodes():
            for n2 in self._graph.nodes():
                if n1 != n2 and self._graph.has_edge(n1, n2) == False:
                    delta = n1.numCanzoni - n2.numCanzoni
                    if delta > 0:
                        self._graph.add_edge(n2, n1, weight=delta)

    def getNodes(self):
        nodi = list(self._graph.nodes)
        return nodi

    def calcola_percorso(self, soglia, a1, a2):
        self._costBest = 0
        self._solBest = []
        parziale = [a1]
        print(self.bilancio[a1.AlbumId])
        bilancioV0 = self.bilancio[a1.AlbumId]
        print(list(self._graph.neighbors(a1)))
        for v in list(self._graph.neighbors(a1)):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale, v, a2, int(soglia), bilancioV0)
                    parziale.pop()
        return self._solBest
    def ricorsione(self, parziale, v0, a2, soglia, bilV0):
        if parziale[-1] == a2:
            if len(parziale) > self._costBest:
                self._costBest = len(parziale)
                self._solBest = copy.deepcopy(parziale)

        for v in self._graph.nodes:
            if v in list(self._graph.neighbors(parziale[-1])):
                if v not in parziale and self.bilancio[v.AlbumId] >= bilV0:
                    edgWg = self._graph[v0][v]["weight"]
                    if edgWg > soglia:
                        parziale.append(v)
                        self.ricorsione(parziale, v0, a2, soglia,bilV0)
                        parziale.pop()
    def getCaratteristiche(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def creaDizionarioBilancio(self):
        self.bilancio = {}
        for n in self._graph.nodes:
            self.bilancio[n.AlbumId] = 0
            for bil in self._graph.predecessors(n):
                self.bilancio[n.AlbumId] += float(self._graph[bil][n]['weight'])
            for bil2 in self._graph.successors(n):
                self.bilancio[n.AlbumId] -= float(self._graph[n][bil2]['weight'])
        list(sorted(self.bilancio.items(), key=lambda item: item[1], reverse=True))
        return self.bilancio

    def getBilanci(self, nodo):
        predecessori = list(self._graph.predecessors(nodo))
        successori = list(self._graph.successors(nodo))
        # NOTA BENE: successors e predecessors restituiscono iteratori => convertire in liste
        bilanci_nodo = {}
        for id in self.bilancio:
            vertice = self._idMap[id]
            if vertice in predecessori or vertice in successori:
                bilanci_nodo[vertice] = self.bilancio[id]
        return bilanci_nodo