from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabelas import Receita, Ingrediente

engine = create_engine("sqlite:///banco.db", echo=True)
base = declarative_base()

def busca_ingrediente_por_nome(nome):
    Session = sessionmaker(bind=engine)
    session = Session()
    ingrediente = session.query(Ingrediente).filter_by(nome=nome).first()
    session.close()
    return ingrediente

def busca_ingredientes_da_receita(nome_receita):
    Session = sessionmaker(bind=engine)
    session = Session()
    # Buscar a receita pelo nome
    receita = session.query(Receita).filter_by(nome=nome_receita).first()
    if receita:
        ingredientes = receita.ingredientes  # Acessa os ingredientes relacionados
        session.close()
        return ingredientes
    else:
        session.close()
        return None
