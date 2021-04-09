from ERP import app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:\Projects\MINI-ERP\ERP\main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#migration configurations
migrate = Migrate(app, db)

class Fornecedores(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name =  db.Column(db.String(),nullable=False)
    address = db.Column(db.String(),nullable=False)
    tax_id = db.Column(db.String(),nullable=False)

class Clientes(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name =  db.Column(db.String(),nullable=False)
    address = db.Column(db.String(),nullable=False)
    tax_id = db.Column(db.String(),nullable=False)
    description = db.Column(db.String(),nullable=False)








db.create_all()




