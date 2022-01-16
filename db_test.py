from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_decl import Base, User, Company
# from datetime import date

engine = create_engine('postgresql+psycopg2://:1111@localhost/mydatabase', echo=True)
# когда echo вкл., то видны все созд. нами SQL запросы

session = sessionmaker(bind=engine)
s = session()

company_one = Company(name="Intetics")
s.add(company_one)
s.commit()

company_two = Company(name="Google")
s.add(company_two)
s.commit()

user_one = User(name="Viktor", email="viktor@gmail.com", creationDate="2022-01-12", company_id=1)
s.add(user_one)
s.commit()

s.add_all([User(name="Jack", email="jack@gmail.com", creationDate="2022-01-02", company_id=2),
           User(name="Sarah", email="sarah@gmail.com", creationDate="2022-01-07", company_id=1),
           User(name="Lee", email="greg@gmail.com", creationDate="2022-01-11", company_id=2)
           ])
s.commit()

print(s.query(User).first().name)

for name, email in s.query(User.name, User.email).order_by(User.name).limit(3):
    print(name, email)

print('\n\n\n')

user_query = s.query(User).filter_by(User.email == 'jack@gmail.com').one()
if author_query != []:
    user_query.email = 'jack1234@gmail.com'
    s.add(user_query)
    s.commit()

