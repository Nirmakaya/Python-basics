from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ORM : Object Relational Mapping, object-oriented way of dealing with DB.
# Here, Tables are classes and Fields are Table's Attributes.

# DB engine connection
# create_engine(SQL server name:// Username:password@ url : port/ DB name)
# echo = True, will gives very long verbose

engine = create_engine("postgresql://postgres:root@localhost:5432/alchemy", echo=False)

#Server
# Here 'Session' acts as class and in 'session' there is a constructor
Session = sessionmaker(bind=engine)
session = Session()

#Table Creation : Base is a constructor of declarative_base() class that we imported
Base = declarative_base()

class Student(Base):
    # Table Name : Mandatory
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

# Migrate : to show in DB code :-
# This means all extends of Base class,
# in (our case only one)is now creates it DB by connecting to engine
Base.metadata.create_all(bind=engine)
# Only have to run for the first time

# DB table entries : Student class objects for DB entries
student1 = Student(name='Sam', age=12, grade='Fifth')
student2 = Student(name='Lily', age=12, grade='Ninth')
student3 = Student(name='Gade', age=12, grade='Second')





#Add Entries to table
# For single entries : add()
# For multiple : add_all()
# Use list for multiple entries
session.add_all([student1, student3, student2])
# Always Commit
session.commit()


# Get data of a table, Using Student DB Class here. : query()
students = session.query(Student)

for student in students:
    print(student.name, student.age, student.grade)


# Get data of a table : order_by()
students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name)


# Get data by filtering : filter() First()
students = session.query(Student).filter(Student.name=="Lily").first()
print(students.name, students.age)

# Get multiple data to filtering, refer official documentation
students = session.query(Student).filter(Student.name=="Lily",Student.name=="Sam").first()

for student in students:
    print(student.name, student.age)


# Count : count()
student_count = session.query(Student).count()
print(student_count)


#Update and commit()
student = session.query(Student).filter(Student.age=='12').first()
student.age="22"
session.commit()

# Delete : delete() and commit
student = session.query(Student).filter(Student.name=="Lemon").first()
session.delete(student)
session.commit()






