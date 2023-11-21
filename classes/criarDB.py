import hashlib
from conexao import conexao

#try:
c = conexao()
con = c.con
cur = c.cur

#Criar a tabela de Frutas
tabelaFrutas = """CREATE TABLE frutas(
    idFruta INTEGER PRIMARY KEY AUTOINCREMENT,
    nomeFruta VARCHAR(42) NOT NULL,
    estacao VARCHAR(42) NOT NULL,
    descricao VARCHAR(1000) NOT NULL
)"""

cur.execute(tabelaFrutas)
c.comita()
#con.commit()

#ABACATE
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) 
            VALUES('Abacate','02-03-04-05',
            'O <b>ABACATE</b> tem mais de <b>30% DE GORDURAS</b>;É rico em açúcares e <b>vitaminas</b> e possui um dos mais elevados teores de <b>proteínas e vitamina A</b> entre as frutas;
            Alguns estudos demonstram que o abacate diminui o <b>COLESTEROL</b>;Combate a <b>ANEMIA</b>;O abacate é um ótimo aliado na dieta de pessoas com <b>DIABETES MELLITUS TIPO 2.</b>')""")
#con.commit()

#ABACAXI
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao)
            VALUES ('Abacaxi', '01-11-12',
            'O <b>ABACAXI</b> é um <b>INFRUTESCÊNCIA</b> das regiões tropicais e sub-tropicais, cultivado pelos indigenas da América;
            Rico em Vitaminas do complexo B, e nutrientes como manganês, magnésio e potássio, e também um composto ativo muito importante chamado <b>BROMELINA</b>;
            Auxilia na <b>DIGESTÃO</b>;
            Ótimo para consumir após exercicios físicos pois a <b>BROMELINA</b> acelera a recuperação dos musculos;
            Aumenta a <b>IMUNIDADE</b>')""")
#con.commit()

#ACEROLA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao)
            VALUES ('Acerola','10-11-12',
            'A <b>ACEROLA</b> é uma fruta nativa da América Central e América do Sul;
            Possui vitaminas A, B1 (tiamina), B2 (riboflavina), B3 (niacina), cálcio, fósforo, ferro e, principalmente, <b>VITAMINA C</b>, que, em algumas variedades, chega a estar presente em até 5 gramas por 100 gramas de polpa. Este valor chega a ser <b>oitenta vezes superior</b> ao da laranja e ao do limão.')""")
#con.commit()

#AMEIXA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao)
            VALUES ('Ameixa Nêspera','05-06-07-08-09-10',
            'É uma fruta rica em <b>vitamina C</b> e sais minerais como cálcio e fósforo;
            Nêsperas em calda são utilizadas na medicina tradicional chinesa como <b>expectorante</b> e para acalmar a garganta. As folhas da nespereira também são utilizadas para o preparo de compressas, chás e extratos. Possuem propriedades <b>antioxidantes</b> e podem auxiliar no combate ao diabetes, às inflamações de pele, ao câncer de pele, às viroses e, inclusive, no combate ao vírus HIV, devido à presença do ácido 2-alpha-hydoxyursolico nas folhas, que possui efeito anti-HIV')""")
#con.commit()

#AMORA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) 
            VALUES ('Amora','09-10-11',
            'A <b>AMORA</b> é uma fruta <b>NATIVA DO BRASIL</b>, ela é parente da <b>Framboesa</b>, e pertencem ao Genero: Rubus existente em diversas partes do planeta em climas temperados;
            "A amora é uma fruta altamente nutritiva de sabor doce e um pouco ácida. Composta por <b>85% DE ÁGUA</b> e vários minerais e vitaminas, a fruta é indicada no controle de hemorragias e da pressão arterial, além de exercer uma função antioxidante.')""")
con.commit()

#BANANA - 6
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) 
            VALUES('Banana','03-04-05-06-07-08-09-10-11-12',
            'Temos diversas <b>VARIEDADES DE BANANAS</b>, o que torna dificil estabelecer a estação do ano para sua colheita;
            Além de que a Bananeira não é uma Arvore e seus frutos brotam e amadurecem de acordo com a época em que a bananeira se desenvolveu;
            Cheia de nutrientes, a fruta auxilia a regularizar o sistema nervoso e o aparelho digestivo. Além disso, o consumo regular oferece resistência aos vasos sanguíneos e evita câimbras, devido à presença do potássio. Enquanto as vitaminas do complexo B são responsáveis pela renovação celular e dos músculos.')""")
#con.commit()
#Abacate, Abacaxi, Acerola, Ameixa Nêspera, Amora, Banana, Carambola, Caju

#CARAMBOLA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Carambola','01-02-06-07-08',
            'Carambola, também conhecida como fruta-estrela, é uma espécie de árvore nativa do Sudeste Asiático tropical;
            Rica em sais minerais (cálcio, fósforo e ferro) e contendo vitaminas A, C e do complexo B, a carambola é considerada uma fruta <b>febrífuga</b> (que serve para combater a febre), <b>antiescorbútica</b> (carência de vitamina C) e, devido à grande quantidade de ácido oxálico, estimulador do apetite;
            Seu suco pode ser usado para tirar manchas de ferro, de tintas e ainda limpar metais. Sua casca é utilizada como antidisentérico, por possuir alto teor de tanino - cujo poder adstringente pode prender o intestino.')""")
#con.commit()

#CACAU
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Cacau','05-09-10-11-12',
            'O cacaueiro é originário do Brasil;
            O cacau é rico em substâncias antioxidantes, ajudando a regular os níveis de colesterol circulante, o que ajuda a evitar a deposição de gordura nos vasos, prevenindo a formação de placas de ateroma e desenvolvimento de doenças cardiovasculares.')""")
#con.commit()

#CAJU
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Caju','01-08-09-10-11-12',
            'O que entendemos popularmente como "caju" se constitui de duas partes: o fruto propriamente dito, que é a <b>castanha</b>; e seu pedúnculo floral, o pseudofruto, um corpo piriforme, amarelo, rosado ou vermelho;
            O pseudofruto, é suculento e rico em vitamina C e ferro;
            Além de auxiliar na cicatrização de feridas e combate a infecções e inflamações, previne a anemia. Outros minerais encontrados na polpa são o cálcio - que fortalece os ossos do corpo. O fósforo - que participa do metabolismo de micronutrientes do corpo, e o cobre - que melhora a saúde da pele e dos cabelos.')""")
#con.commit()

#CAQUI
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Caqui','04-05-06',
            'O <b>CAQUI</b> ajuda a manter a saúde cardiovascular. Isso porque essa fruta contém antioxidantes, que combatem os riscos de doenças no coração. Essas substâncias antioxidantes previnem o surgimento de aterosclerose coronariana — ou seja, o acúmulo de placas de gorduras nas artérias.')""")
#con.commit()

#COCO
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Coco','01-02-03-04-05-06-07-08-09-10-11-12',
            'Fruto <b>EXTREMAMENTE</b> versátil com diversas aplicações que vão além da culinaria e medicina;
            Pode ser consumido <b>VERDE</b> ou </b>SECO</b>. Contendo a <b>Agua de Coco</b> quando verde. Faz-se <b>Leite de Coco</b>, <b>Óleo de Coco</b>, <b>Bio Combustivel</b>, as folhas são usadas em artesanato, a casca seca pode ser queimada;
            A água de coco é um <b>isotônico natural<b>, que hidrata por ser rica em sais minerais. Amacia a pele, reduz o nível de <b>COLESTEROL</b<, previne enjoos, auxilia no controle da <b>PRESSÃO ARTERIAL</b>, no funcionamento intestinal e ameniza dores de estômago ocasionadas por gastrites ou úlceras, agindo como anti-inflamatório. A polpa do coco também possui ação anti-inflamatória. É rica em fibras que auxilia o bom funcionamento intestinal, e em potássio, excelente fonte de energia pelo elevado teor de calorias.')""")
con.commit()

#CUPUAÇU
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Cupuaçu','01-02-03-11-12',
            'O cupuaçu é um fruto típico da Amazônia brasileira. Ele possui vitamina A, B1, B2 e C, sais minerais e pectina;
            A polpa branca do cupuaçu tem odor descrito como uma mistura de chocolate e abacaxi e é frequentemente utilizada em sobremesas, sucos e doces;
            O chá e o extrato das folhas tem efeito calmante e também são usados para tratar problemas intestinais, renais e respiratórios.')""")
#con.commit()

#FIGO
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Figo','01-02-03-12',
            'A muda de figueira é uma árvore exótica oriunda do Oriente Médio. Essa árvore frutífera se popularizou no território nacional por se adaptar facilmente ao clima brasileiro;
            Combate a <b>Prisão de Ventre</b>, evita <b>Pressão Alta</b>, Ajuda a combater <b>Diabetes</b>, Fortalece o <b>Sistema Imunológico</b>')""")
#con.commit()

#GOIABA - 14
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Goiaba','02-03-04',
            'Branca ou Vermelha as Goiabas são originária da América tropical. Ocorre sobretudo no Brasil, nas Antilhas;
            A goiaba é uma fruta rica em fibras que estimulam os movimentos intestinais, melhorando a digestão. Além disso, quando se ingere com casca, ajuda a combater a acidez do estômago, sendo excelente para o tratamento de úlceras gástricas e duodenais;
            Mas atenção pois as moscas também adoram Goiabas e colocam seus ovos nelas, gerando em seu interior o famoso <b>Bicho-da-Goiaba</b>, é comum envolver o fruto com papel para evitar as moscas e por consequencia as larvas.')""")
#con.commit()

#GRAVIOLA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Graviola','01-02-03',
            'A graviola é uma planta originária das Antilhas, onde se encontra em estado silvestre. É nativa das regiões tropicais das Américas e do Caribe e é amplamente propagada;
            A fruta é uma excelente fonte de vitamina C e do complexo B e possui alto teor de ferro, cálcio, potássio, fósforo e carboidratos, e pode ser consumida natural ou utilizada no preparo de sucos e receitas e suas folhas podem ser utilizadas para fazer chás;
            É Antioxidante, anti-inflamatória, tem possíveis propriedades anti-cancerígenas e rica em nutrientes.')""")
#con.commit()

#JABUTICABA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Jabuticaba','09-10-11',
            'Nativa da Mata-Atlantica a <b>JABUTICABA</b> é uma Arvoré <b>BRASILEIRA</b>, se destaca pois os frutos crescem diretamente do tronco, forrando-o;
            A fruta é pequena, de casca roxa e polpa branca, e contém ferro, vitaminas C, B, B2, B3 e carboidratos;
            Alivia a dor de garganta, Promove a saúde digestiva, Mantém ossos e dentes fortes, Traz benefícios para a pele, Combate a diarreia (popularmente "TAPA O C#" rs)')""")
#con.commit()

#JACA
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Jaca','01-02-11-12',
            'A jaca foi domesticada de forma independente no sul e no sudeste da Ásia e trazida pelos Portugueses ao Brasil;
            A polpa comestível é formada por 74% de água, 23% de carboidratos, 2% de proteína e 1% de gordura.')""")
#con.commit()

#Jambolão
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Jambolão','',
            'Também conhecido como Jamelão ou João-bolão. É uma fruta pouco conhecida por não ser muito comercializada, e portanto com pouco estudo;
            Mas é usada para auxiliar no tratamento de diabetes.')""")
#con.commit()

#Kiwi
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Kiwi','04-05-06-07-08',
            'Originária do sul da China. É considerado o fruto comercial com maior quantidade de vitamina C já identificado perdendo só para a acerola;
            Por ter fibras, vitamina K, A, E e B6, o kiwi também é benéfico para o bom funcionamento do intestino e aumenta a sensação de saciedade')""")
con.commit()

#Laranja
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Laranja','01-02-03-06-07-08-09-10-11-12',
            'A laranja originou-se em uma região que abrange a China meridional, o nordeste da Índia e Myanmar;
            rica em fibras, vitaminas A, vitamina C, flavonoides e betacaroteno com propriedades antioxidantes e anti-inflamatórias, que auxiliam no combate ao envelhecimento precoce, ajudam a reduzir o colesterol ruim, protegendo de doenças cardiovasculares, e fortalecem o sistema imunológico.')""")
#con.commit()

#Lichia
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Lichia','12',
            'A lichia é uma fruta de origem chinesa e é uma excelente fonte de vitamina C, ferro, cálcio, fibras e potássio;
            Contém aminoácidos incomuns que interrompem a gliconeogênese e a β-oxidação de ácidos graxos.')""")
#con.commit()

#Limão - 22
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Limão','01-02-03-04-05',
            'No Brasil a variedade mais comum é o Limão Taiti, em outras partes do mundo o Limão Siciliano (que veio da Persia, mas é original do sudoeste da Ásia)')""")
#con.commit()

#Maça
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Maça','02-03-04-05-06-07',
            'É um pseudofruto, originária da Ásia Ocidental;
            A maçã contém as seguintes vitaminas: B1, B2 e Niacina, além de sais minerais, como fósforo e ferro.É rica em quercetina, substância que ajuda a evitar a formação de coágulos sanguíneos capazes de provocar derrames. A maçã é recomendada para pessoas com problemas de intestino, obesidade, reumatismo, gota, diabetes, enfermidades da pele e do sistema nervoso.')""")
#con.commit()

#Mamão
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Mamão','01-02-03-10-11-12',
            'O mamão é uma fruta muito nutritiva, fonte de minerais e antioxidantes, além de excelente fonte de cálcio;
            Possui vitamina A, que auxilia a saúde da pele e da visão; e vitamina C, que fortalece o sistema imunológico. É rico em fibras, o que melhora o funcionamento intestinal, e suas sementes são ricas em carpaína, uma substância que possui ação anti-inflamatória.')""")
#con.commit()

#Manga - 25
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Manga','01-02-03-10-11-12',
            'A manga é a fruta nacional da Índia, onde há mais de 100 variedades;
            Uma manga fresca contém cerca de 15% de açúcar, até 1% de proteína e quantidades significativas de vitaminas, minerais e antioxidantes, podendo conter vitamina A, B e C.
            Graças à alta quantidade de ferro que contém, a manga é indicada para tratamentos de anemia e é benéfica para as mulheres grávidas e em períodos de menstruação. Pessoas que sofrem de cãimbras, stress e problemas cardíacos, podem se beneficiar das altas concentrações de potássio e magnésio existentes que também auxiliam àqueles que sofrem de acidose. As mangas também suavizam o intestino, tornando mais fácil a digestão')""")
#con.commit()


#Maracujá
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Maracujá','01-02-11-12',
            'Maracujá (do tupi mara kuya, "fruto que se serve" ou "alimento na cuia");
            Este fruto é fonte de vitaminas A, C e do complexo B. Além disso, apresenta boa quantidade de sais minerais (ferro, sódio, cálcio e fósforo);
            Sua utilização como sedativo (calmante) é conhecida desde a antiguidade, entretanto essa não é sua única utilização, pois pode ser utilizada como hipnótico, sonífero e tonificante')""")
#con.commit()

#Melancia
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Melancia','01-02-10-11-12',
            'É uma trepadeira rastejante originária da África;
            Suculenta e doce, com alto teor de água (cerca de 92%), ou seja, ajuda a manter a hidratação.
            Outro benefício é a vasodilatação impulsionada pela citrulina, um aminoácido que se concentra sobretudo naquela parte branquinha da melancia.')""")
#con.commit()

#Melão
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Melão','01-10-11-12',
            'É uma fruta provavelmente nativa do Oriente Médio;
            Contém quantidades razoáveis de Cálcio, Fósforo e Ferro, que contribuem para a formação dos ossos, dentes e sangue. Tem também vitamina A que protege a visão, vitamina C, que age contra infecções e Niacina, que combate problemas de pele. Por conter pectina e fibras solúveis, ajuda a controlar os níveis de colesterol no sangue. Tem alto teor de bioflavonoides, que aumentam a resistência dos vasos sanguíneos e capilares, além de ser útil no fortalecimento do sistema imunológico.')""")
#con.commit()

#Mexerica
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Mexerica','06-07-08-09',
            'Também conhecida como Tangerina, Pocã ou Bergamota;
            Boa fonte de vitaminas A e C e sais minerais como potássio, cálcio e fósforo;
            A vitamina C é essencial para o sistema imunológico. A vitamina A é indispensável para a saúde dos olhos e da pele e aumenta a resistência às infecções. As vitaminas do complexo B fortificam os nervos.')""")
con.commit()

#Morango
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Morango','08',
            'De Origem Europeia o Morango é rico em vitaminas como, por exemplo, vitamina C, A, E, B5 e B6;
            Os principais minerais presentes no morango são: Cálcio, Potássio, Ferro, Selênio e Magnésio;
            Todas essas substâncias têm a capacidade de proteger as células contra os efeitos dos radicais livres produzidos pelo organismo;
            Os principais beneficios são: fortalecimento do sistema imunológico, auxílio no bom funcionamento do sistema digestório, ação anti-inflamatória, auxílio no processo de cicatrização de ferimentos.')""")
#con.commit()

#Pera
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Pera','02-03-04-05',
            'A pera é um fruto rico em vitamina A e C, de baixo valor energético e elevado teor de água. Além disso, ela possui quantidades consideráveis de vitaminas B1, B2 e B3, sódio, potássio, fósforo, enxofre, magnésio, silício e ferro.')""")
#con.commit()

#Pêssego
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Pêssego','01-10-11-12',
            'O pêssego é rico em fibras, bom para o funcionamento do intestino e contém minerais, carboidratos, proteínas e vitaminas. É uma fruta que possui baixo teor calórico. O pêssego é o fruto do pessegueiro, uma pequena árvore nativa da China')""")
#con.commit()

#Pitanga - 33
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Pitanga','01-10-11-12',
            'A pitangueira é uma árvore nativa da Mata Atlântica brasileira;
            A pitanga é uma fruta que possui muitos nutrientes como vitaminas A, B e C, cálcio, fósforo, ferro e compostos fenólicos como flavonoides, carotenoides e antocianinas com propriedades antioxidantes, anti-inflamatórias, analgésicas e anti-hipertensivas, que auxiliam no combate ao envelhecimento precoce, nos sintomas de artrite e gota, nos problemas respiratórios e no desenvolvimento de doenças cardiovasculares, por exemplo.')""")
#con.commit()

#Romã
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Romã','09-10-11-12',
            'Estudos mostraram que a romã pode ajudar a reduzir a pressão arterial e ser utilizada na prevenção de alguns problemas cardiovasculares;
            Outro estudo mostra que o seu consumo leva a um aumento de testosterona que pode variar entre 16% e 30%. Também é popularmente conhecida por ter como ótimo fruto e semente para ajudar no controle regular do fluxo menstrual.')""")
#con.commit()

#Siriguela
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Siriguela','01-12',
            'Também conhecida como (S)Ceriguela ou Siringuela ela é nativa do Brasil;
            A seriguela é rica em antioxidantes, como o betacaroteno e a vitamina C - essas substâncias evitam a formação de radicais livres no organismo. Dessa forma, e fruta ajuda a prevenir o envelhecimento celular e o aparecimento de doenças como câncer, Alzheimer, doenças cardíacas e aterosclerose.')""")
#con.commit()

#Uva
cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('Uva','01-02-03-04-05-06-07',
            'Entre os nutrientes encontrados na uva, estão: vitamina E, vitamina C, vitamina K e vitamina A, além de minerais como o cálcio, ferro e potássio.')""")
#con.commit()

#cur.execute("""INSERT INTO frutas (nomeFruta, estacao, descricao) VALUES('','','')""")
con.commit()


#TODO

#CRIAR TABELA USUARIO

tabelaUsers = """CREATE TABLE usuarios(
    idUser INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario VARCHAR(42) NOT NULL,
    senha VARCHAR(500) NOT NULL,
    email VARCHAR(250) NOT NULL,
    icone INTEGER NOT NULL,
    dataNascimento VARCHAR(10),
    redeSocial1 VARCHAR(100),
    redeSocial2 VARCHAR(100),
    dataInsert VARCHAR(8) NOT NULL,
    qtdeInsert INTEGER DEFAULT 0,
    qtdeConfirmacao INTEGER DEFAULT 0,
    qtdeRejeito INTEGER DEFAULT 0
)"""

#Data AnoMesDia
cur.execute(tabelaUsers)
con.commit()

senha = 'quake190'
hash_object = hashlib.sha256()
#Converte o password para Byte e encoda
hash_object.update(senha.encode())
#Pega o valor hex do metodo hash
hash_password = hash_object.hexdigest()

lao = f"""INSERT INTO usuarios (usuario, senha, email, icone, dataNascimento, dataInsert, qtdeInsert)
        VALUES ('Lao','{hash_password}','flavio.lao@gmail.com',1,'19870123','20230903',24)"""

cur.execute(lao)
con.commit()

#REFAZER TABELA LOCAIS

tabelaLocais = """CREATE TABLE locais(
    idLocal INTEGER PRIMARY KEY AUTOINCREMENT,
    lat VARCHAR(25) NOT NULL,
    lon VARCHAR(25) NOT NULL,
    idFruta INTEGER NOT NULL,
    flag VARCHAR(20),
    idUsuario INTEGER NOT NULL,
    dataInsert VARCHAR(8) NOT NULL,
    ratingPos INTEGER DEFAULT 0,
    ratingNeg INTEGER DEFAULT 0,
    FOREIGN KEY(idFruta) REFERENCES frutas(idFruta),
    FOREIGN KEY(idUsuario) REFERENCES usuarios(idUser) 
)
"""
cur.execute(tabelaLocais)
con.commit()

cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.740961', '-47.624300',1,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.741568', '-47.624399',3,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.688744', '-47.637726',3,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.744034', '-47.618878',5,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.745638', '-47.626456',5,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.745906', '-47.626555',6,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.726095', '-47.634778',14,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.740601', '-47.624022',22,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.736763', '-47.623625',25,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.731267', '-47.636565',25,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.734413', '-47.640909',33,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.741333', '-47.624255',33,'ATIVO',1,'20231103')")
cur.execute("INSERT INTO locais (lat,lon,idFruta,flag,idUsuario,dataInsert) VALUES('-22.745646', '-47.626441',35,'ATIVO',1,'20231103')")

con.commit()

c.close()
# except:
#     c.close()
#     print("Erro ao criar database")