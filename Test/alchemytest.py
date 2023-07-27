from sqlalchemy import create_engine, Column, Integer, select, func, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, aliased

engine = create_engine('postgresql://chandan:User#123@localhost/testdb')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship('Employee', back_populates='department')


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship('Department', back_populates='employees')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
try:
    # person1 = Person(name='Alice', age=25)
    # person2 = Person(name='Kiran', age=27)
    # session.add_all([person1, person2])
    dept1 = Department(name='IT')
    dept2 = Department(name='Marketing')
    session.add_all([dept1, dept2])

    emp1 = Employee(name='Alice', age=25, department=dept1)
    emp2 = Employee(name='Bob', age=30, department=dept2)
    session.add_all([emp1, emp2])
    session.commit()
except:
    session.rollback()
    raise ConnectionError


people = session.query(Person).all()
for person in people:
    print(person.id, person.name, person.age)

result1 = session.query(Employee, Department)\
    .join(Department, Employee.id == Department.id).all()

result2 = session.query(Employee, Department)\
    .outerjoin(Department, Employee.id == Department.id).all()

subq = session.query(func.avg(Employee.age)).subquery()
result4 = session.query(Employee.name).filter(Employee.age>subq).all()

# result3 = session.query(Employee, Department).
e1 = aliased(Employee)
e2 = aliased(Employee)
query = select([e1.name, e2.name]).where(e1.age == e2.age)



