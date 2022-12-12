from db_setup import db
from tables import *
from app_setup import app

if __name__ == '__main__':
    app.app_context().push()
    #Создание(Модификация) соответствующей базы данных и таблицы из   заготовленных шаблонов'''
    db.create_all() 

    students.add("22У2222", "Королева", "Елизавета", "Англии", 99, "Э", 6)
    students.add("33У3333", "Король", "Карл", "Англии", 88, "СМ", 2)
    students.add("44У4444", "Меркьюри", "Фредди", "Квинович", 43, "ИУ", 5)
    students.add("55У5555", "Куртка", "Бейн", "Нирванович", 27, "СМ", 5)

    res = db.engine.execute('SELECT * FROM students;')
    print(*res, sep="\n")

    app.run()
