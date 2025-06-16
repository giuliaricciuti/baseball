import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._team = None

    def handleCreaGrafo(self, e):
        self._model.creaGrafo(self._team)
        print("grafo")
        self.fillDDAnni()
        self._view.update_page()

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def fillDDTeam(self):
        for t in self._model.getAllTeams():
            self._view._ddSquadra.options.append(
                ft.dropdown.Option(text = t.name, data = t, on_click = self.readDDTeam)
            )

    def fillDDAnni(self):
        anni = self._model.getAllYears(self._team)
        for t in anni:
            self._view._ddAnno.options.append(
                ft.dropdown.Option(text = t, data = t, on_click = self.readDDAnno)
            )

    def readDDTeam(self, e):
        if e.control.data is None:
            self._team = None
        else:
            self._team = e.control.data
        print(self._team)

    def readDDAnno(self, e):
        if e.control.data is None:
            self._anno = None
        else:
            self._anno = e.control.data
        print(self._anno)