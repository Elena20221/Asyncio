from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PG_DSN= 'postgresql+asyncpg://admin:zvezda@127.0.0.1:5431/netlogy_asynk'
engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class SwapiPeople(Base):

     __tablename__ = 'people'

     id = Column(Integer, primary_key=True)
     birth_year = Column(String)
     eye_color = Column(String)
     films = Column(Text)
     gender = Column(String)
     hair_color = Column(String)
     height = Column(String)
     homeworld = Column(String)
     mass = Column(String)
     name = Column(String)
     skin_color = Column(String)
     species = Column(Text)
     starships = Column(Text)
     vehicles = Column(Text)




