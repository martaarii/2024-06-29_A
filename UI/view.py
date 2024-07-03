import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.dd_album = None
        self.btn_seleziona = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_num = None
        self.btn_grafo = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Album di Itunes", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW 1
        self.txt_num = ft.TextField(
            label="Numero canzoni",
            width=200,
            hint_text="Inserisci un numero di canzoni"
        )
        self.btn_grafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_grafo)
        row1 = ft.Row([self.txt_num, self.btn_grafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #row 2
        self.dd_album = ft.Dropdown(label="Album")
        self.btn_seleziona = ft.ElevatedButton(text="Stampa adiacenze", on_click=self._controller.handle_seleziona)
        row2 = ft.Row([self.dd_album, self.btn_seleziona],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        # ROW 3
        self.txt_soglia = ft.TextField(
            label="Numero canzoni",
            width=200,
            hint_text="Inserisci un ALTRO numero"
        )
        row3 = ft.Row([self.txt_soglia],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # row 4
        self.dd_album2 = ft.Dropdown(label="Album")
        self.btn_percorso = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handle_percorso)
        row4 = ft.Row([self.dd_album2, self.btn_percorso],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()