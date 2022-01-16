from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# from datetime import date

# подключиться к базе данных и внести данные
# engine = create_engine("mysql+mysqlconnector://root:root@localhost/pyloungedb", echo=True)
# engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
engine = create_engine('postgresql+psycopg2://garri:1111@localhost/mydatabase')
# engine = create_engine('postgresql+psycopg2://garri:1111@localhost/mydatabase', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id_user = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100))
    creationDate = Column(String(10))
    company_id = Column(Integer, ForeignKey("Company.id_company"))
    company = relationship("Company")

class Company(Base):
    __tablename__ = 'Company'

    id_company = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user = relationship("User")  # company has many users

Base.metadata.create_all(engine)


"""
# метаданные - инф. о данных в БД (инф. о таблицах и столбцах, в которых хранятся данные)
meta = MetaData(engine)

# create table
users = Table('Users', meta, autoload=True)

conn = engine.connect()

# c (column)
s = users.select().where(users.c.name == 'Jack')
result = conn.execute(s)

for row in result.fetchall():
    print(row)

# delete record
delete_query = users.delete().where(users.c.id_users == 1)
conn.execute(delete_query)

# update record
update_query = users.update().where(users.c.id_users == 1).values(title='AnotherTitle')
conn.execute(update_query)
"""
