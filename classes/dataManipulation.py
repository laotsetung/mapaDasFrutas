import datetime

class dataManipulation:

    def dataHoje():
        d = datetime.datetime.now()
        hoje = str(d.strftime("%Y%m%d"))
        return hoje
    
    def getMes():
        d = datetime.datetime.now()
        mes = str(d.strftime("%m"))
        return mes
    
    def retiraBarras(dataStr):
        dtnAr = dataStr.split('-')
        dtnStr = f"{dtnAr[0]}{dtnAr[1]}{dtnAr[2]}"

        return dtnStr
    
    def colocaBarras(dataStr):
        res = dataStr[0:4]+'/'+dataStr[4:6]+'/'+dataStr[-2:]
        return res
