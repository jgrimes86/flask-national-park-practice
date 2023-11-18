from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class NationalPark(db.Model, SerializerMixin):
    __tablename__ = 'national_parks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # add relationship
    
    # add serialization rules

    def __repr__(self):
        return f'<NationalPark {self.id} {self.name}>'


class Visitor(db.Model, SerializerMixin):
    __tablename__ = 'visitors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # add relationship
    
    # add serialization rules

    def __repr__(self):
        return f'<Visitor {self.id} {self.name}>'


class Trip(db.Model, SerializerMixin):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    # add relationship
    
    # add serialization rules

    def __repr__(self):
        return f'<Trip {self.id} start={self.start_date} end={self.end_date}>'