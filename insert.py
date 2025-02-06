from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabelas import Receita, Ingrediente, receita_ingrediente

engine = create_engine("sqlite:///banco.db", echo=True)
base = declarative_base()


def adiciona_ingrediente(nome, estoque_min, estoque_atual):
    Session = sessionmaker(bind=engine)
    session = Session()
    novo_ingrediente = Ingrediente(nome=nome, estoque_min=estoque_min, estoque_atual=estoque_atual)
    session.add(novo_ingrediente)
    session.commit()
    session.close()

def adiciona_receita(nome, ingredientes_quantidades):
    Session = sessionmaker(bind=engine)
    session = Session()
    nova_receita = Receita(nome=nome)
    session.add(nova_receita)
    session.flush()
    for ingrediente_id, quantidade in ingredientes_quantidades.items():
        session.execute(
            receita_ingrediente.insert().values(
                receita_id=nova_receita.id,
                ingrediente_id=ingrediente_id,
                quantidade=quantidade
            )
        )
    session.commit()
    session.close()
    print(f"Receita '{nome}' adicionada com sucesso.")
