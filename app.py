import streamlit as st
from controller import ItemController

controller = ItemController()

st.title("Cadastro e Listagem de Itens")

st.header("Cadastrar novo item")
descricao = st.text_input("Descrição do item")
quantidade = st.number_input("Quantidade", min_value=1, step=1)

if st.button("Cadastrar"):
    if descricao and quantidade > 0:
        controller.criarItem(descricao, int(quantidade))
        st.success("Item cadastrado com sucesso!")
        st.experimental_rerun()
    else:
        st.error("Preencha todos os campos corretamente.")

st.header("Itens cadastrados")
itens = controller.obterTodosOsItens()
if itens:
    for item in itens:
        st.write(f"ID: {item.id} | Descrição: {item.descricao} | Quantidade: {item.quantidade}")
else:
    st.info("Nenhum item cadastrado ainda.")