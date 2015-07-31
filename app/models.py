from . import db

class Stuff(db.Model):
    __tablename__ = 'stuff'
    id = db.Column(db.Integer, primary_key=True, index=True)
    stuff = db.Column(db.String(255))
    things = db.Column(db.Text())
    
    def __repr__(self):
        return '<Stuff %r: %r>' % (self.stuff, self.things)
