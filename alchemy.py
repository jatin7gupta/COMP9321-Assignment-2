from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///tahelka.db', echo=True)
Session = sessionmaker(bind=Engine)
