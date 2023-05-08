from mysql import connector

class Db:
    #connexion bdd via le constructeur
    def __init__(self):
        self.db = connector.connect(
            user = 'root',
            password = '',
            database = "flasksql",
            host = 'localhost')
             
    def getUserByEmail(self, email):
        current_db = self.db.cursor()
        req = "SELECT mail, password FROM users WHERE mail = %s"
        data = (email,)
        current_db.execute(req, data)
        result = current_db.fetchall()
        data = []
        
        for email, password in result:
            data.append(email)
            data.append(password)
        return data

    
    def insertUser(self, lastname, firstname, email, password):
        current_db = self.db.cursor()
        req = "INSERT INTO users (nom, prenom, mail, password) VALUES (%s, %s, %s, %s)"
        user_data =(lastname, firstname, email, password)
        current_db.execute(req, user_data)
        self.db.commit()
    
    #fermeture de la connexion
    def __del__(self):
        self.db.close()