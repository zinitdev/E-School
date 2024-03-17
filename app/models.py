import enum
from app import db
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Enum, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime


class GenderEnum(enum.Enum):
    FEMALE = 'Female'
    MALE = 'Male'


class CommonModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class InforModel(CommonModel):
    __abstract__ = True
    
    first_name = Column(String(80))
    last_name = Column(String(80))
    address = Column(Text)
    gender = Column(Enum(GenderEnum), default=GenderEnum.MALE)
    avatar = Column(Text, default=None)
    phone = Column(String(10), nullable=False)
    email = Column(String(125), unique=True, nullable=False)
    

class Grade(CommonModel):
    name = Column(String(80), unique=True)
    classes = relationship('Class', backref='grade', lazy=True)
    
    def __str__(self):
        return f"Grade {self.name}"


class_student = db.Table('class_student',
                    Column('class_id', Integer, ForeignKey('class.id'), nullable=False),
                    Column('student_id', Integer, ForeignKey('student.id'), nullable=False)
                    )


class Class(CommonModel):
    name = Column(String(80), unique=True)
    grade_id = Column(Integer, ForeignKey(Grade.id), nullable=False)
    students = relationship('Student', secondary=class_student, backref='class', lazy=True)
    
    def __str__(self):
        return self.name


class Student(InforModel):
    dob = Column(DateTime, default=datetime.utcnow()) 
    scores = relationship('Score', backref='student', lazy=True)
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


subject_semester = db.Table('subject_semester',
    Column('subject_id', Integer, ForeignKey('subject.id')),
    Column('semester_id', Integer, ForeignKey('semester.id'))
)


class Subject(CommonModel):
    title = Column(String(80), unique=True)
    description = Column(Text)
    scores = relationship('Score', backref='subject', lazy=True)
    semesters = relationship('Semester', secondary=subject_semester, backref='subject', lazy=True)
    
    def __str__(self):
        return self.title
    

class Score(CommonModel):
    result = Column(Float, default=0.00)
    subject_id = Column(Integer, ForeignKey(Subject.id), nullable=False)
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    test_id = Column(Integer, ForeignKey('test.id'), nullable=False)

    def __str__(self):
        return f"{self.result}"


class Test(CommonModel):
    name = Column(String(80), unique=True)
    scores = relationship('Score', backref='test', lazy=True)

    def __str__(self):
        return self.name


class AcademicYear(CommonModel):
    start_year = Column(DateTime, default=datetime.utcnow())
    end_year = Column(DateTime, default=datetime.utcnow())
    semesters = relationship('Semester', backref='academic_year', lazy=True)

    def __str__(self):
        return f"{self.start_year.year} - {self.end_year.year}"


class Semester(CommonModel):
    name = Column(String(100))
    academic_year_id = Column(Integer, ForeignKey('academic_year.id'), nullable=False)

    def __str__(self):
        return self.name