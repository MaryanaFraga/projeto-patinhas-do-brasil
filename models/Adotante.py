class Adotante:
    
    def __init__(self, nome_completo, tel, rua, num, bairro, cidade, estado_sigla, obs='', id=None):
        self.id = id
        self.nome_completo = nome_completo
        self.tel = tel
        self.rua = rua
        self.num = num
        self.bairro = bairro
        self.cidade = cidade
        self.estado_sigla = estado_sigla
        self.obs = obs
