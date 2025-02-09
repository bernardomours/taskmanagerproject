import sqlite3

class DataBase:
    def __init__(self, banco = None):
        self.connect = None
        self.cursor = None
        
        if banco:
            self.open(banco)
            
    def open(self, banco):
        try:
            self.connect = sqlite3.connect(banco)
            self.cursor = self.connect.cursor
            print("Conexão Estabelecida!")
            
        except sqlite3.Error as e:
            print("Erro de Conexão!")
            
            
db = DataBase("fun")        