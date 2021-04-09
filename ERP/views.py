from ERP import app
from flask import Flask , render_template,request,redirect,url_for,jsonify
from ERP.models import *

def testeadd():
    teste = Fornecedores(name="São Paulo",address="Rua Paulo Santa helena 20",tax_id="1234567891011")
    db.session.add(teste)
    db.session.commit()
    db.session.close()

#testeadd()

@app.route('/')
def index():
    item = Fornecedores.query.all()
    teste = []
    for i in item:
        teste.append(i.name)
    return jsonify(teste)


