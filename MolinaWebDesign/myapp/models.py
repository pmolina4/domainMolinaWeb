from typing import Callable  # para agregar anotaciones a las clases

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Sequence
import pdfkit
import jinja2
import smtplib
from datetime import datetime


def init_db(app) -> dict[str, Callable]:
    db = SQLAlchemy(app)

    # esta clase gestionará la tabla, hay que pasarle la clase base de
    # todos los modelos de Flask alchemy que es db.Model
    class Usuario(db.Model):

        __tablename__ = "Usuario"  # Nombre de la tabla que se crea

        # declarar campos de la tabla "Equipo"
        Usuario_id = db.Column("usuario_id", db.Integer, Sequence(
            'usuario_id_seq'),  primary_key=True)
        Usuario = db.Column(db.String(20))
        Correo = db.Column(db.String(50))
        Contrasena = db.Column(db.String(50))
        Rol = db.Column(db.String(10))

        def __str__(self):
            return f"[{self.usuario}] {self.correo} {self.contrasena} {self.rol}"
        
    class Toldo(db.Model):

        __tablename__ = "Toldo"  # Nombre de la tabla que se crea

        # declarar campos de la tabla "Equipo"
        Toldo_id = db.Column("toldo_id", db.Integer, Sequence(
            'toldo_id_seq'),  primary_key=True)
        Modelo = db.Column(db.String(20))
        Tipo = db.Column(db.String(30))
        Dimensiones = db.Column(db.String(30))
        Imagen = db.Column(db.String(30))
    
    class PresupuestoToldo(db.Model):

        __tablename__ = "PresupuestoToldo"  # Nombre de la tabla que se crea

        # declarar campos de la tabla "Equipo"
        PresupuestoToldo_id = db.Column("presupuestoToldo_id", db.Integer, Sequence(
            'presupuestoToldo_id_seq'),  primary_key=True)
        Ancho = db.Column(db.String(20))
        Salida = db.Column(db.Integer)
        Color = db.Column(db.String(30))
        TipoLona = db.Column(db.String(30))
        Usu = db.Column(db.String(30))

   # ------------- FUNCIONES DE USUARIO -----------
    def create_usuario(usuario: str, correo: str, contrasena: str, rol: str):
        usuario = Usuario(
            Usuario=usuario, Correo=correo, Contrasena=contrasena, Rol=rol
        )
        db.session.add(usuario)
        db.session.commit()

    def find_login(usuario, contrasena):
    # Busca un usuario que coincida con el usuario y la contraseña dados
        usuario_encontrado = Usuario.query.filter_by(
        Usuario=usuario, Contrasena=contrasena).first()
        if usuario_encontrado:
        # Si se encuentra un usuario con este usuario y contraseña, el inicio de sesión es exitoso
            return True
        else:
        # Si no se encuentra un usuario, el inicio de sesión falla
            return False
    def find_admin(usuario, contrasena):
    # Busca un usuario que coincida con el usuario y la contraseña dados
        usuario_encontrado = Usuario.query.filter_by(
        Usuario=usuario, Contrasena=contrasena, Rol="admin").first()
        if usuario_encontrado:
        # Si se encuentra un usuario con este usuario y contraseña, el inicio de sesión es exitoso
            return True
        else:
        # Si no se encuentra un usuario, el inicio de sesión falla
            return False


   # ------------- FUNCIONES DE TOLDOS -----------
    def list_toldos() -> list[Toldo]:
        toldos = Toldo.query.all()
        return [toldo for toldo in toldos]
    
    def read_toldo(Toldo_id: int) -> Toldo:
        return Toldo.query.get(Toldo_id)
    
    def delete_toldo(Toldo_id: int):
        toldo = Toldo.query.get(Toldo_id)
        db.session.delete(toldo)
        db.session.commit()

    def create_toldo(modelo: str, tipo: str, dimensiones: str, imagen: str):
        toldo = Toldo(
            Modelo=modelo, Tipo=tipo, Dimensiones=dimensiones, Imagen=imagen
        )
        db.session.add(toldo)
        db.session.commit()
    
    def update_toldo(
        Toldo_id: int, modelo: str, tipo: str, dimensiones: str
    ):
        toldo = Toldo.query.get(Toldo_id)
        toldo.Modelo = modelo
        toldo.Tipo = tipo
        toldo.Dimensiones = dimensiones
        toldo.Imagen = toldo.Imagen
        db.session.commit()




    # ------------- FUNCIONES DE PRESUPUESTOS TOLDOS -----------
    
    def create_presupuestoT(ancho: str, salida: int, color: str, tipoLona: str, usuario: str):
        presupuestoToldo = PresupuestoToldo(
            Ancho=ancho, Salida= salida, Color=color, TipoLona=tipoLona, Usu=usuario
        )
        db.session.add(presupuestoToldo)
        db.session.commit()
    
    
    # ------------- FUNCIONES DE Solicitudes  -----------
    
    def list_solicitudes() -> list[PresupuestoToldo]:
        solicitudes = PresupuestoToldo.query.all()
        return [solicitud for solicitud in solicitudes]
    
    def list_solicitudes_filter(Usu: str) -> list[PresupuestoToldo]:
        solicitudes = PresupuestoToldo.query.filter_by(Usu=Usu).all()
        return solicitudes
    
    def read_solicitud(PresupuestoToldo_id: int) -> PresupuestoToldo:
        return PresupuestoToldo.query.get(PresupuestoToldo_id)
    
    def delete_solicitud(PresupuestoToldo_id: int):
        solicitud = PresupuestoToldo.query.get(PresupuestoToldo_id)
        db.session.delete(solicitud)
        db.session.commit()

    # create_all es un método de Flask-alchemy que crea la tabla con sus campos
    db.create_all()

    return {
        # estos alias serán usados para llamar a los métodos de la clase, por ejemplo db_access["create"]
        # invoca al método create_contact
        "create_usuario": create_usuario,
        "list_toldos": list_toldos,
        "read_toldo": read_toldo,
        "delete_toldo": delete_toldo,
        "create_toldo": create_toldo,
        "update_toldo" : update_toldo,
        "find_login" : find_login,
        "find_admin" : find_admin,
        "create_presupuestoT" : create_presupuestoT,
        "list_solicitudes" : list_solicitudes,
        "read_solicitud" : read_solicitud,
        "delete_solicitud" : delete_solicitud,
        "list_solicitudes_filter" : list_solicitudes_filter
    }
