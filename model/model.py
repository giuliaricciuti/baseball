import networkx as nx

from database.DAO import DAO
from model.team import Team


class Model:
    def __init__(self):
        self._squadre = []
        self._anno = None
        self._graph = nx.Graph()


    def buildGraph(self):
        self._graph.clear()
        self.idMapSquadre = {}
        for s in self._squadre:
            self.idMapSquadre[s.ID] = s
        self._graph.add_nodes_from(self._squadre)
        for u in self._graph.nodes:
            for v in self._graph.nodes:
                if u!=v:
                    pesoU = DAO.getPesoSquadra(u.ID, self._anno)
                    pesoV = DAO.getPesoSquadra(v.ID, self._anno)
                    self._graph.add_edge(u, v, weight = pesoU + pesoV)

    def getAnni(self):
        return DAO.getAllAnni()

    def getSquadreAnni(self, year):
        self._anno = year
        self._squadre= DAO.getSquadreAnno(year)
        return self._squadre

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def handleDettagli(self, ID):
        squadra = self.idMapSquadre[ID]
        adiacenti = self._graph.neighbors(squadra)
        archi = [(squadra, a, self._graph[squadra][a]['weight']) for a in adiacenti]
        archi.sort(key = lambda x: x[2], reverse=True)
        return archi

