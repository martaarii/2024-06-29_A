import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._album = None
        self._album2 = None

    def handle_grafo(self, e):
        self._view.txt_result.controls.clear()
        numero = self._view.txt_num.value
        if numero is None or numero == "" or numero == 0:
            self._view.create_alert("Inserire un numero maggiore di 0")
            return
        self._model.creaGrafo(numero)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato"))
        self.fillDD()
        self._view.update_page()

    def fillDD(self):
        album = self._model.getNodes()
        ordinaLista = sorted(album, key=lambda x: x.Title, reverse=False)
        for a in ordinaLista:
            self._view.dd_album.options.append(ft.dropdown.Option(
                data=a, key=a.AlbumId, text=a.Title, on_click=self._readAlbum))
            self._view.dd_album2.options.append(ft.dropdown.Option(
                data=a, key=a.AlbumId, text=a.Title, on_click=self._readAlbum2))
        self._view.update_page()
    def _readAlbum(self,e):
        print("read_album called ")
        self._album = e.control.data
    def _readAlbum2(self,e):
        print("read_album called ")
        self._album2 = e.control.data

    def handle_percorso(self,e):
        album1 = self._album
        album2 = self._album2
        soglia = self._view.txt_soglia.value
        self._view.txt_result.controls.clear()
        if soglia is None or soglia == "":
            self._view.create_alert("Selezionare una soglia")
            return
        if album1 is None or album2 is None:
            self._view.create_alert("Selezionare due album per poter calcolare il percorso")
            return
        self._model.creaDizionarioBilancio()
        percorso = self._model.calcola_percorso(soglia, album1, album2)
        if len(percorso) == 2:
            self._view.txt_result.controls.append(ft.Text(
                "Non esiste un percorso per questi due vertici"))
        else:
            for b in percorso:
                self._view.txt_result.controls.append(ft.Text(f"{b.Title}"))
        self._view.update_page()

    def handle_seleziona(self, e):
        album = self._album
        if album is None:
            self._view.create_alert("Selezionare un Album")
            return
        self._view.txt_result.controls.clear()
        self._model.creaDizionarioBilancio()
        bilanci = self._model.getBilanci(album)
        for b in bilanci:
            self._view.txt_result.controls.append(ft.Text(f"{b.Title}-->{bilanci[b]}"))
        self._view.update_page()
