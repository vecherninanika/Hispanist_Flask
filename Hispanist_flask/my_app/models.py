from flask_login import UserMixin
from ..database import db

metadata = db.metadata


user_to_word = db.Table('user_to_word',
                            db.Column('users', db.Integer, db.ForeignKey('users.id')),
                            db.Column('words', db.Integer, db.ForeignKey('words.id'))
                            )


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    level = db.Column(db.String(50))
    region = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    age = db.Column(db.Integer)
    goal = db.Column(db.String(300))
    info = db.Column(db.String())
    points = db.Column(db.Integer, default=0)
    words = db.relationship('Word', secondary=user_to_word, back_populates='users', cascade="all, delete")


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='user', lazy=True, cascade="all, delete-orphan")



article_to_topic = db.Table('article_to_topic',
                            db.Column('articles', db.Integer, db.ForeignKey('articles.id')),
                            db.Column('topics', db.Integer, db.ForeignKey('topics.id'))
                            )


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.String(), nullable=False)
    image = db.Column(db.String())
    topics = db.relationship('Topic', secondary=article_to_topic, back_populates='articles', cascade="all, delete")


class Topic(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    articles = db.relationship('Article', secondary=article_to_topic, back_populates='topics', cascade="all, delete")


class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    website = db.Column(db.String(200))


class University(db.Model):
    __tablename__ = 'universities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    website = db.Column(db.String(200))


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), nullable=False)
    options = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String(), nullable=False)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)
    image = db.Column(db.String())


class Word(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(), nullable=False)
    users = db.relationship('User', secondary=user_to_word, back_populates='words', cascade="all, delete")    
    translation = db.Column(db.String())


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String())
