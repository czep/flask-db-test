from flask import render_template, url_for
from . import main
from ..models import Stuff
from .forms import StuffForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = StuffForm()
    if form.validate_on_submit():
        new_stuff = Stuff(stuff=form.stuff.data, things=form.things.data)
        db.session.add(new_stuff)
        form.stuff.data = ''
        form.things.data = ''
    stuff = Stuff.query.all()
    return render_template('index.html', form=form, stuff=stuff)