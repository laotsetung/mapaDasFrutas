import hashlib

class Criptografia():

    def encryptar(self, senha):
        #Cria objeto hashlib
        hash_object = hashlib.sha256()
        #Converte o password para Byte e encoda
        hash_object.update(senha.encode())
        #Pega o valor hex do metodo hash
        hash_password = hash_object.hexdigest()

        return hash_password