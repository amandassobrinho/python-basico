class Cliente:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.telefone = telefone
        self.email = email
    @property
    def nome(self):
        return self.__nome
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, novo_telefone):
        if not type(novo_telefone) is int:
            raise TypeError()
        else:
            self.__telefone = novo_telefone
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, novo_email):
        if not type(novo_email) is str:
            raise TypeError() 
        if not ("@" in novo_email):
            raise ValueError()
        else: self.__email = novo_email
    
