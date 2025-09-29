from typing import List
from model import Item
import ItemDAO as db

class ItemController:

    @staticmethod
    def criarItem(descricao: str, quantidade: int):
        novo_item = Item(descricao=descricao, quantidade=quantidade)
        db.add_item(novo_item)

    @staticmethod
    def obterTodosOsItens() -> List[Item]:
        return db.list_all_itens()