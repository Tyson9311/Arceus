from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config

Base = declarative_base()
engine = create_engine(Config.DB_URL)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

def init_db():
    Base.metadata.create_all(engine)

def get_user_bots(user_id):
    session = Session()
    # डेटाबेस लॉजिक
    session.close()
