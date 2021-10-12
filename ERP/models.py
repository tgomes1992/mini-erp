
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from ERP import app

#database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#migration configurations

migrate = Migrate(app, db)

#criação básica de fornecedores e suas notas

class Fornecedores(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    nome =  db.Column(db.String(),nullable=False)
    endereco = db.Column(db.String())  
    cnpj = db.Column(db.String(),nullable=False)
    notas =  db.relationship('Notas', backref='fornecedores', lazy=True)


class Notas(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    status = db.Column(db.String())
    numero = db.Column(db.Integer())
    forn_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'),nullable=False)
    valor = db.Column(db.Float(),nullable=False)






db.create_all()




