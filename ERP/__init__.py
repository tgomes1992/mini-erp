from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

# csrf = CSRFProtect(app)


from ERP import views

