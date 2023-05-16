from flask import Flask

# método que crea la aplicación (es llamadao en server.py)
def create_app():
    app = Flask(__name__) # para crear una aplicación tipo Flask
    app.secret_key = "abcd1234"
    # declarar qué archivo SQLite se conectará a la aplicación creada con Flask
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///persianas_molina.sqlite3"

    
    with app.app_context(): 
        # importar los objetos que manejarán las vistas y la BD
        from .models import init_db
        from .views import init_views

        # crear las instancias para manejar las vistas y la BD
        db_access = init_db(app) # init_db está en models.py
        init_views(app, db_access) # init_views está en views.py

    return app
    
    # init_db es la clase que crea la tabla e implementa los métodos que operan sobre ella:
    #  create_contact, read_contact, update_contact, delete_contact, list_contacts
    
    # init_views es la clase que renderiza cada una de los páginas html
    # e implementa las acciones de cada una para las peticiones "GET" y "POST" con el servidor
