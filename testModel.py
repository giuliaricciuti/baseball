from database.DAO import DAO
from model.model import Model

# m = Model()
# m.creaGrafo("Philadelphia Athletics")
# print(m.getNum())
# print(m.handleDettagli(1910))
print(DAO.getPeso("Philadelphia Athletics", 1919, 1929))