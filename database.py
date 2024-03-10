from sqlalchemy import create_engine, Column, Integer, String , ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , relationship

# پیکربندی اتصال به پایگاه داده PostgreSQL
# db_user = 'postgres'
# db_password = 'postgres'
# db_host = 'localhost'
# db_port = '5432'
# db_name = 'postgres'
#
# # ایجاد URL اتصال به PostgreSQL
# db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
#
# # ایجاد موتور SQLAlchemy برای اتصال به PostgreSQL
# engine = create_engine(db_url)

# ایجاد connection به دیتابیس
engine = create_engine('sqlite:///database.db', echo=True)

# # تعریف Base برای ORM
Base = declarative_base()

# تعریف مدل داده
class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     age = Column(Integer)



class Category(Base):
      __tablename__ = 'categories'
      id = Column(Integer, primary_key=True)
      name = Column(String)
      books = relationship("Book", backref="category")





class Book(Base):
      __tablename__ = 'books'
      id = Column(Integer, primary_key=True)
      name = Column(String)
      description = Column(String)
      category_id = Column(Integer, ForeignKey('categories.id'))





Base.metadata.create_all(engine)

# ایجاد session
Session = sessionmaker(bind=engine)
session = Session()

# اینسرت کردن یک رکورد جدید
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()


# خواندن اطلاعات
user = session.query(User).filter_by(name='Alice').first()

# آپدیت اطلاعات
user.age = 31
session.commit()                               #ABOUT USER

# حذف رکورد
session.delete(user)
session.commit()







new_category = Category(name='category1')
session.add(new_category)
session.commit()                                           #ABOUT CATEGORY

# خواندن اطلاعات
category = session.query(Category).filter_by(name='category1').first()

# آپدیت اطلاعات
user.name = 'category2'
session.commit()

# حذف رکورد
session.delete(category)
session.commit()








new_book = Book(name='book1'  ,description = 'this is a book1' )
session.add(new_book)
session.commit()


book = session.query(Book).filter_by(name='book1').first()


# آپدیت اطلاعات
book.description = 'This is book2'
session.commit()
                                                            #ABOUT Book
# حذف رکورد
session.delete(book)
session.commit()








