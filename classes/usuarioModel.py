import datetime
import hashlib
from classes.conexao import conexao
from classes.dataManipulation import dataManipulation

class usuarioModel:

    def buscaId(self, idUser):
        # print('BUSCA ID')
        self.id = idUser
        c=conexao()
        cur = c.cur
        sql = f"""SELECT COUNT(idUser), idUser, usuario, senha, email, icone, dataNascimento, dataInsert, qtdeInsert,
                qtdeConfirmacao, qtdeRejeito, redeSocial1, redeSocial2 FROM usuarios WHERE idUser = '{idUser}'"""
        cur.execute(sql)
        res = cur.fetchall()
        print(res)
        c.close()

        if res[0][0] == 0:
            return None
        else:
            # print('aqi')
            self.id = idUser
            self.usuario = res[0][2]
            self.senha = res[0][3]
            self.email = res[0][4]
            self.icone = res[0][5]
            self.dataNasc = res[0][6]
            self.dataInsert = res[0][7]
            self.qtdeInsert = res[0][8]
            self.qtdeConfirmacao = res[0][9]
            self.qtdeRejeito = res[0][10]
            self.redeSocial1 = res[0][11]
            self.redeSocial2 = res[0][12]
            return self.id
        

    def __init__(self, usuario = '', senha = ''):
        # self.id = idUser
        self.usuario = usuario
        self.senha = senha

    def set_all(self, usuario, senha, email, icone, dataNasc, redeS1, redeS2, qtIns,qtConf,qtRej):
        # self.id = idUser
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.icone = icone

        dtnAr = dataNasc.split('-')
        dtnStr = f"{dtnAr[0]}{dtnAr[1]}{dtnAr[2]}"

        self.dataNasc = dtnStr#dataNasc
        self.redeSocial1 = redeS1
        self.redeSocial2 = redeS2
        d = datetime.datetime.now()
        hoje = str(d.strftime("%Y%m%d"))
        self.dataInsert = hoje
        self.qtdeInsert = qtIns
        self.qtdeConfirmacao = qtConf
        self.qtdeRejeito = qtRej
    
    def get_usuario(self):
        return self.usuario
    
    def get_icone(self):
        return self.icone
    
    def get_id(self):
        return str(self.id)
        
    def respostaPerfil(self):
        print(self.dataInsert)
        dtn = dataManipulation.colocaBarras(self.dataNasc)
        dti = dataManipulation.colocaBarras(self.dataInsert)
        resposta = {'id':self.id,'usuario':self.usuario,'iconeVerUser':self.icone,
                    'dataInsert':dti,
                    'dataNascimento':dtn,
                    'qtdeInsert':self.qtdeInsert,
                    'qtdeConfirmacao':self.qtdeConfirmacao,'qtdeRejeito':self.qtdeRejeito}
        return resposta


    #Classes necessarias para usar o flask login 
    @property
    def is_authenticated(self):
        print("USUARIO LOGADO!!!!!!!!!!!!!!")
        return True
    
    @property
    def is_active(self):
        print("USUARIO LOGADO!!!!!!!!!!!!!!")
        return True
    
    @property
    def is_anonymous(self):
        return False
    

    
    def set_email(self, email):
        self.email = email
    #Precisa de nomeUsuario
    def usuarioExiste(self):
        c = conexao()
        cur=c.cur

        sql = f"SELECT COUNT(idUser) FROM usuarios WHERE usuario = '{self.usuario}'"
        cur.execute(sql)
        res = cur.fetchall()
        #c.close()

        if res[0][0] == 1:
            return True
        
        sql = f"SELECT COUNT(idUser) FROM usuarios WHERE email = '{self.email}'"
        cur.execute(sql)
        res = cur.fetchall()

        if res[0][0] == 1:
            return True
        else:
            return False #False é o esperado para incluir novo cadastro    
    
        
    #Precisa de nomeUsuario e senha
    def verificaLogin(self):
        c = conexao()
        cur=c.cur

        sql = f"SELECT COUNT(idUser), * FROM usuarios WHERE usuario = '{self.usuario}' AND senha = '{self.senha}'"
        #print(sql)
        cur.execute(sql)
        res = cur.fetchall()
        print(res)
        c.close()

        if res[0][0] == 1:
            self.id = res[0][1]
            return True
        else:
            return False
    
    def verificaLoginById(self, id):
        c = conexao()
        cur=c.cur

        sql = f"SELECT COUNT(idUser), * FROM usuarios WHERE idUser = {id}"
        #print(sql)
        cur.execute(sql)
        res = cur.fetchall()
        #print(res)
        c.close()

        if res[0][0] == 1:
            self.id = res[0][1]
            return True
        else:
            return False

    def inserirNoBanco(self):
        #c = conexao()
        #cur=c.cur

        hash_object = hashlib.sha256()
    
        #Converte o password para Byte e encoda
        hash_object.update(self.senha.encode())

        #Pega o valor hex do metodo hash
        hash_password = hash_object.hexdigest()

        sql = f"""INSERT INTO usuarios (usuario, senha, email, icone, dataNascimento, dataInsert, qtdeInsert)
        VALUES ('{self.usuario}','{hash_password}','{self.email}',{self.icone},'{self.dataNasc}','{self.dataInsert}',0)"""

        print (sql)

    def userAddInsertLocal(self):
        try:
            c = conexao()
            cur=c.cur

            sql = f"SELECT qtdeInsert From usuarios WHERE idUser = {self.id}"
            cur.execute(sql)
            res = cur.fetchall()

            qtdeInsert =  res[0][0]

            sql = f"UPDATE usuarios SET qtdeInsert = {qtdeInsert+1} WHERE idUser = {self.id}"
            cur.execute(sql)
            c.con.commit()
            c.close()
        except:
            return False
        
    def getListaUsuarios(self):
        #try:
        c = conexao()
        cur=c.cur

        sql = f"SELECT idUser, usuario FROM usuarios"
        cur.execute(sql)
        res = cur.fetchall()

        resposta = []
        for r in res:
            resposta.append({'id':r[0],'usuario':r[1]})# = {'id':r[0],'usuario':r[1]}

        c.close()
        return resposta
        #except:
        #    return False
        
