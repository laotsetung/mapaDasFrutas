from classes.conexao import conexao

class frutaModel:

    def novaFrutaModel(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def frutaInDB(self):
        try:
            c = conexao()
            sql = f"SELECT COUNT(idFruta) FROM frutas WHERE nomeFruta = '{self.nome}'"
            print(sql)

            #con = c.con
            cur = c.cur
            cur.execute(sql)
            resultado = cur.fetchall()
            print(resultado)
            print(resultado[0][0])
            if resultado[0][0] == 1:
                c.close()
                return 1 # 1 = True
            else:
                c.close()
                return 0 # 0 = False
        except:
            c.close()
            print ("Error")
            return 9 #9 = error
        
    # def adicionaFrutaDb(self):
    #     try:
    #         c = conexao()
    #         sql = f"INSERT INTO frutas (nomeFruta, flag) VALUES ('{self.nome}','{self.cor}','ATIVO')"

    #         #con = c.con
    #         cur = c.cur
    #         try:
    #             cur.execute(sql)
    #             c.con.commit()
                
    #             print("Fruta adicionada no banco de dados")
    #             c.close()
    #             return 1
    #         except:
    #             print("Erro ao adicionar fruta no banco de dados")
    #             c.close()
    #             return 0
    #     except:
    #         c.close()
    #         print("Erro ao conectar com o banco de dados!")
    #         return 9
        
    def getListaFrutas(self):
        try:
            c = conexao()
            #con = c.con
            cur = c.cur
            sql = "SELECT idFruta, nomeFruta FROM frutas ORDER BY nomeFruta"

            cur.execute(sql)
            res = cur.fetchall()

            c.close()
            print(res)
            return res
        except:
            print("Error pegar lista de frutas")
            c.close()
            return None
        
    def getFruta(self, id):
        try:
            c = conexao()
            #con = c.con
            cur = c.cur
            sql = f"SELECT * FROM frutas WHERE idFruta = {id}"

            cur.execute(sql)
            res = cur.fetchall()

            c.close()
            print(res)
            return res
        except:
            print("Error pegar fruta")
            c.close()
            return None