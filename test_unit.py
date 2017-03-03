from sqlalchemy import *
from datetime import datetime
from cooking_points import *

engine = create_engine('sqlite:///:memory:', echo=True)
meta = MetaData()
conn = engine.connect()
persons = Table('Person', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        )
cooking_roles = Table('CookingRole', meta,
        Column('name', String, primary_key=True),
        Column('points', Integer),
        )
cookings = Table('Cooking', meta,
        Column('id', Integer, primary_key=True),
        Column('date', DateTime, default=datetime.now()),
        )
cooking_entries = Table('cooking_entry', meta,
        Column('id', Integer, primary_key=True),
        Column('person', None, ForeignKey('Person.id')),
        Column('role', None, ForeignKey('CookingRole.name')),
        Column('cooking', None, ForeignKey('Cooking.id')),
        )
meta.create_all(engine)
conn.execute(persons.insert(), [
    {'name': 'Albert'},
    {'name': 'Belle'},
    {'name': 'Christoph'},
    ])
conn.execute(cooking_roles.insert(), [
    {'name': 'Shopping', 'points': 3},
    {'name': 'Cooking', 'points': 6},
    {'name': 'Dishes', 'points': 2},
    {'name': 'Eating', 'points': 0},
    ])
conn.execute(cookings.insert())
conn.execute(cooking_entries.insert(), [
    {'person': 1, 'role': 'Shopping', 'cooking': 1},
    {'person': 2, 'role': 'Cooking', 'cooking': 1},
    {'person': 3, 'role': 'Dishes', 'cooking': 1},
    {'person': 3, 'role': 'Dishes', 'cooking': 1},
    {'person': 1, 'role': 'Eating', 'cooking': 1},
    {'person': 2, 'role': 'Eating', 'cooking': 1},
    {'person': 3, 'role': 'Eating', 'cooking': 1},
    ])
print('Cooking points:')
result = conn.execute(select([persons.c.name, persons.c.id]))
for row in result:
    print(str(row[persons.c.id])+'|'+row[persons.c.name]+': '
            +str(calculate_cooking_points(row[persons.c.id])))
