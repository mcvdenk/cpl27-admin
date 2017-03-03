# TODO add relationship()s http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CookingEvent(Base):
    __tablename__ = 'CookingEvent'
    id   = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)

class CookingEntry(Base):
    __tablename__ = 'CookingEntry'
    id     = Column(Integer, primary_key=True)
    event  = Column(Integer, ForeignKey('CookingEvent.id'), nullable=False)
    person = Column(Integer, ForeignKey('Person.id'), nullable=False)
    role   = Column(Integer, ForeignKey('CookingRole.id'), nullable=False)

class CookingRole(Base):
    __tablename__ = 'CookingRole'
    id     = Column(Integer, primary_key=True)
    name   = Column(String(20), nullable=False)
    points = Column(Float, nullable=False)

class DutyEntry(Base):
    __tablename__ = 'DutyEntry'
    person = Column(Integer, ForeignKey('Person.id'), nullable=False)
    type   = Column(Integer, ForeignKey('DutyType.id'), nullable=False)
    date   = Column(Date, nullable=False)

class DutyQueue(Base):
    __tablename__ = 'DutyQueue'
    id     = Column(Integer, primary_key=True)
    person = Column(Integer, ForeignKey('Person.id'), nullable=False)

class DutyType(Base):
    __tablename__ = 'DutyType'
    id          = Column(Integer, primary_key=True)
    name        = Column(String(20), nullable=False)
    checklist   = Column(Text, nullable=False)
    startWindow = Column(Date, nullable=False)
    endWindow   = Column(Date, nullable=False)

class Person(Base):
    __tablename__ = 'Person'
    id            = Column(Integer, primary_key=True)
    name          = Column(String(50), nullable=False)
    email         = Column(String(100))
    bankAccount   = Column(String(50))
    joinDate      = Column(Date, nullable=False)
    leaveDate     = Column(Date)
    room          = Column(Integer, ForeignKey('Room.number'))
    cookingPoints = Column(Float)

class Room(Base):
    __tablename__ = 'Room'
    number     = Column(Integer, primary_key=True)
    inhabitant = Column(Integer, ForeignKey('Person.id'))

class Transaction(Base):
    __tablename__ = 'Transaction'
    id     = Column(Integer, primary_key=True)
    person = Column(Integer, ForeignKey('Person.id'), nullable=False)
    group  = Column(Integer, ForeignKey('TransactionGroup.id'), nullable=False)
    amount = Column(Float, nullable=False)

class TransactionGroup(Base):
    __tablename__ = 'TransactionGroup'
    id           = Column(Integer, primary_key=True)
    category     = Column(String(20))
    note         = Column(Text)
    date         = Column(Date, nullable=False)
    writeoffDate = Column(Date, nullable=False)
