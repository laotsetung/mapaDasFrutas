from flask import Blueprint, jsonify, render_template, request, url_for, flash, redirect
# import os
from dotenv import load_dotenv, dotenv_values
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from classes.conexao import conexao
from classes.frutaModel import frutaModel
from classes.localModel import localModel
import datetime

from classes.usuarioModel import usuarioModel

rotas = Blueprint("mainRoute", __name__)

def carregaUser():
    userId = current_user.get_id()
    if userId:
        user = usuarioModel()
        user.buscaId(userId)

        # usuario = {'{user.get_id()}','{user.get_usuario()}','{user.get_icone()}'}
        usuario = {'id':user.get_id(),'usuario':user.get_usuario(),'icone':user.get_icone()}

        return usuario
    else:
        return None
  
def limpaString(texto):
    caracteresTortos = ("'","=",'"',"´","`",",",";","%","¨","&","*","!","(",")","[","]","{","}","º","ª")

    for c in caracteresTortos:
        if c in texto:
            return False
        else:
            return True

    
# @rotas.route('/locais')
# def getLocais():
#     locais = localModel()
#     res = locais.carregaLocais()

#     return jsonify(res)

# @rotas.route('/frutas')
# def getFrutas():
#     frutas = frutaModel()
#     res = frutas.getListaFrutas()

#     return jsonify(res)

@rotas.route("/")
def main():
    print("ROTA / ")
        
    ip = request.remote_addr
    with open("log.txt", "a") as file1:
        file1.write(f"\n{ip} | {datetime.datetime.now()}")

    return render_template('getLocation.html')

@rotas.route("/index", methods=["POST","GET"])
def mapa():
    
    # print(f"USUARIO ATUAL : {x.get_id()}")
    print(f"---ROTA INDEX ; METODO = {request.method}")
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']

        locais = localModel()
        res = locais.carregaLocais(lat, lon)
        usuario = carregaUser()
        print(f"contagem: {len(res)}")

        print("---RENDERIZANDO index.html :")
        return render_template('index.html', markers=res, lat=lat, lon=lon, usuario=usuario)
    else:
        #return render_template('getLocation.html')
        if not request.args.get("lat") and not request.args.get("lon"):
            return render_template('getLocation.html')
        else:
            lat = request.args.get("lat")
            lon = request.args.get("lon")
            if (lat != "" and lon != ""):
                locais = localModel()
                res = locais.carregaLocais(lat, lon)
                usuario = carregaUser()

                print(f"---RENDERIZANDO index.html : {usuario}")
                return render_template('index.html', markers=res, lat=lat, lon=lon, usuario=usuario)
            else:
               return render_template('getLocation.html')

@rotas.route('/local', methods=['POST','GET'])
@login_required
def addLocalPost():
    print(f"---ROTA /LOCAL ; metodo = {request.method}")
    #Metodo POST - ADICIONAR NOVO LOCAL DE FRUTA
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']
        idFruta = request.form['idFruta']
        userId = current_user.get_id()
        usuario = carregaUser()

        #obs = request.form['obs']
        print(f"lat : {lat} / lon : {lon} / idFruta : {idFruta} ")

        novoPonto = localModel()
        novoPonto.novoLocal(lat, lon, idFruta, userId)
        if (novoPonto.inserirLocal()):
            print("---NOVO LOCAL ADICIONADO - REDIRECIONANDO PARA getLocation.HTML")
            return render_template("getLocation.html")
        else:
            print("---Erro ao inserir novo local!!")
            return "Erro ao inserir local <a href='/local'> VOLTAR </a>"
    else:
        #METODO GET - CARREGAR A PAGINA
        frutas = frutaModel()
        res = frutas.getListaFrutas()
        print("RENDERIZANDO addLocal.html")
        usuario = carregaUser()

        return render_template('addLocal.html', frutas=res, usuario=usuario )
# @rotas.route('/local', methods=['GET'])
# def addLocalGet():

    
@rotas.route('/admin')
def admin():
    locais = localModel()
    res = locais.carregaLocaisAdmin()
    print(res)
    return render_template('admin.html', markers=res)

@rotas.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        nomeUsuario = request.form['usuario']
        senha = request.form['senha']

        if limpaString(nomeUsuario) or limpaString(senha):
            usuario = usuarioModel(nomeUsuario,senha)
            
            if(usuario.verificaLogin()):
                login_user(usuario)
                print("!!!USUARIO LOGADO!!!")
                flash("Login realizado com sucesso!","ok")
                return redirect("/")
            else:
                #SE O USUARIO NAO ESTA LOGADO VAI PARA A PAGINA DE LOGIN
                flash("Usuario ou Senha Inválidos!", "erro")
                return render_template('login.html')
                #SE O USUARIO ESTIVER LOGADO, VAI PARA A PAGINA DE STATUS DA CONTA
        else:
            flash("Usuario ou Senha com Caracteres Inválidos!", "erro")
            return render_template('login.html')    
    else:
        return render_template('login.html')

@rotas.route('/cadastrar', methods=["POST","GET"])
def cadastrar():
    if request.method == 'POST':
        #TODO - ROTINA DE INSERIR USUARIO NO DB
        nomeUsuario = request.form['usuarioTxt']
        senha = request.form['senhaTxt']

        usuarioM = usuarioModel(nomeUsuario,senha)
        usuarioM.set_email(request.form['emailTxt'])

        if(not usuarioM.usuarioExiste()):
            usuarioM.set_all(nomeUsuario, senha, request.form['emailTxt'],
                             request.form['iconePerfil'], request.form['dataNascimento'],
                             request.form['redeSocial1'],request.form['redeSocial2'],0,0,0)
            
            usuarioM.inserirNoBanco()
            flash("Usuario Cadastrado com sucesso!!", "ok")
            #return render_template('index.html')
            return redirect("/")
        else:
            flash("Usuario ou Email já cadastrado!","erro")
            return render_template("cadastro.html")
        
        #return render_template('cadastro.html')
    else:
        return render_template('cadastro.html')

# @rotas.route('/deletar/<id>', methods=['GET'])
# def deletar(id):
#     if (id != ""):
#         try:
#             c = conexao()
#             cur = c.cur
#             sql = f"DELETE FROM locais WHERE idLocal = {id}"
#             cur.execute(sql)
#             c.close()
#         except:
#             return "Erro ao excluir registro <a href='/admin'> ADMIN </a>"
@rotas.route('/erro')
def rotaErro():
    render_template("erro.html")

@rotas.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout!","ok")
    return render_template('getLocation.html')

@rotas.route("/perfil/<id>")
def perfil(id):
    usuarioLogado = carregaUser()
    usuario = usuarioModel()
    
    usuario.buscaId(id)
    resposta = usuario.respostaPerfil()

    if usuarioLogado == None:
        return render_template('perfil.html', verPerfil=resposta)
    else:
        return render_template('perfil.html', verPerfil=resposta, usuario=usuario)
    
@rotas.route("/verUsuarios")
def verUsuarios():
    #usuario = usuarioModel()
    usuario = carregaUser()

    us = usuarioModel()
    resposta = us.getListaUsuarios()

    print(resposta)

    return render_template("verUsuarios.html", listaUsers=resposta, usuario=usuario)

@rotas.route("/estatisticas")
def estatisticas():
    usuario = carregaUser()

    f = frutaModel()
    frutas = f.getListaFrutas()
    print(frutas)
    qtdeFrutas = len(frutas)
    print(qtdeFrutas)

    l = localModel()
    locais = l.carregaLocais(1,1)
    qtdeLocais = len(locais)

    return render_template('estatisticas.html', usuario=usuario, frutas=frutas, qtdeFrutas=qtdeFrutas, locais=locais, qtdeLocais=qtdeLocais)

@rotas.route("/sobre")
def sobre():
    usuario = carregaUser()
    return render_template('sobre.html', usuario=usuario)

def montaMeses(meses):
    mesesArray = meses.split('-')
    mesesArrayInt = []
    for mes in mesesArray:
        mesesArrayInt.append(int(mes))

    resultado = []
    for a in range(1,13):
        b = int('0'+str(a)) if (a<10) else a

        if b in mesesArrayInt:
            resultado.append(1)
        else:
            resultado.append(0)

    print(resultado)
    return resultado

@rotas.route("/verFruta/<id>")
def verFruta(id):
    usuario = carregaUser()

    f = frutaModel()
    fruta = f.getFruta(id)
    meses = montaMeses(fruta[0][2])

    return render_template('verFruta.html', usuario=usuario, nomeFruta=fruta[0][1], idFruta=fruta[0][0], meses=meses, descricao=fruta[0][3])


@rotas.route("/estacao/<val>", methods=["GET"])
def estacao(val):
    
    # print(f"USUARIO ATUAL : {x.get_id()}")
    print(f"---ROTA Frutas da Estacao ; METODO = {request.method}")
    # if request.method == 'POST':
    #     lat = request.form['lat']
    #     lon = request.form['lon']

    #     locais = localModel()
    #     res = locais.carregaLocaisEstacao(lat, lon)
    #     usuario = carregaUser()
    #     print(res)
    #     print("---RENDERIZANDO index.html ESTACAO:")
    #     return render_template('index.html', markers=res, lat=lat, lon=lon, usuario=usuario)
    # else:
    #return render_template('getLocation.html')
    valores = val.split(";")
    lat = valores[0]
    lon = valores[1]
    if lat == "" or lon == "":
        flash("Erro ao recuperar Localização, Recarregando..", "erro")
        return render_template('getLocation.html')
    else:
        locais = localModel()
        res = locais.carregaLocaisEstacao(lat, lon)
        usuario = carregaUser()
        print(f"contagem: {len(res)}")
        print(f"---RENDERIZANDO index.html ESTACAO: {usuario}")
        # return ()
        # return redirect(url_for('mainRoute.mapa'), markers=res, lat=lat, lon=lon, usuario=usuario)
        
        return render_template('index.html', markers=res, lat=lat, lon=lon, usuario=usuario)
