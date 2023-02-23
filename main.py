import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model import create_tables, Publisher, Book, Shop, Stock, Sale


DSN = 'postgresql://postgres:postgresdb@localhost:5432/db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
session.add(publisher1)
session.commit()
print(publisher1)

print()

book1 = Book(title='Капитанская дочка', publisher=publisher1)
book2 = Book(title='Руслан и Людмила', publisher=publisher1)
book3 = Book(title='Евгений Онегин', publisher=publisher1)
session.add_all([book1, book2, book3])
session.commit()
for book in session.query(Book).all():
    print(book)

print()   

shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Книжный дом')
session.add_all([shop1, shop2, shop3])
session.commit()
for shop in session.query(Shop).all():
    print(shop)

print()

stock1 = Stock(book=book1, shop=shop1, count='1')
stock2 = Stock(book=book2, shop=shop1, count='2')
stock3 = Stock(book=book1, shop=shop2, count='1')
stock4 = Stock(book=book3, shop=shop3, count='3')
stock5 = Stock(book=book1, shop=shop1, count='1')
session.add_all([stock1, stock2, stock3, stock4, stock5])
session.commit()
for stock in session.query(Stock).all():
    print(stock)

print()

sale1 = Sale(price='600', date_sale='09-11-2022', stock=stock1, count='1')
sale2 = Sale(price='500', date_sale='08-11-2022', stock=stock3, count='1')
sale3 = Sale(price='580', date_sale='05-11-2022', stock=stock5, count='1')
sale4 = Sale(price='490', date_sale='02-11-2022', stock=stock2, count='1')
sale5 = Sale(price='600', date_sale='26-11-2022', stock=stock4, count='1')
session.add_all([sale1, sale2, sale3, sale4, sale5])
session.commit()
for sale in session.query(Sale).all():
    print(sale)

print()

print('Информация о покупке книг данного издателя:')
for q in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Sale).join(Shop).filter(Publisher.name == 'Пушкин'):
    print(q)


session.close()

