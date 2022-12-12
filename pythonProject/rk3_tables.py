from rk3_setup import db

class films(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_name = db.Column(db.String(63), unique=True, nullable=False)
    film_producer = db.Column(db.String(63), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    category = db.Column(db.String(63), unique=False, nullable=True)


    @staticmethod
    def add(film_name, film_producer, year, category):
        db.session.add(films(film_name=film_name, film_producer=film_producer, year=year, category=category))
        db.session.commit()
