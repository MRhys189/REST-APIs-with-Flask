from db import db


class StoreModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic') #a many to one relationship(many items in 1 store )

    def __init__(self, name):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'items': [items.json for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        # SELECT * FROM items WHERE name=name
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
