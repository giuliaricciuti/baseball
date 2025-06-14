from database.DAO import DAO
from model.model import Model

m = Model()
m.getSquadreAnni(2015)
m.buildGraph()
for n in m.handleDettagli(2789):
    print(n[1], n[2])