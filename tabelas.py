from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///banco.db", echo=True)
base = declarative_base()

receita_ingrediente = Table(
    'receita_ingrediente', base.metadata,
    Column('receita_id', Integer, ForeignKey('receitas.id'), primary_key=True),
    Column('ingrediente_id', Integer, ForeignKey('ingredientes.id'), primary_key=True),
    Column('quantidade', Float, nullable= False)
)

# Modelo Receita
class Receita(base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    ingredientes = relationship('Ingrediente', secondary=receita_ingrediente, lazy='subquery',
                                 backref='receitas')

# Modelo Ingrediente
class Ingrediente(base):
    __tablename__ = 'ingredientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    estoque_min = Column(Float, nullable=False)
    estoque_atual = Column(Float, nullable=False)
