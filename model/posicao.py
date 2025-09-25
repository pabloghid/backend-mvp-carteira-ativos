from datetime import datetime
from typing import Union

from sqlalchemy import Column, DateTime, Double, ForeignKey, Integer
from sqlalchemy.orm import relationship

from model import Base


class Posicao(Base):
    __tablename__ = "posicao"

    id = Column(Integer, primary_key=True)
    ativo_id = Column(Integer, ForeignKey('ativo.id'), unique=True)
    quantidade = Column(Integer)
    preco_medio = Column(Double(2))
    total_investido = Column(Double(2))
    dt_atualizacao = Column(DateTime, default=datetime.now())
    
    ativo = relationship("Ativo", back_populates="posicoes")

    def __init__(self, ativo_id:int, quantidade:int, preco_medio:float, total_investido:int, dt_atualizacao:Union[DateTime, None] = None):
        """
        Cria uma Posicao

        Arguments:
            ativo_id: id do ativo da tabela ativo
            quantidade: quantidade de ativos
            preco_medio: preço médio das compras
            total_investido: total investido no ativo
            dt_atualizacao: data de atualização
        """
        self.ativo_id = ativo_id
        self.quantidade = quantidade
        self.preco_medio = preco_medio
        self.total_investido = total_investido
        if dt_atualizacao:
            self.dt_atualizacao = dt_atualizacao