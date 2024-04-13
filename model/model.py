from database.corso_DAO import CorsoDao
from database.studente_DAO import StudenteDao

class Model:
    def __init__(self):
        self.corsoDao = CorsoDao()
        self.studenteDao = StudenteDao()

    def get_corsi(self):
        return self.corsoDao.get_corsi()

    def get_iscritti(self, corso):
        return self.corsoDao.get_iscritti(corso)

    def get_studente(self, matr):
        return self.studenteDao.get_studente(matr)
