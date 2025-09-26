from pydantic import BaseModel
from typing import Optional, List
from model.posicao import Posicao
from datetime import datetime

class PosicaoSchema(BaseModel):
    """ 
    Define como um novo produto a ser inserido deve ser representado
    """
    ativo_id: int
    quantidade: int
    preco_medio: float
    total_investido: float
    dt_atualizacao: Optional[datetime] = None

class ListagemPosicoesSchema(BaseModel):
    """
      Define como uma listagem de Posições será retornada.
    """
    posicoes:List[PosicaoSchema]

class PosicaoViewSchema(BaseModel):
    """ 
    Define a visualização de uma posição
    """
    ativo_id: int
    quantidade: int
    preco_medio: float
    total_investido: float
    dt_atualizacao: Optional[datetime] = None

class PosicaoUpdateSchema(BaseModel):
    """ 
    Representação da edição de produto
    """
    ativo_id: Optional[int] = None
    quantidade: Optional[int] = None
    preco_medio: Optional[float] = None
    total_investido: Optional[float] = None
    dt_atualizacao: Optional[datetime] = None

class PosicaoPathSchema(BaseModel):
    """
    Deleta uma Posicao a partir do ID
    """
    posicao_id: int


class PosicaoDelSchema(BaseModel):
    """ 
    Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção.
    """
    message: str
    nome: str

def listar_posicoes(posicoes: List[Posicao]):
    """ 
    Retorna uma lista de posições
    """
    result = []
    for posicao in posicoes:
        result.append({
            "id": posicao.id,
            "nome": posicao.ativo.nome,
            "codigo_negociacao": posicao.ativo.codigo_negociacao,
            "quantidade": posicao.quantidade,
            "preco_medio": posicao.preco_medio,
            "total_investido": posicao.total_investido,
            "dt_atualizacao": posicao.dt_atualizacao.strftime("%d/%m/%Y") if posicao.dt_atualizacao else None,
        })

    return {"posicoes": result}

def listar_posicao(posicao: Posicao):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": posicao.id,
        "nome": posicao.ativo.nome,
        "codigo_negociacao": posicao.ativo.codigo_negociacao,
        "valor": posicao.quantidade,
        "preco_medio": posicao.preco_medio,
        "total_investido": posicao.total_investido,
        "dt_atualizacao": posicao.dt_atualizacao.strftime("%d/%m/%Y") if posicao.dt_atualizacao else None,
    }