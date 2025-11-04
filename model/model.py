from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        query = "SELECT * FROM automobile"
        result = []

        try:
            cnx = get_connection()
            if cnx is None:
                print("Errore: Impossibile connettersi al database.")
                return None

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)

            for row in cursor.fetchall():
                auto = Automobile(
                    row['codice'],
                    row['marca'],
                    row['modello'],
                    row['anno'],
                    row['posti'],
                    row['disponibile']
                )
                result.append(auto)

            cursor.close()
            cnx.close()
            return result

        except Exception as err:
            print(f"Errore nella lettura dal database: {err}")
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO

        query = """SELECT * 
                   FROM automobile
                   WHERE modello = %s"""
        result = []
        try:
            cnx = get_connection()
            if cnx is None:
                return None

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (modello,))

            for row in cursor.fetchall():
                auto = Automobile(row['codice'],
                                  row['marca'],
                                  row['modello'],
                                  row['anno'],
                                  row['posti'],
                                  row['disponibile'])
                result.append(auto)

            cursor.close()
            cnx.close()
            return result
        except Exception as err:
            print(f"Errore nella lettura dal database: {err}")
            return None

