from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.sentiero import Sentiero


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    # TODO
    @staticmethod
    def read_rifugi():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ 
                SELECT *
                FROM rifugio
                    """
        try:
            cursor.execute(query)
            for row in cursor:
                rifugio = Rifugio(
                    id=row['id'],
                    nome=row['nome'],
                    localita=row['localita'],
                    )
                result.append(rifugio)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def read_sentieri():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ 
                SELECT *
                FROM connessione
                    """
        try:
            cursor.execute(query)
            for row in cursor:
                sentiero = Sentiero(
                    id=row['id'],
                    id_rifugio1=row['id_rifugio1'],
                    id_rifugio2=row['id_rifugio2'],
                    anno=row['anno'],
                )
                result.append(sentiero)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result