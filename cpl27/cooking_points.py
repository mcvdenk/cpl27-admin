from sqlalchemy import *
from datetime import datetime
from model import *

def calculate_cooking_points(person, conn):
    """A function calculating the diff in cooking points from last week 

    :param person: The id of the person
    :type person: person.id
    :param conn: The connection to the database
    :type conn: Connection
    :return: The amount of cooking points of person
    :rtype: int
    """
