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
    trips = db.relationship('Trip', back_populates='national_park')
    visitors = association_proxy('trips', 'visitor')
    
    # add serialization rules
    serialize_rules=('-trips.national_park',)

    def __repr__(self):
        return f'<NationalPark {self.id} {self.name}>'


class Visitor(db.Model, SerializerMixin):
    __tablename__ = 'visitors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # add relationship
    trips = db.relationship('Trip', back_populates='visitor')
    national_parks = association_proxy('trips', 'national_park')

    # add serialization rules
    serialize_rules=('-trips.visitor',)

    def __repr__(self):
        return f'<Visitor {self.id} {self.name}>'


class Trip(db.Model, SerializerMixin):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    national_park_id = db.Column(db.Integer, db.ForeignKey('national_parks.id'))
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'))

    # add relationship
    visitor = db.relationship('Visitor', back_populates='trips')
    national_park = db.relationship('NationalPark', back_populates='trips')
    
    # add serialization rules
    serialize_rules=('-visitor.trips', '-national_park.trips')

    # validations
    @validates('visitor_id')
    def validate_visitor(self, key, visitor_id):
        v_ids = [v.id for v in Visitor.query.all()]
        if visitor_id not in v_ids:
            raise ValueError("Visitor must be an existing Visitor instance")
        else:
            return visitor_id

    @validates('national_park_id')
    def validate_park(self, key, national_park_id):
        np_ids = [np.id for np in NationalPark.query.all()]
        if national_park_id not in np_ids:
            raise ValueError("National Park must be an existing National Park instance")
        else:
            return national_park_id

    def __repr__(self):
        return f'<Trip {self.id} start={self.start_date} end={self.end_date}>'