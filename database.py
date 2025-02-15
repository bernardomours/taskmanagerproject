import sqlite3

# 📌 Criar o banco de dados e a tabela se não existirem
def criar_banco():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            observacoes TEXT,
            status TEXT NOT NULL,
            palavra_chave TEXT
        )
    """)

    conexao.commit()
    conexao.close()


# 📌 Função para adicionar uma nova tarefa ao banco de dados
def inserir_tarefa(nome, data, prioridade, observacoes, status, palavra_chave):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tarefas (nome, data, prioridade, observacoes, status, palavra_chave)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, data, prioridade, observacoes, status, palavra_chave))

    conexao.commit()
    conexao.close()


# 📌 Função para listar todas as tarefas
def listar_tarefas():
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    conexao.close()
    return tarefas


# 📌 Função para atualizar uma tarefa existente
def atualizar_tarefa(id_tarefa, nome, data, prioridade, observacoes, status, palavra_chave):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET nome = ?, data = ?, prioridade = ?, observacoes = ?, status = ?, palavra_chave = ?
        WHERE id = ?
    """, (nome, data, prioridade, observacoes, status, palavra_chave, id_tarefa))

    conexao.commit()
    conexao.close()


# 📌 Função para excluir uma tarefa
def excluir_tarefa(id_tarefa):
    conexao = sqlite3.connect("tarefas.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))

    conexao.commit()
    conexao.close()

# def atualizar_edicao(id_tarefa,nova_tarefa):
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
#     cursor.execute("UPDATE tarefas SET descricao = ? WHERE id = ?", (id_tarefa, nova_tarefa ))
#     conexao.commit()
#     conexao.close()
    

# 📌 Executar a criação do banco de dados ao rodar o arquivo
if __name__ == "__main__":
    criar_banco()
    print("Banco de dados e tabela criados com sucesso!")




# import sqlite3

# def inicializar_banco():
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS tarefas (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             data TEXT NOT NULL,
#             prioridade TEXT NOT NULL,
#             observacoes TEXT,
#             status TEXT NOT NULL,
#             palavra_chave TEXT 
#         )
#     ''')
#     conexao.commit()
#     conexao.close()

# def listar_tarefas(status=None):
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
#     if status:
#         cursor.execute("SELECT * FROM tarefas WHERE status = ?", (status,))
#     else:
#         cursor.execute("SELECT * FROM tarefas")
#     tarefas = cursor.fetchall()
#     conexao.close()
#     return tarefas

# def adicionar_tarefa(nome, data, prioridade, observacoes, status="Pendente",palavra_chave):
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
#     cursor.execute("INSERT INTO tarefas (nome, data, prioridade, observacoes, status, palavra_chave) VALUES (?, ?, ?, ?, ?, ?)",
#                    (nome, data, prioridade, observacoes, status, palavra_chave))
#     conexao.commit()
#     conexao.close()

# def excluir_tarefa(id_tarefa):
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
#     cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
#     conexao.commit()
#     conexao.close()

# def atualizar_tarefa(nome, data, prioridade, observacoes, status, palavra_chave):
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
#     cursor.execute("""
#         UPDATE tarefas
#         SET nome = ?, data = ?, prioridade = ?, observacoes = ?, status = ?, palavra_chave = ?
#         WHERE id = ?
#     """, (nome, data, prioridade, observacoes, status))
#     conexao.commit()
#     conexao.close()

# # Inicializa o banco ao rodar o script
# if __name__ == "__main__":
#     inicializar_banco()

# def inserir_tarefa(nome, data, prioridade, obs, status, palavra_chave):
#     conexao = sqlite3.connect("tarefas.db")
#     cursor = conexao.cursor()
    
#     cursor.execute("""
#         INSERT INTO tarefas (nome, data, prioridade, observacoes, status, palavra_chave)
#         VALUES (?, ?, ?, ?, ?, ?)
#     """, (nome, data, prioridade, obs, status, palavra_chave))
    
#     conexao.commit()
#     conexao.close()


