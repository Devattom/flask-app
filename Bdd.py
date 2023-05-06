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
        req = "SELECT mail, password FROM users WHERE mail = %s"
        data = (email,)
        current_db.execute(req, data)
        result = current_db.fetchall()
        print(result)
        # data['email'] = result[0]
        # data['password'] = result[1]
        return result

    
    def insertUser(self, lastname, firstname, email, password):
        current_db = self.db.cursor()
        req = "INSERT INTO users (nom, prenom, mail, password) VALUES (%s, %s, %s, %s)"
        user_data =(lastname, firstname, email, password)
        current_db.execute(req, user_data)
        self.db.commit()
    

    def __del__(self):
        self.db.close()