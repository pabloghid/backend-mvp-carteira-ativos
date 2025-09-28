from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base


class Ativo(Base):
    __tablename__ = "ativo"

    id = Column(Integer, primary_key=True)
    nome = Column(String(140))
    codigo_negociacao = Column(String(7))
    tipo = Column(String(25))
    
    posicoes = relationship("Posicao", back_populates="ativo")

    def __init__(self, nome:str, codigo_negociacao:str, tipo:str):
        """
        Cria um Ativo

        Arguments:
            nome: nome do ativo
            codigo_negociacao: código de negociação do ativo
            tipo: tipo de ativo
        """
        self.nome = nome
        self.codigo_negociacao = codigo_negociacao
        self.tipo = tipo
    
        