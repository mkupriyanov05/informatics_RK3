from rk3_setup import db, app
from flask import render_template
from rk3_tables import *

if __name__ == '__main__':
    app.app_context().push()
    db.create_all() 

    films.add("Die Hard", "Bruce Willis", "1988", "Thriller")
    films.add("Island of Cursed", "Martin Scorcese", "2009", "Detective")

    @app.route('/')
    def unpacking():
        list_1 = []

        res = db.engine.execute('SELECT * FROM films;').fetchall()
        for row in res:
            for item in row:
                list_1.append(item)


        return render_template('rk3.html', id_1=list_1[0], id_2=list_1[5], film_name_1=list_1[1],
        film_name_2=list_1[6], film_producer_1=list_1[2], film_producer_2=list_1[7],
        year_1=list_1[3], year_2=list_1[8], category_1=list_1[4], category_2=list_1[9])


    

    print(type(db.engine.execute('SELECT year FROM films WHERE id = 1;')))

    res = db.engine.execute('SELECT * FROM films;')
    print(*res, sep="\n")

    app.run()
