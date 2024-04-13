# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

class CorsoDao:

    def __init__(self):
        self.dbConnect = DBConnect()

    def get_corsi(self):
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """SELECT * FROM corso"""
        cursor.execute(query)
        corsi = []
        for row in cursor:
            corsi.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return corsi

    def get_iscritti(self, corso):
        cnx = self.dbConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente, iscrizione WHERE studente.matricola=iscrizione.matricola AND iscrizione.codins=%s"""
        cursor.execute(query, (corso, ))
        studenti = []
        for row in cursor:
            studenti.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return studenti