from db_connection import *
from db_adding import db_adding
from models import drop_tables, create_tables, Publisher, Book, Shop, Stock, Sale

drop_tables(engine)
create_tables(engine)

db_adding()

def max_len(column):
    """Функция определяет максимальную длину строки в столбце"""
    rows = []
    for row in session.query(column).all():
        rows.append(row[0])
    return len(max(rows, key=len))


#  выборка данных

if __name__ == '__main__':

    while True:
        publisher_id = int(input('Введите идентификатор издателя (от 1 до 4) или 0 для выхода '))
        if publisher_id != 0:
            subq = session.query(Book.title, Shop.name, Stock.id).join(Stock.book).join(Stock.shop).filter(Book.id_publisher == publisher_id).subquery()
            for result in session.query(subq.c.title, subq.c.name, Sale.price, Sale.date_sale).join(subq,Sale.id_stock == subq.c.id).all():
                print(result[0], ' ' * (max_len(Book.title) - len(result[0])), end='| ')
                print(result[1], ' ' * (max_len(Shop.name) - len(result[1])), end='| ')
                print(result[2], result[3], sep=' | ')
        else:
            break

    session.close()


