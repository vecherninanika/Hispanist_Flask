from models import db, Book
from app import app

books = []

title_1 = 'España ayer y hoy'
link_1 = 'https://drive.google.com/file/d/1dP1PHQ0zsNwPE1w69tq9NA3fyMCaYLqz/view?usp=sharing'
image_1 = 'https://img4.labirint.ru/rc/6fa01ea4e5ecc92e7956e8e64cca724a/363x561q80/books95/948098/cover.jpg?1684851928'

book_1 = Book(title=title_1, link=link_1, image=image_1)
books.append(book_1)


title_2 = 'Viva la cultura en España'
link_2 = 'https://drive.google.com/file/d/1rVA-hrBzXfO416UmeRal7fPULjtiAFfx/view?usp=sharing'
image_2 = 'https://www.moscowbooks.ru/image/book/324/w259/i324580.jpg?cu=20180101000000'

book_2 = Book(title=title_2, link=link_2, image=image_2)
books.append(book_2)


title_3 = 'Geografía de Hispanoamérica'
link_3 = 'https://drive.google.com/file/d/1Dacp3qxo3_flNLTiWPFkyzHvQV1MGwK4/view?usp=sharing'
image_3 = 'https://hispanoamericaunida.files.wordpress.com/2019/02/01-e-hispanoamc3a9rica.jpg'

book_3 = Book(title=title_3, link=link_3, image=image_3)
books.append(book_3)


title_4 = 'Historia de Hispanoamérica'
link_4 = 'https://drive.google.com/file/d/14VK0RA-kOsUFVzhRUNv6wNGd37PCBi3i/view?usp=sharing'
image_4 = 'https://hispanoamericaunida.files.wordpress.com/2019/02/01-e-hispanoamc3a9rica.jpg'

book_4 = Book(title=title_4, link=link_4, image=image_4)
books.append(book_4)


with app.app_context():
    for book in books:
        db.session.add(book)
        db.session.commit()


