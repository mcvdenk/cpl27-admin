from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, DateField
from wtforms.validators import DataRequired

class DeclarationForm(FlaskForm):
    person = SelectField('Paid by', validators=[DataRequired()])
    cost = DecimalField('Price', validators=[DataRequired()])
    dateStart = DateField('Bought on')
    dateEnd = DateField('Expires on')

class CookingForm(FlaskForm):
    pass
