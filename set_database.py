import sqlite3

conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    quantidade INTEGER NOT NULL 
);
""")

# caso seja necessário apagar as info do db:
# cursor.execute("DELETE FROM itens;")
# cursor.execute("DELETE FROM sqlite_sequence;")

conn.commit()
conn.close()
print('Banco de Dados criado com sucesso')