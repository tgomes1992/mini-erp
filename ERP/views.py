from flask import Flask , render_template,request,redirect,url_for,jsonify ,flash
from ERP.models import *
from ERP.forms import CadastroF , NotasForm


@app.route('/')
def home_page():
    return render_template('template_base.html')


@app.route("/cadastrofornecedor",methods=['GET'])
def criar_fornecedor():
        return render_template('cadastrofornecedores.html',form=CadastroF())

@app.route('/cadastrar_fornecedor',methods=['POST'])
def cadastrar_fornecedor():
    print (request.method)
    if request.method == 'POST':
        nforn = Fornecedores(nome=request.form['nome'],
                            endereco=request.form['endereco'],
                            cnpj=request.form['cnpj'])
        db.session.add(nforn)
        db.session.commit()
        db.session.close()
        flash("fornecedor cadastrado com sucesso")
        return redirect(url_for('criar_fornecedor'))


@app.route("/gerenciar_fornecedores")
def check_vendors():
    vendors = Fornecedores.query.all()
    #resultado = jsonify(vendors)
    return render_template('gerenciar_fornecedores.html',fornecedores=vendors)


@app.route('/editarFornecedor/<int:id>')
def get_fornecedor_id(id):
    item = Fornecedores.query.get(id)
    result = dict(fornecedor=item,form=CadastroF())
    return render_template('editar_fornecedor.html',data=result)

    
@app.route('/concluir_edicao/<int:id>',methods=['POST'])
def concluir_edicao(id):
    item = Fornecedores.query.get(id)
    item.nome = request.form['nome']
    item.cnpj = request.form['cnpj']
    item.endereco = request.form['endereco']
    db.session.commit()
    db.session.close()
    flash("completed")
    return redirect(url_for('check_vendors'))


@app.route('/lancar_notas')
def lancar_notas():
  return render_template('lancar_notas.html',form=NotasForm())


@app.route('/lancar_notas_concluir',methods=['POST'])
def lancar_notas_concluir():
    print (request.method)
    if request.method == 'POST':
        nota = Notas(status=request.form['status'],
                            numero=request.form['numero'],
                            valor=request.form['valor'].replace(",","."),
                            forn_id=request.form['fornecedor'])
        db.session.add(nota)
        db.session.commit()
        db.session.close()
        flash("nota registrada com sucesso")
        return redirect(url_for('lancar_notas'))


@app.route('/notas_lancadas',methods=['POST'])
def notas_lancadas():
    pass
