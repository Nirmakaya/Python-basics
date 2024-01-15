from sqlalchemy import create_engine, Integer, Column, String, CHAR, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String(50))
    lastname = Column("lastname", String(50))
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    # A constructor of Person
    def __int__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    # Repro Function : Specifies how we want to print the output when a object of Person is called
    # Like when you print the rows/output of a table
    def __repr__(self):
        # f string
        return f"({self.ssn}) {self.firstname} {self.lastname} {self.gender}, {self.age})"


class City(Base):
    __tablename__ = 'cityinfo'

    city = Column("city", String(50), primary_key=True)
    name = Column("name", String(50))

    def __int__(self, city, name):
        self.city = city
        self.name = name

    def __repr__(self):
        # f string
        return f"({self.city}) {self.name}"

# ForeignKey() table
class Thing(Base):
    __tablename__ = 'Thing'

    tid = Column("tid", String(50), primary_key=True)
    description = Column("description", String(50))
    # Use of ForeignKey(), people is the table name of Person
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __int__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        # f string
        return f"({self.tid}) {self.description}, owned by {self.owner}"


engine = create_engine("postgresql://postgres:root@localhost:5432/alchemy", echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Person(ssn='12453', firstname='Mike', lastname='Tyson', gender='M', age=50)
p2 = Person(ssn='73940', firstname='Eternal', lastname='Sorcerer', gender='M', age=22)
p3 = Person(ssn='74829', firstname='Rebrasca', lastname='Tenet', gender='F', age=35)
p4 = Person(ssn='12376', firstname='Kai', lastname='Parker', gender='M', age=28)
p5 = Person(ssn='99238', firstname='Demon', lastname='Salvator', gender='M', age=27)
session.add_all([p1,p2,p3,p4,p5])
session.commit()


c1 = City(city='Delhi', name='Mike')
c2 = City(city='Pero', name='Eternal')
c3 = City(city='Rio', name='Rebrasca')
c4 = City(city='Columbia', name='Kai')
c5 = City(city='New Orelands', name='Demon')
session.add_all([c1,c2,c3,c4,c5])
session.commit()

t1 = Thing(tid='1', description="Car", owner=p1.ssn)
t2 = Thing(tid='2', description="Laptop", owner=p2.ssn)
t3 = Thing(tid='3', description="PS5", owner=p3.ssn)
t4 = Thing(tid='4', description="Book", owner=p4.ssn)
session.add_all([t2, t3, t4])
session.commit()



# See the output : in query(), we give the name of the Class we want to fetch : all()
result = session.query(Person).all()
print(result)

# We can use operators >, <, ==
age = session.query(Person).filter(Person.age > 34).all()
for a in age:
    print(a.firstname, a.age)

# We can use like() function just as in SQL query
adv_query = session.query(Person).filter(Person.firstname.like("%ra%"))
for ad in adv_query:
    print(ad.firstname, ad.lastname)

# in_() : for list of values, put data in a tuple format
adv_query_2 = session.query(Person).filter(Person.firstname.in_(["Rebrasca", "Kai"]))
for ad in adv_query_2:
    print(ad.firstname, ad.lastname)


# Foreign key used query
two_table_query = session.query(Person, Thing).filter(Thing.owner == Person.ssn).filter(Person.firstname=="Kai").all()
print(two_table_query)




# Left Join
joins = (session.query(Person, Thing)
         .join(Thing)
         .all())

# joins will have two variable/object of two tables
for i, j in joins:
    print(i.firstname, j.description)









