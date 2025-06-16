import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()

    def creaGrafo(self, team):
        self._anni = DAO.getYearsTeam(team)
        self._graph.add_nodes_from(self._anni)
        self.addEdges(team)

    def addEdges(self, team):
        anni = list(self._graph.nodes)
        res = []
        for a in anni:
            pesoA = DAO.getPeso(a, team)
            res.append((a, pesoA))
        for i in range(len(res)):
            for j in range(i+1, len(res)):
                # peso può essere zero, va bene
                self._graph.add_edge(res[i][0], res[j][0], weight=abs(res[i][1] - res[j][0]))

    def getDettagli(self, anno):
        result = []
        for n in self._graph.neighbors(anno):
            peso = self._graph[anno][n]['weight']
            result.append((n, peso))
        result.sort(key = lambda x:x[1])
        return result

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def fillDDTeams(self):
        pass

    def fillDDYears(self):
        pass