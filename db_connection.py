import os
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

driver = os.getenv('driver')
login = os.getenv('login')
password = os.getenv('password')
database = os.getenv('database')
DSN = f"{driver}://{login}:{password}@localhost:5432/{database}"
# DSN = 'postgresql://postgres:01892684@localhost:5432/test'
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()