from db_setup import db

class students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    record_book_number = db.Column(db.String(6), unique=True, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    patronymic = db.Column(db.String(80), unique=False, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=False)
    faculty = db.Column(db.String(5), unique=False, nullable=False)
    education_year = db.Column(db.Integer, unique=False, nullable=False)


    @staticmethod
    def add(record_book_number, surname, first_name, patronymic, age, faculty, education_year):
        db.session.add(students(record_book_number=record_book_number, surname=surname,
        first_name=first_name, patronymic=patronymic, age=age, faculty=faculty,
        education_year=education_year))
        db.session.commit()
