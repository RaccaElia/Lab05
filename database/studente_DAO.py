# Add whatever it is needed to interface with the DB Table studente
from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class StudenteDao:

    def __init__(self):
        self.dbConnect = DBConnect()

    def get_studente(self, matricola):
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente WHERE studente.matricola=%s"""
        cursor.execute(query, (matricola,))
        stud = cursor.fetchone()
        if stud == None:
            return None
        studente = Studente(stud["matricola"], stud["cognome"], stud["nome"], stud["CDS"])
        cursor.close()
        cnx.close()
        return studente

    def get_corsi_studente(self, matricola):
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM iscrizione, corso WHERE iscrizione.matricola=%s AND iscrizione.codins=corso.codins"""
        cursor.execute(query, (matricola,))
        corsi = []
        for row in cursor:
            corsi.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return corsi