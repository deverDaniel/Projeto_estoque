from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from tabelas import Receita, receita_ingrediente

engine = create_engine("sqlite:///banco.db", echo=True)
base = declarative_base()


def reduzir_estoque_por_receita(nome_receita, quantidade_receitas):
    Session = sessionmaker(bind=engine)
    session = Session()
    # Buscar a receita pelo nome
    receita = session.query(Receita).filter_by(nome=nome_receita).first()
    if not receita:
        print("Receita não encontrada.")
        session.close()
        return False

    # Iterar pelos ingredientes da receita e reduzir o estoque
    try:
        for ingrediente in receita.ingredientes:
            # Obter a quantidade usada por unidade da receita
            quantidade_usada = session.query(receita_ingrediente).filter_by(
                receita_id=receita.id, ingrediente_id=ingrediente.id
            ).first().quantidade

            # Calcular o total a ser reduzido do estoque
            total_usado = quantidade_usada * quantidade_receitas

            # Reduzir do estoque atual do ingrediente
            if ingrediente.estoque_atual >= total_usado:
                ingrediente.estoque_atual -= total_usado
            else:
                print(f"Estoque insuficiente para o ingrediente {ingrediente.nome}.")
                session.close()
                return False

        # Salvar alterações no banco
        session.commit()
        print(f"Estoque atualizado para {quantidade_receitas} unidades da receita '{nome_receita}'.")
        session.close()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar estoque: {e}")
        session.close()
        return False
