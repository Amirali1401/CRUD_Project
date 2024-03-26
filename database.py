from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship , sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db_user = 'postgres'
db_password = 'postgres'
db_host = 'db'
db_port = '5432'
db_name = 'postgres'

db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(db_url)
base = declarative_base()
session = sessionmaker(bind = engine)()


class Category(base):
      __tablename__ = 'categories'
      id = Column(Integer, primary_key=True)
      name = Column(String)
      # books = relationship("Book", backref="category")



class Book(base):
      __tablename__ = 'books'
      id = Column(Integer, primary_key=True)
      name = Column(String)


base.metadata.create_all(engine)


