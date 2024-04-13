class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self._codiceInsegnamento = codins
        self._crediti = crediti
        self._nome = nome
        self._periodo = pd

    def __str__(self):
        return f"{self._nome} ({self._codiceInsegnamento})"
