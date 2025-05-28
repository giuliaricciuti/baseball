import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._squadra = None

    def handleCreaGrafo(self, e):
        self._model.buildGraph()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text
                                               (f"Grafo creato con {self._model.getNum()[0]} vertici "
                                                f"e {self._model.getNum()[1]} archi"))
        self._view.update_page()

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def fillDD(self, dd: ft.dropdown):
        anni = self._model.getAnni()
        for a in anni:
            dd.options.append(ft.dropdown.Option(text=a, data=a, on_click=self.readDD))

    def readDD(self, e):
        if e.control.data is None:
            self._anno = None
        else:
            self._anno = e.control.data
            self._view._txtOutSquadre.controls.clear()
            squadre = self._model.getSquadreAnni(self._anno)
            for s in squadre:
                self._view._txtOutSquadre.controls.append(ft.Text(s))
                self._view._ddSquadra.options.append(ft.dropdown.Option(
                    data=s, text=s.teamCode, on_click=self.readDDSquadra
                ))
            self._view.update_page()

    def readDDSquadra(self, e):
        if e.control.data is None:
            self._squadra = None
        else:
            self._squadra = e.control.data


