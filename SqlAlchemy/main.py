from sqlalchemy import create_engine, ForeignKey, Column, Table, String, Integer, CHAR, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    pid = Column("pid", Integer, primary_key=True, autoincrement=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.pid}, {self.first_name} {self.last_name}, {self.gender}, {self.age})"

class Thing(Base):
    __tablename__ = 'things'
    tid = Column("tid", Integer, primary_key=True, autoincrement=True)
    description = Column("description", String)
    owner = Column("owner", Integer, ForeignKey('people.pid'))
    def __init__(self, description, owner):
        self.description = description
        self.owner = owner
    def __repr__(self):
        return f"({self.tid}, {self.description} owned by {self.owner})"


engine = create_engine('sqlite:///people.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a new person
person = Person("John", "Doe", "M", 30)
session.add(person)
session.commit()

p1 = Person("Jane", "Doe", "F", 25)
p2 = Person("Alice", "Smith", "F", 35)
p3 = Person("Bob", "Smith", "M", 40)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

results = session.query(Person).all()
for person in results:
    print(person)

result = session.query(Person).filter(Person.gender == "M").all()
for person in result:
    print(person)

t1 = Thing("car",p1.pid)
t2 = Thing("home",p2.pid)
t3 = Thing("laptop",p3.pid)
t4 = Thing("computer",p1.pid)
t5 = Thing("phone",p2.pid)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()

results = session.query(Thing, Person).filter(Thing.owner == Person.pid).all()
for r in results:
    print(r)