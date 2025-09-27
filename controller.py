from typing import List
from model import Item
import ItemDAO

class ItemController:
    def __init__(self):
        pass

    def criarItem(self, descricao: str, quantidade: int):
        novo_item = Item(descricao=descricao, quantidade=quantidade)
        ItemDAO.add_item(novo_item)

    def obterTodosOsItens(self) -> List[Item]:
        return ItemDAO.list_all_itens()