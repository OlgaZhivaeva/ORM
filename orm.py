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
    def tabulation(name, number):
        return ' '*(number - len(name))


    while True:
        publisher_id = int(input('Введите идентификатор издателя или 0 для выхода '))
        if publisher_id != 0:
            subq = session.query(Book.title, Shop.name, Stock.id).join(Stock.book).join(Stock.shop).filter(Book.id_publisher == publisher_id).subquery()
            for result in session.query(subq.c.title, subq.c.name, Sale.price, Sale.date_sale).join(subq, Sale.id_stock == subq.c.id).all():
                print(f'{result[0]}', tabulation(result[0], 39), end='| ')
                print(f'{result[1]}', tabulation(result[1], 8), end='| ')
                print(result[2], result[3], sep=' | ')
        else: break







    session.close()



