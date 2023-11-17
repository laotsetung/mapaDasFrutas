from conexao import conexao

c = conexao()

con = c.con
cur = c.cur

sql1 = "SELECT * FROM locais"

"""idLocal INTEGER PRIMARY KEY AUTOINCREMENT,
    lat VARCHAR(25) NOT NULL,
    lon VARCHAR(25) NOT NULL,
    idFruta INTEGER NOT NULL,
    flag VARCHAR(20),
    idUsuario INTEGER NOT NULL,
    dataInsert VARCHAR(8) NOT NULL,
    ratingPos INTEGER DEFAULT 0,
    ratingNeg INTEGER DEFAULT 0,
    FOREIGN KEY(idFruta) REFERENCES frutas(idFruta),
    FOREIGN KEY(idUsuario) REFERENCES usuarios(idUser) """

cur.execute(sql1)
res = cur.fetchall()

for r in res:
    lat = r[1]
    lon = r[2]
    idFruta = r[3]
    flag = r[4]
    idUser = r[5]
    dtIns = r[6]
    ratingPos = r[7]
    ratingNeg = r[8]


    sql2 = f"""INSERT INTO locais(lat, lon, idFruta, flag, idUsuario, dataInsert, ratingPos, ratingNeg) VALUES('{lat}','{lon}',{idFruta},'{flag}',{idUser},'{dtIns}',{ratingPos},{ratingNeg})"""
    
    with open("bkpLocais.txt", "a") as file1:
        file1.write(f"{sql2}\n")

    
c.close()