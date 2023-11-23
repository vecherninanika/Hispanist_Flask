from Hispanist_flask.my_app.models import *
from manage import app
from werkzeug.security import generate_password_hash

# admin = User(name='admin', username='adminuser', password=generate_password_hash('123456'), role=1)
# with app.app_context():
#     db.session.add(admin)
#     db.session.commit()


# user = User(name='nika', username='nika', password=generate_password_hash('wangnyang'), role=2)
with app.app_context():
    user = User.query.filter(User.id==2)
    user.points = 0
    db.session.commit()


title_1 = 'El Premio Goya'
text_1 = """"""


image_1 = 'https://upload.wikimedia.org/wikipedia/en/a/a5/1st_Goya_Awards_logo.jpg'

article = Article(title=title_1, text=text_1, image=image_1)
# with app.app_context():
#     article = Article.query.filter(Article.title==title_1).first()
#     # db.session.add(article)
#     article.image = image_1
#     db.session.commit()


question_1 = 'Сеута и Мели'
options_1 = '1982,1990,1980,1986'
answer_1 = '1982'

# question = Question(question=question_1, options=options_1, answer=answer_1)
# with app.app_context():
#     db.session.add(question)
#     db.session.commit()



# Эссе по разным темам
# Об изучении испанского
# История и география
# ВсОШ
# Литература
# Культура

# title_1 = 'El Premio Goya'
# name_1 = 'Эссе по разным темам'
# with app.app_context():
#     article = Article.query.filter(Article.title==title_1).first()
#     # topic = Topic(name=name_1)
#     topic = Topic.query.filter(Topic.name==name_1).first()
#     topic.articles.append(article)  
#     db.session.add(topic)
#     # topic.articles = []
#     # db.session.delete(topic)
#     db.session.commit()

