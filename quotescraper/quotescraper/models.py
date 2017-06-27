import logging
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.types import ARRAY
import settings

DeclarativeBase = declarative_base()

def db_connect():
    db_url = URL(**settings.DATABASE)
    logging.info("Creating an SQLAlchemy engine at URL '{db_url}'".format(db_url=db_url))
    return create_engine(db_url)

def create_quotes_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    
class Quote(DeclarativeBase):
    __tablename__ = "quotes"
    
    id = Column(Integer, primary_key=True)
    text = Column('text', String)
    author = Column('author', String)
    tags = Column('tags', ARRAY(String))