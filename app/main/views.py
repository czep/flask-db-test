from flask import render_template
from . import main
from ..models import Stuff
from .forms import StuffForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = StuffForm()
    if form.validate_on_submit():
        stuff = Stuff(stuff=form.stuff.data, things=form.things.data)
        db.session.add(stuff)
        form.stuff.data = ''
        form.things.data = ''
    old_stuff = Stuff.query.all()
    return render_template('index.html', form=form, old_stuff=old_stuff)
