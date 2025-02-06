from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from insert import adiciona_ingrediente, adiciona_receita
from get import busca_ingrediente_por_nome, busca_ingredientes_da_receita
from update import reduzir_estoque_por_receita


engine = create_engine("sqlite:///banco.db", echo=True)
base = declarative_base()



ingrediente1 = busca_ingrediente_por_nome('Açúcar')
ingrediente2 = busca_ingrediente_por_nome('Chocolate em pó')
print(f"{ingrediente1.nome}, {ingrediente2.nome}")

reduzir_estoque_por_receita("Doce de Chocolate", 2)
