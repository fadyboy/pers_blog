# database models for application

from app import db

# define class models for the Category and Interests

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, db.Sequence('category_id'), primary_key=True)
    name = db.Column(db.String(50))

    # add a relationship to the Interests table
    category_interests = db.relationship('Interests', backref = 'category', cascade = 'all, delete, delete_orphan')

    def __reduce__(self):
        return '<Category {}'.format(self.name)


class Interests(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, db.Sequence('interest_id'), primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Interests {}'.format(self.title)

