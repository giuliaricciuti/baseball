import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._years = []

    def creaGrafo(self, team):
        self._graph.clear()
        self._years = DAO.getAllYears(team)
        self._graph.add_nodes_from(self._years)
        self.addEdges(team)

    def addEdges(self, team):
        for a1 in self._graph.nodes:
            for a2 in self._graph.nodes:
                if a1!=a2:
                    peso = DAO.getPeso(team, a1, a2)
                    self._graph.add_edge(a1, a2, weight=peso)

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def handleDettagli(self, anno):
        res = []
        for a in self._graph.neighbors(anno):
            peso = self._graph[anno][a]["weight"]
            if peso[0]!=0:
                res.append((a, peso[0]))
        res.sort(key=lambda x:x[1], reverse=True)
        return res

    def getAllTeams(self):
        return DAO.getAllTeams()

    def getAllYears(self, team):
        return DAO.getAllYears(team)