from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey

# метаданные - инф. о данных в БД (инф. о таблицах и столбцах, в которых хранятся данные)
meta = MetaData()

# создать таблицу
users = Table('users', meta,
    Column('id_user', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('email', String(100), nullable=False),
    Column('creationDate', String(10), nullable=False),
    Column('company_id', Integer, nullable=False),
    Column('company', String(100), nullable=False)
)

# c (column)
# print(users.c.name)
# print(users.primary_key)
# print(users.c)

# Для созд. движка (объекта Engine) исп. ф-ция create_engine() из пакета sqlalchemy
# Если echo=True, то движок будет сохр. логи SQL в стандартный вывод. По умолчанию False
# engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/mydatabase", echo=True)
engine = create_engine('postgresql+psycopg2://postgres:1111@localhost/mydatabase')
meta.create_all(engine)

# Подключение к базе данных
conn = engine.connect()

# добавить данные в таблицу
# ins_user_query = users.insert().values(name='Arnold', email='arnold@gmail.com', creationDate='2022-01-03', company_id=1, company='Google')
# conn.execute(ins_user_query)
# ins_user_query2 = users.insert().values(name='Jack', email='jack@gmail.com', creationDate='2022-01-07', company_id=2, company='Intetics')
# conn.execute(ins_user_query2)
# ins_user_query3 = users.insert().values(name='Sam', email='sam@gmail.com', creationDate='2022-01-18', company_id=1, company='Google')
# conn.execute(ins_user_query3)

# print(conn)
# print(engine)

# удалить данные из таблицы
delete_query = users.delete().where(users.c.id_user == 3)
conn.execute(delete_query)

# обновить данные в таблице
# update_query = users.update().where(users.c.id_user == 3).values(name='Harry')
# conn.execute(update_query)

# запрос в базу данных и показать инф.
s = users.select().where(users.c.name == 'Arnold')
result = conn.execute(s)

for row in result.fetchall():
    print(row)