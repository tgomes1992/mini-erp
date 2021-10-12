from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField , SelectField ,IntegerField ,FloatField
from ERP.models import Fornecedores

class CadastroF(FlaskForm):
    nome = StringField('nome')
    endereco = StringField('endereco')
    cnpj = StringField('cnpj')
    submit = SubmitField("Cadastrar")


class NotasForm(FlaskForm):
    status = SelectField("status",choices=['Aberto',"Compensado"])
    numero = IntegerField('numero')
    fornecedor = SelectField("fornecedor", choices=[(item.id,item.nome) for item in Fornecedores.query.all()])
    valor = FloatField('valor')
    submit = SubmitField("Lançar")



