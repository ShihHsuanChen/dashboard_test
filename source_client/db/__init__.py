from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


DB_PATH = '/home/jackchen/workspace/dashboard1/record.db'
conn_str = f'sqlite:///{DB_PATH}'

engine = create_engine(conn_str, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
