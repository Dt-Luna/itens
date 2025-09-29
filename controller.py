from typing import List
from model import Item
from database import ItemDAO

class ItemController:

    @staticmethod
    def criarItem(descricao: str, quantidade: int):
        novo_item = Item(descricao=descricao, quantidade=quantidade)
        ItemDAO.adicionar(novo_item)

    def obterTodosOsItens(self) -> List[Item]:
        return ItemDAO.listarTodos()