import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._squadre = []
        self._graph = nx.Graph()


    def buildGraph(self):
        self._graph.clear()
        self._graph.add_nodes_from(self._squadre)
        for u in self._graph.nodes:
            for v in self._graph.nodes:
                if u!=v:
                    self._graph.add_edge(u, v)

    def getAnni(self):
        return DAO.getAllAnni()

    def getSquadreAnni(self, year):
        self._squadre= DAO.getSquadreAnno(year)
        return self._squadre

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()