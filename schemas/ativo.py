from pydantic import BaseModel
from typing import Optional, List
from model.ativo import Ativo

def listar_ativos(ativos: List[Ativo]):
    """ 
    Retorna uma lista de ativos
    """
    result = []
    for ativo in ativos:
        result.append({
            "id": ativo.id,
            "nome": ativo.nome,
            "codigo_negociacao": ativo.codigo_negociacao,
            "tipo": ativo.tipo
        })

    return {"ativos": result}

class AtivoSchema(BaseModel):
    """ 
    Define como um novo ativo a ser inserido deve ser representado
    """
    id: int
    nome: str
    codigo_negociacao: str
    tipo: str

class ListagemAtivosSchema(BaseModel):
    """
      Define como uma listagem de Ativos será retornada.
    """
    ativos:List[AtivoSchema]