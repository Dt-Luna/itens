import sqlite3
from model import Item
from typing import List

class ItemDAO:
    DB_NAME = 'estoque.db'

    @staticmethod
    def get_db_connection():
        conn = sqlite3.connect(ItemDAO.DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def adicionar(item: Item):
        conn = ItemDAO.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
            (item.descricao, item.quantidade)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listarTodos() -> List[Item]:
        conn = ItemDAO.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM itens ORDER BY id ASC")
        rows = cursor.fetchall()
        conn.close()
        return [
            Item(
                id=row['id'],
                descricao=row['descricao'],
                quantidade=row['quantidade']
            ) for row in rows
        ]

        
