import sqlite3

class DataBase:
    def __init__(self, banco = None): #cria o banco de dados
        self.connect = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.connect = sqlite3.connect(banco)
            self.cursor = self.connect.cursor()
            print("Conexão Estabelecida!")

        except sqlite3.Error as e:
            print("Erro de Conexão!")


    def criar_tabelas(self):
        cursor = self.cursor
        cursor.execute("""CREATE TABLE Tarefas(
            ID INTEGER PRIMARY KEY autoincrement,
            NomeEvento TEXT NOT NULL,
            Prazo DATE NOT NULL,
            Prioridade TEXT NOT NULL,
            Obs TEXT,
            Status TEXT,
            PalavraChave TEXT)""")
        
db = DataBase("user.db")

db.criar_tabelas()