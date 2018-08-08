from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators,ValidationError

class ManholeForm(Form):
    name=TextField('Manhole Adi',[validators.Required('Lutfen Manhole adini girin.')])
    gl=TextField('Zemin Kotu',[validators.Required('Lutfen zemin kotunu girin.')])
    il = TextField('Akar Kotu', [validators.Required('Lutfen akar kotunu girin.')])
    x = TextField('X Koordinati', [validators.Required('Lutfen x koordinatini girin.')])
    y = TextField('Y Koordinati', [validators.Required('Lutfen y koordinatini girin.')])
    submit=SubmitField('Gönder')