import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from model.base import Base
from model.ativo import Ativo
from model.posicao import Posicao

db_path = "database/"

if not os.path.exists(db_path):
   os.makedirs(db_path)

db_url = 'sqlite:///%s/db.sqlite3' % db_path

engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
   create_database(engine.url) 

Base.metadata.create_all(engine)