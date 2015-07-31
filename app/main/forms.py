from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class StuffForm(Form):
    stuff = StringField('Stuff', validators=[Required()])
    things = TextAreaField('Things', validators=[Required()])
    submit = SubmitField('Submit Stuff and Things')
