from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from model import *
from cooking_points import *

engine = create_engine('sqlite:///:memory:', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Person(name = 'Albert'),
    Person(name = 'Belle'),
    Person(name = 'Christoph'),
    CookingRole(name = 'Shopping', points = 3),
    CookingRole(name = 'Cooking', points = 6),
    CookingRole(name = 'Dishes', points = 2),
    CookingRole(name = 'Eating', points = 0),
    CookingEvent(date = datetime.now()),
    CookingEntry(person = 1, role = 1, event = 1),
    CookingEntry(person = 2, role = 2, event = 1),
    CookingEntry(person = 3, role = 3, event = 1),
    CookingEntry(person = 3, role = 3, event = 1),
    CookingEntry(person = 1, role = 4, event = 1),
    CookingEntry(person = 2, role = 4, event = 1),
    CookingEntry(person = 3, role = 4, event = 1)
    ])

session.commit()

print('Cooking points:')
result = conn.execute(select([persons.c.name, persons.c.id]))
for row in result:
    print(str(row[persons.c.id])+'|'+row[persons.c.name]+': '
            +str(calculate_cooking_points(row[persons.c.id], conn)))
