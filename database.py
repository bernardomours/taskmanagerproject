import sqlite3

class DataBase:
    def __init__(self, name = 'system.db') -> None:
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
            
        except:
            pass
        
    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tarefas(
            
            TituloEvento TEXT,
            Prazo DATE,
            Prioridade TEXT,
            Observacoes TEXT,
            PalavraChave TEXT, 
            
            PRIMARY KEY(ID)      
            
            );
            
           """)
        
    def register_tasks(self):
        campos_table = "ID, NOME, DATA, PRIORIDADE, OBSERVAÇÕES, STATUS"
        
                