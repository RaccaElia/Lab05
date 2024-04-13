class Studente:
    def __init__(self, matricola, cognome, nome, cds):
        self._matricola = matricola
        self._cognome = cognome
        self._nome = nome
        self._corsoDiStudi = cds

    def __str__(self):
        return f"{self._nome.upper()} {self._cognome.upper()} ({self._matricola})"