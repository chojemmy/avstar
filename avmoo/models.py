from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql://root@localhost/avmoo?charset=utf8')
Base = declarative_base()

class Starinfo(Base):
    __tablename__ = 'starinfo'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    birthday = Column(String(64))
    height = Column(String(64))


if __name__ == '__main__':
    Base.metadata.create_all(engine)


