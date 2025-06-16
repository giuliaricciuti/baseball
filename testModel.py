from database.DAO import DAO
from model.model import Model

m = Model()
m.creaGrafo('Chicago Cubs')
print(m.getNum())
print(m.getDettagli(2000))