from db_connection import *
from db_adding import db_adding
from models import drop_tables, create_tables, Publisher, Book, Shop, Stock, Sale


drop_tables(engine)
create_tables(engine)
db_adding()

def data_selecting(publisher_id):
    """Функция производит выборку данных"""
    for result in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Sale).join(Shop).filter(Publisher.id == publisher_id).all():
        print(result[0], ' ' * (max_len(Book.title) - len(result[0])), end='| ')
        print(result[1], ' ' * (max_len(Shop.name) - len(result[1])), end='| ')
        print(result[2], result[3], sep=' | ')

def get_publisher_id(publisher_name):
    """Функция определяет идентификатор издателя по его имени"""
    return session.query(Publisher.id).filter(Publisher.name == publisher_name)[0][0]

def publishers_list():
    """Фукция выдает список издателей"""
    publishers = []
    for publisher in session.query(Publisher.name).all():
        publishers.append(publisher[0])
    return publishers

def max_len(column):
    """Функция определяет максимальную длину строки в столбце"""
    rows = []
    for row in session.query(column).all():
        rows.append(row[0])
    return len(max(rows, key=len))

if __name__ == '__main__':

    publisher = (input('Введите идентификатор или имя издателя '))
    if publisher.isdigit():
        data_selecting(publisher)
    else:
        if publisher in publishers_list():
            publisher_id = str(get_publisher_id(publisher))
            data_selecting(publisher_id)




session.close()


