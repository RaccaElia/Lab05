import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.dropCorsi = ft.Dropdown(width=800, label="corso", options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear")])
        self.btnIscritti = ft.ElevatedButton(width=150, text="Cerca iscritti", on_click=self._controller.handleCercaIscritti)
        row1 = ft.Row([self.dropCorsi, self.btnIscritti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.txtMatricola = ft.TextField(width=250, label="matricola")
        self.txtNome = ft.TextField(width=350, label="nome", read_only=True)
        self.txtCognome = ft.TextField(width=350, label="cognome", read_only=True)
        row2 = ft.Row([self.txtMatricola, self.txtNome, self.txtCognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btnStudente = ft.ElevatedButton(width=150, text="Cerca studente", on_click=self._controller.handleCercaStudente)
        self.btnCorsi = ft.ElevatedButton(width=150, text="Cerca corsi", on_click=self._controller.handleCercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(width=150, text="Iscrivi", on_click=self._controller.handleIscrivi)
        row3 = ft.Row([self.btnStudente, self.btnCorsi, self.btnIscrivi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

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
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
