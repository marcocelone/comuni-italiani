from db import db

class StoreModel(db.Model):
    __tablename__ = 'comuni'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, comune):
        self.name = comune
        #self.id = _id

    def json(self):
        #return {'name': self.name, 'store_id': self.id, 'items': [item.json() for item in self.items.all()]}
        return {'name': self.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
