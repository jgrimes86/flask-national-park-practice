#!/usr/bin/env python3

from app import app
from models import db, NationalPark, Visitor, Trip
from datetime import datetime

with app.app_context():

    # This will delete any existing rows
    # so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Visitor.query.delete()
    NationalPark.query.delete()
    Trip.query.delete()

    print("Creating Visitors...")
    karen = Visitor(name="Karen")
    sanjay = Visitor(name="Sanjay")
    kiki = Visitor(name="Kiki")
    visitors = [karen, sanjay, kiki]

    print("Creating NationalParks...")

    np1 = NationalPark(name="Yosemite")
    np2 = NationalPark(name="Pinnacles")
    np3 = NationalPark(name="Yellowstone")
    national_parks = [np1, np2, np3]

    print("Creating Trips...")

    t1 = Trip(visitor=karen, national_park=np1, start_date=datetime.strptime("2023-11-18 03:02:03", '%Y-%m-%d %H:%M:%S'), end_date=datetime.strptime("2023-11-20 03:02:03", '%Y-%m-%d %H:%M:%S'))
    t2 = Trip(visitor=sanjay, national_park=np2, start_date=datetime.strptime("2023-11-18 03:02:03", '%Y-%m-%d %H:%M:%S'), end_date=datetime.strptime("2023-11-19 03:02:03", '%Y-%m-%d %H:%M:%S'))
    t3 = Trip(visitor=kiki, national_park=np3, start_date=datetime.strptime("2023-11-20 03:02:03", '%Y-%m-%d %H:%M:%S'), end_date=datetime.strptime("2023-11-21 03:02:03", '%Y-%m-%d %H:%M:%S'))
    t4 = Trip(visitor=kiki, national_park=np1, start_date=datetime.strptime("2023-11-21 03:02:03", '%Y-%m-%d %H:%M:%S'), end_date=datetime.strptime("2023-11-28 03:02:03", '%Y-%m-%d %H:%M:%S'))
    t5 = Trip(visitor=sanjay, national_park=np2, start_date=datetime.strptime("2023-12-18 03:02:03", '%Y-%m-%d %H:%M:%S'), end_date=datetime.strptime("2023-12-20 03:02:03", '%Y-%m-%d %H:%M:%S'))
    t6 = Trip(visitor=kiki, national_park=np3, start_date=datetime.strptime("2023-12-22 03:02:03", '%Y-%m-%d %H:%M:%S'), end_date=datetime.strptime("2023-12-30 03:02:03", '%Y-%m-%d %H:%M:%S'))
    trips = [t1, t2, t3, t4, t5, t6]

    db.session.add_all(national_parks)
    db.session.add_all(visitors)
    db.session.add_all(trips)
    db.session.commit()

    print("Seeding done!")