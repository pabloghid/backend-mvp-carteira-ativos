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
    dt_atualizacao: Optional[datetime]

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
    dt_atualizacao: datetime

class PosicaoUpdateSchema(BaseModel):
    """ 
    Representação da edição de produto
    """
    ativo_id: Optional[int]
    quantidade: Optional[int]
    preco_medio: Optional[float]
    total_investido: Optional[float]
    dt_atualizacao: Optional[datetime]

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
            "nome": posicao.ativo.nome,
            "codigo_negociacao": posicao.ativo.codigo_negociacao,
            "valor": posicao.quantidade,
            "preco_medio": posicao.preco_medio,
            "total_investido": posicao.total_investido,
            "dt_atualizacao": posicao.dt_atualizacao.isoformat() if posicao.dt_atualizacao else None,
        })

    return {"produtos": result}

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
        "dt_atualizacao": posicao.dt_atualizacao.isoformat() if posicao.dt_atualizacao else None,
    }