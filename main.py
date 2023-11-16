from flask import Flask
from flask_login import LoginManager
from classes.usuarioModel import usuarioModel
from routes.mainRoutes import rotas
import os
from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)
app.config['SECRECT_KEY'] = os.getenv("CHAVE")
app.secret_key = os.getenv("CHAVE")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
    
#Rotas do projeto
app.register_blueprint(rotas)

@login_manager.user_loader
def load_user(user_id):
# def load_user(user_id):
    # print(session_token)
    user = usuarioModel()
    user.verificaLoginById(user_id)
    if(user):
        print("USUARIO LOGAADO")
        return user#str(user.get_id())
    else:
        print("USUARIO NAO ESTA LOGADO")
        return None
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", ssl_context="adhoc", debug=True)