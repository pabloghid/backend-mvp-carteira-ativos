from flask import redirect
from flask_openapi3 import Info, OpenAPI, Tag
from flask_cors import CORS

from sqlalchemy.exc import IntegrityError

from model import Session, Ativo, Posicao

from utils.utils import add_dados_iniciais

from schemas.posicao import (
    PosicaoSchema, ListagemPosicoesSchema, PosicaoViewSchema, 
    PosicaoUpdateSchema,PosicaoPathSchema, PosicaoDelSchema, 
    listar_posicoes, listar_posicao
)
from schemas.ativo import ListagemAtivosSchema, listar_ativos
from schemas.error import ErrorSchema

## Adição de dados iniciais
try:
    session = Session()
    if session.query(Ativo).first() is None:
        add_dados_iniciais(session, Ativo)
except Exception as e:
    print(e)

info = Info(title="Finances API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

posicoes_tag = Tag(name="posicoes", description="Posições de ativos")
ativos_tag = Tag(name="ativos", description="Ativos")
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get("/ativos", summary="Listagem de ativos", tags=[ativos_tag],
         responses={"200": ListagemAtivosSchema, "404": ErrorSchema})
def get_ativos():
    """
    Listar todos os ativos
    """

    session = Session()
    try:
        ativos = session.query(Ativo).all()

        if not ativos:
            return {"ativos": []}, 200
        else:
            return listar_ativos(ativos), 200
    finally:
        session.close()

@app.get("/posicoes", summary="Posições de ativos", tags=[posicoes_tag],
         responses={"200": ListagemPosicoesSchema, "404": ErrorSchema})
def get_posicoes():
    """
    Listar todas as posições
    """
    try:
        session = Session()
        posicoes = session.query(Posicao).all()

        if not posicoes:
            return {"posicoes": []}, 200
        else:
            return listar_posicoes(posicoes), 200
    finally:
        session.close()

@app.post('/posicao', summary="Adicionar posição de ativo", tags=[posicoes_tag],
          responses={"200": PosicaoViewSchema, "404": ErrorSchema})
def add_posicao(form: PosicaoSchema):
    """Adiciona uma nova Posição à base de dados

    Retorna uma representação das posições.
    """
    posicao = Posicao(
        ativo_id=form.ativo_id,
        quantidade=form.quantidade,
        preco_medio=form.preco_medio,
        total_investido=form.total_investido
        )
    
    try:
        session = Session()
        session.add(posicao)
        session.commit()
        return listar_posicao(posicao), 200

    except IntegrityError as e:
        error_msg = "Posição já salva na base de dados."
        session.rollback()
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item."
        session.rollback()
        return {"message": e}, 400

    finally:
        session.close()

@app.get("/posicao/<int:posicao_id>", summary="Posição de um ativo", tags=[posicoes_tag],
         responses={"200": PosicaoViewSchema, "404": ErrorSchema})
def get_posicao(path: PosicaoPathSchema):
    """
    Listar todas as posições
    """
    try:
        session = Session()
        posicao = session.query(Posicao).get(path.posicao_id)
        if not posicao:
            return {"posicao": {}}, 200
        else:
            return listar_posicao(posicao), 200
    finally:
        session.close()

@app.put("/posicao/<int:posicao_id>", summary="Atualizar posição", tags=[posicoes_tag],
        responses={"200": PosicaoViewSchema, "404": ErrorSchema})
def update_posicao(path: PosicaoPathSchema, form: PosicaoUpdateSchema):
    """
    Atualiza os dados de uma posição existente
    """
    session = Session()
    try:

        posicao = session.query(Posicao).get(path.posicao_id)
        print(posicao.quantidade)
        if not posicao:
            session.rollback()
            return {"error": "Posição não encontrada"}, 404

        if form.quantidade is not None:
            posicao.quantidade = form.quantidade
        if form.preco_medio is not None:
            posicao.preco_medio = form.preco_medio
        if form.total_investido is not None:
            posicao.total_investido = form.total_investido
        if form.ativo_id is not None:
            posicao.ativo_id = form.ativo_id

        session.commit()
        return listar_posicao(posicao), 200
    finally:
        session.close()

@app.delete('/posicao/<int:posicao_id>', summary="Deletar posição", tags=[posicoes_tag], 
            responses={"200": PosicaoDelSchema, "404": ErrorSchema})
def del_produto(path: PosicaoPathSchema):
    """
    Deleta uma posição pelo ID
    """
    session = Session()

    try:
        posicao = session.query(Posicao).get(path.posicao_id)

        if not posicao:
            session.rollback()
            session.commit()
            return {"message": "Posição não encontrada"}, 404
        
        nome_ativo = posicao.ativo.nome

        session.delete(posicao)
        session.commit()

        return {"message": f"Posição do ativo {nome_ativo} deletada com sucesso"}, 200

    finally:
        session.close()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)