import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def listaCorsi(self):
        corsi = self._model.get_corsi()
        opzioni = []
        for corso in corsi:
            opzioni.append(ft.dropdown.Option(key=corso._codiceInsegnamento, text=corso.__str__()))
        return opzioni

    def handleCercaIscritti(self, e):
        if self._view.dropCorsi.value is None or self._view.dropCorsi.value == "":
            self._view.create_alert("Inserire il corso, PIRLA!!!")
            return
        else:
            iscritti = self._model.get_iscritti(self._view.dropCorsi.value)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} studenti!"))
            for stud in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{stud.__str__()}"))
            self._view.update_page()

    def handleCercaStudente(self, e):
        self._view.txtNome.value = ""
        self._view.txtCognome.value = ""
        if self._view.txtMatricola.value is None or self._view.txtMatricola.value == "":
            self._view.create_alert("Inserire la matricola, PIRLA!!!")
            return
        elif not self._view.txtMatricola.value.isnumeric():
            self._view.create_alert("la matricola è un numero a 6 cifre!")
            return
        elif self._model.get_studente(self._view.txtMatricola.value) == None:
            self._view.create_alert("Nun ce sta nisciuno con sta matricola, controlla pirla")
            return
        else:
            stud = self._model.get_studente(int(self._view.txtMatricola.value))
            self._view.txtNome.value = stud._nome
            self._view.txtCognome.value = stud._cognome
            self._view.update_page()

    def handleCercaCorsi(self, e):
        pass

    def handleIscrivi(self, e):
        pass