from mysql import connector

class Db:
    def __init__(self):
        self.db = connector.connect(
            user = 'root',
            password = '',
            database = "flasksql",
            host = 'localhost')
        
    def getData(self):
        current_db = self.db.cursor()

        req = 'SELECT * FROM users'

        current_db.execute(req)

        result = current_db.fetchall()

        retour = ''
        for ligne in result:
            retour += str(ligne)
        
        return retour
    
    def getUserByEmail(self, email):
        current_db = self.db.cursor()

        req = 'SELECT '
    

    def __del__(self):
        self.db.close()