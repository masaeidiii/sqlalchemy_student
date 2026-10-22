from sqlalchemy import create_engine, Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    name = Column(String)
    score = Column(INTEGER)

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
sessionLocal = Session()


#CREAT STUDENT
new_student1 = Student(name='shirin', score=100)
new_student2 = Student(name='sara', score=65)
new_student3 = Student(name='pejman', score=85)
new_student4 = Student(name='sohrab', score=42)
new_student5 = Student(name='ali', score=88)
new_student6 = Student(name='fateme', score=95)

sessionLocal.add(new_student1)
sessionLocal.add(new_student2)
sessionLocal.add(new_student3)
sessionLocal.add(new_student4)
sessionLocal.add(new_student5)
sessionLocal.add(new_student6)
sessionLocal.commit()

#getint info of std
students = sessionLocal.query(Student).all()
for student in students:
    print(f"ID: {student.id}   , Name: {student.name}  , Score: {student.score}")


#changing std name
student_to_update = sessionLocal.query(Student).filter_by(id=1).first()
student_to_update.name = 'fateme'
student_to_update.score = 90
sessionLocal.commit()


#deleting std ID
student_to_delete = sessionLocal.query(Student).filter_by(id=1).first()
sessionLocal.delete(student_to_delete)
sessionLocal.commit()

