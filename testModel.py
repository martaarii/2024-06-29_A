from model.model import Model
myModel = Model()

myModel.creaGrafo(18)

nodi = myModel.getNodes()
dizionario= myModel.creaDizionarioBilancio()
bilanci = myModel.getBilanci(nodi[1])

