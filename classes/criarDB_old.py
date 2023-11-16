from conexao import conexao

try:
    c = conexao()
    con = c.con
    cur = c.cur

    #Criar a tabela de Frutas
    tabelaFrutas = """CREATE TABLE fruta(
        idFruta INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeFruta VARCHAR(32) NOT NULL,
        cor VARCHAR(32) NOT NULL,
        flag VARCHAR(50) NOT NULL
    )"""

    cur.execute(tabelaFrutas)
    con.commit()

    cur.execute("INSERT INTO fruta (nomeFruta, cor, flag) VALUES('Amora','Roxa','ATIVO')")
    cur.execute("INSERT INTO fruta (nomeFruta, cor, flag) VALUES('Abacate','Verde','ATIVO')")
    con.commit()

    tabelaLocais = """CREATE TABLE locais(
        idLocal INTEGER PRIMARY KEY AUTOINCREMENT,
        lat VARCHAR(25) NOT NULL,
        lon VARCHAR(25) NOT NULL,
        idFruta INTEGER NOT NULL,
        obs VARHCAR(1000),
        flag VARCHAR(20),
        FOREIGN KEY(idFruta) REFERENCES fruta(idFruta)
    )
    """
    cur.execute(tabelaLocais)
    con.commit()

    cur.execute("INSERT INTO locais (lat,lon,idFruta,obs,flag) VALUES('-22.744034', '-47.618878',1,'','ATIVO')")
    cur.execute("INSERT INTO locais (lat,lon,idFruta,obs,flag) VALUES('-22.740961', '-47.624300',2,'','ATIVO')")
    con.commit()

    c.close()
except:
    c.close()
    print("Erro ao criar database")