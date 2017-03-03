from sqlalchemy import *
from datetime import datetime

meta = MetaData()

persons = Table('Person', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('cooking_points', Integer, default=0),
        )
cooking_roles = Table('CookingRole', meta,
        Column('name', String, primary_key=True),
        Column('points', Integer),
        )
cookings = Table('Cooking', meta,
        Column('id', Integer, primary_key=True),
        Column('date', DateTime, default=datetime.now()),
        )
cooking_entries = Table('CookingEntry', meta,
        Column('id', Integer, primary_key=True),
        Column('person', None, ForeignKey('Person.id')),
        Column('role', None, ForeignKey('CookingRole.name')),
        Column('cooking', None, ForeignKey('Cooking.id')),
        )

def calculate_cooking_points(person, conn):
    """A function calculating the diff in cooking points from last week 

    :param person: The id of the person
    :type person: person.id
    :param conn: The connection to the database
    :type conn: Connection
    :return: The amount of cooking points of person
    :rtype: int
    """
    s = select([func.sum(cooking_roles.c.points)]).select_from(
            cooking_entries.join(cooking_roles)).where(
                    cooking_entries.c.person == person)
    return conn.execute(s).fetchone()[0]
