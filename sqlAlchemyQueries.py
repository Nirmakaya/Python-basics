from sqlalchemy import create_engine, Integer, Column, String, CHAR, ForeignKey,\
    and_, desc, asc
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
    # Use of ForeignKey()
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


## Filter_by() : it can be also used to filter, but with this we have less control on filter,
# so we use filter() in general

# We can write table.attributes in query directly instead of writing it after in for loop

# We use .first() with filter because .all() with a filter applied doesn;t make sense.
# With filter_by() we don't need to write the class name and comparison operator '=='
# We can directly write the value
# With filter we generally use Unique values only to get the output

result = session.query(Thing.description).filter_by(description='PS5').first()

for value in result:
    print(value)



filter = session.query(Thing).filter(Thing.description == 'Car', and_(Thing.tid == '1')).first()

print(filter)
## We don't use loop for a single value print. Else it will through error
# for row in filter:
#     print(row.tid, row.description, row.owner)


## Joins with order_by() , import desc and asc to use
join = (session.query(Person, Thing).\
        select_from(Person).join(Thing).\
        order_by(asc(Person.firstname),
                 asc(Person.lastname)).\
        all())


for Person, Thing in join:
    print(Person.ssn, Person.firstname, Person.lastname, Person.gender, Person.age,
          Thing.tid , Thing.description, Thing.owner)


# ## Joins of 3 tables : with 3 we use .select_from() to identify the left most table.
# join = (session.query(Person, Thing, City).\
#         select_from(Person).join(Thing).join(City)
#         all())
#
#
# for Person, Thing, City in join:
#     print(Person.ssn, Person.firstname, Person.lastname, Person.gender, Person.age,
#           Thing.tid , Thing.description, Thing.owner,
#           City.city, City.name)
