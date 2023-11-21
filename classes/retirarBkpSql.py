import hashlib
from conexao import conexao

c = conexao()

cur = c.cur

#seleciona todas as frutas
#sql = "SELECT * FROM frutas WHERE nomeFruta = 'Caju'"
#cur.execute(sql)
#r = cur.fetchall()

# sql2 = "UPDATE frutas SET estacao = '01-08-09-10-11-12' WHERE nomeFruta = 'Caju'"
# cur.execute(sql2)
# c.con.commit()
senha = 'quake190'
hash_object = hashlib.sha256()

#Converte o password para Byte e encoda
hash_object.update(senha.encode())

#Pega o valor hex do metodo hash
hash_password = hash_object.hexdigest()

sql = f"UPDATE usuarios SET senha = '{hash_password}', qtdeInsert = 24 WHERE idUser = 1"
print(sql)
cur.execute(sql)
c.comita()
c.close()
#print(r)

# cur.execute(sql)
# res = cur.fetchall()
# bkpSqlTblFrutas = []

# for r in res:
#     sqlBkp = f"INSERT INTO fruta (nomeFruta, flag) VALUES('{r[1]}','{r[3]}')"
#     bkpSqlTblFrutas.append(sqlBkp)
    
# for a in bkpSqlTblFrutas:
#     print(a)

#seleciona todos os locais 
# alterar = "UPDATE locais SET lat='-22.745686', lon = '-47.626361' WHERE idLocal = 13"
# cur.execute(alterar)
# c.con.commit()

#sql = "SELECT l.idLocal, l.lat, l.lon, f.nomeFruta, l.obs, l.flag FROM locais l INNER JOIN frutas f ON f.idFruta = l.idFruta"# WHERE f.nomeFruta = 'Siriguela'"

#sql = "SELECT f.idFruta, f.nomeFruta from frutas f"
# lao = """INSERT INTO usuarios (usuario, senha, email, icone, dataNascimento, dataInsert, qtdeInsert)
#         VALUES ('Lao','quake190!','flavio.lao@gmail.com',1,'19870123','20230903',13)"""

"""sql = "UPDATE usuarios SET icone = 2 WHERE idUser = 1"

cur.execute(sql)
c.con.commit()

sql = "SELECT * FROM usuarios"
cur.execute(sql)
res = cur.fetchall()
print(res)
for r in res:
    print(r)"""
#(13, '-22.745646', '-47.626441', 'Siriguela', '', 'ATIVO')

# bkpLocais = []

# for r in res:
#     sqlBkp = f"INSERT INTO locais (lat,lon,idFruta,obs,flag) VALUES('{r[0]}', '{r[1]}',{r[2]},'{r[3]}','{r[4]}')"
#     bkpLocais.append(sqlBkp)

# for a in bkpLocais:
#     print(a)
    
#c.close()
