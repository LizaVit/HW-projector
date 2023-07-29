#Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
#Find all students` name that visited 'English' classes.
#(Optional): Rewrite queries from the previous lesson using SQLAlchemy.

from sqlalchemy import create_engine

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'


engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='postgres',
        user='postgres',
        password='postgres',
        port=5432,
    )
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f'This is {self.id} student {self.name}. Age: {self.age}'

    def __repr__(self):
        return self.__str__()
    
class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String)

    def __str__(self):
        return f'This is {self.id} subject {self.subject_name}'

    def __repr__(self):
        return self.__str__()
    
class Student_subject(Base):
    __tablename__ = 'student_subject'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('student.id'))
    subject_id = Column(ForeignKey('subject.id'))

    def __str__(self):
        return f'This is {self.id} student {self.student_id}. subject {self.subject_id}'

    def __repr__(self):
        return self.__str__()
    

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

session.query(Student_subject).delete();
session.query(Student).delete();
session.query(Subject).delete();

subj_math = Subject(subject_name = 'Math')
subj_eng = Subject(subject_name = 'English')
subj_mus = Subject(subject_name = 'Music')
st_maks = Student(name='Maksym', age=25)
st_gal = Student(name='Galya', age=21)
st_vas = Student(name='Vasya', age=23)

session.add_all([subj_math, subj_eng, subj_mus, st_maks, st_gal, st_vas])
session.commit()

session.add_all([
                Student_subject(student_id = st_maks.id, subject_id = subj_math.id),
                Student_subject(student_id = st_maks.id, subject_id = subj_eng.id),
                Student_subject(student_id = st_gal.id, subject_id = subj_math.id)
                ])

session.commit()

students = session.query(Student).all()
print(students)



Math_result = session.query(Student.name, Subject.subject_name, Student_subject.id).join(Student).join(Subject).filter(Subject.subject_name == 'Math').all()

for name, subj, id in Math_result:
    print(f"Математика : {name}")

session.close()

