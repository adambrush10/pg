form flask_wtf import FlaskForm
from wtforms import StringField
form wtforms.validators import DataRequired, Length, SubmitField

class InputForm(FlaskForm):
    symbol = StringField('Symbol',
                         validators=[DataRequired(), Length(min=2, max=4)])
    startdate = StringField('StartDate')
    enddate = StringField('EndDate')
    submit = SubmitField('Get History')
