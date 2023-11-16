from conexao import conexao

c=conexao()
cur = c.cur

sql = """UPDATE fruta
        SET estacao = '0'"""

# sql = """ALTER TABLE fruta
#          ADD estacao VARCHAR(100);"""

cur.execute(sql)


sql = "SELECT * FROM fruta"
cur.execute(sql)
res = cur.fetchall()

for r in res:
    print(r)


# sql = """ALTER TABLE fruta
#          ADD estacao VARCHAR(100)"""

# sql = """ALTER TABLE fruta
#         DROP COLUMN cor"""

# cur.execute(sql)


c.close()


sql = "INSERT INTO fruta (nomeFruta, estacao) VALUES('Abacate','02-03-04')"

sql = "UPDATE fruta SET estacao = ''"

# (1, 'Amora', 'ATIVO', '0')
# (2, 'Abacate', 'ATIVO', '0')
# (3, 'Ameixa', 'ATIVO', '0')
# (4, 'Manga', 'ATIVO', '0')
# (5, 'Acerola', 'ATIVO', '0')
# (6, 'Pitanga', 'ATIVO', '0')
# (7, 'Goiaba', 'ATIVO', '0')
# (8, 'Jaboticaba', 'ATIVO', '0')
# (9, 'Banana', 'ATIVO', '0')
# (10, 'Cacau', 'ATIVO', '0')
# (11, 'Carambola', 'ATIVO', '0')
# (12, 'Coco', 'ATIVO', '0')
# (13, 'Jaca', 'ATIVO', '0')
# (14, 'Limão', 'ATIVO', '0')
# (15, 'Mamão', 'ATIVO', '0')
# (16, 'Maracujá', 'ATIVO', '0')
# (17, 'Romã', 'ATIVO', '0')
# (18, 'Siriguela', 'ATIVO', '0')