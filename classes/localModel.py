from classes.conexao import conexao
import datetime

from classes.usuarioModel import usuarioModel

class localModel:

    def __init__(self):
        pass

    def novoLocal(self, lat, lon, idFruta, idUser):
        self.lat = lat[0:10]
        self.lon = lon[0:10]
        self.idFruta = idFruta
        self.idUser = idUser

    def inserirLocal(self):
        try:
            c = conexao()
            cur = c.cur
            d = datetime.datetime.now()
            hoje = str(d.strftime("%Y%m%d"))
            
            sql = f"""INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert,ratingPos,ratingNeg) 
                    VALUES('{self.lat}', '{self.lon}',{self.idFruta},'ATIVO',{self.idUser},'{hoje}',0,0)"""
            
            cur.execute(sql)
            c.con.commit()

            #Todo - Usuario Acrescentar Um local

            usuario = usuarioModel()
            usuario.buscaId(self.idUser)
            usuario.userAddInsertLocal()

            c.close()
            return True
        except:
            return False

    def carregaLocais(self, lat, lon):
        try:
            lat = float(lat)
            lon = float(lon)

            latMin = lat - 1
            latMax = lat + 1
            lonMin = lon - 1
            lonMax = lon + 1

            c = conexao()
            cur = c.cur
            #Código para selecionar só os locais perto da localização
            """ sql = fSELECT l.idLocal, l.lat, l.lon, f.nomeFruta FROM locais l 
                        INNER JOIN frutas f ON f.idFruta = l.idFruta
                        WHERE l.lat < '{latMin}' AND l.lat > '{latMax}'
                        AND l.lon < '{lonMin}' AND l.lon > '{lonMax}'
                        """
            
            #Codigo que seleciona todas os locais da base de dados
            sql = """SELECT l.idLocal, l.lat, l.lon, f.nomeFruta, f.idFruta FROM locais l 
                        INNER JOIN frutas f ON f.idFruta = l.idFruta"""
            
            print(sql)
            cur.execute(sql)
            res = cur.fetchall()
            print(res)
            c.close()
            resposta = []
            for r in res:
                #print(r)
                item = {'lat':r[1],'lon':r[2],'popup':r[3],'id':r[4]}
                resposta.append(item)
            
            return resposta
        except:
            #c.close()
            return "Error Local"
        
    def carregaLocaisAdmin(self):
        try:
            c = conexao()
            cur = c.cur
            
            #Codigo que seleciona todas os locais da base de dados
            sql = """SELECT l.idLocal, l.lat, l.lon, f.nomeFruta FROM locais l 
                        INNER JOIN frutas f ON f.idFruta = l.idFruta"""
            
            #print(sql)
            cur.execute(sql)
            res = cur.fetchall()
            c.close()
            resposta = []
            for r in res:
                print(r)
                item = {'id':r[0],'lat':r[1],'lon':r[2],'nome':r[3]}
                resposta.append(item)
            
            return resposta
        except:
            c.close()
            return "Error Local"
        

    def carregaLocaisEstacao(self, lat, lon):
        try:
            print("Carrega locais estacao")
            if lat:
                lat = float(lat)
            if lon:
                lon = float(lon)

            # latMin = lat - 1
            # latMax = lat + 1
            # lonMin = lon - 1
            # lonMax = lon + 1
            d = datetime.datetime.now()
            mes = str(d.strftime("%m"))
            print(f"Mes: {mes}")
            c = conexao()
            cur = c.cur
            #Código para selecionar só os locais perto da localização
            """ sql = fSELECT l.idLocal, l.lat, l.lon, f.nomeFruta FROM locais l 
                        INNER JOIN frutas f ON f.idFruta = l.idFruta
                        WHERE l.lat < '{latMin}' AND l.lat > '{latMax}'
                        AND l.lon < '{lonMin}' AND l.lon > '{lonMax}'
                        """
            
            #Codigo que seleciona todas os locais da base de dados
            sql = f"""SELECT l.idLocal, l.lat, l.lon, f.nomeFruta, f.idFruta FROM locais l 
                        INNER JOIN frutas f ON f.idFruta = l.idFruta
                        WHERE f.estacao LIKE '%{mes}%'"""
            
            print(sql)
            cur.execute(sql)
            res = cur.fetchall()
            c.close()
            resposta = []
            for r in res:
                #print(r)
                item = {'lat':r[1],'lon':r[2],'popup':r[3],'id':r[4]}
                resposta.append(item)
            
            return resposta
        except:
            #c.close()
            return "Error Local"