from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ as env

db_name = env['POSTGRES_DB']
db_user = env['POSTGRES_USER']
db_pass = env['POSTGRES_PASSWORD']
db_host = env['DB_HOST']
db_port = env['DB_PORT']

# Database connection
engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

# Database session
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Database metadata
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()