import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import drop_tables, create_tables, Publisher, Book, Shop, Stock, Sale
from settings import driver, login, password, database
import json


if __name__ == '__main__':
    DSN = f"{driver}://{login}:{password}@localhost:5432/{database}"
    engine = sq.create_engine(DSN)

    drop_tables(engine)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open('test_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    publisher_id = input('Введите идентификфтор издателя ')
    result = session.query(Book.title, Shop.name).join(Stock.book).join(Stock.shop).filter(Book.id_publisher == Publisher.id).all()











    session.close()



