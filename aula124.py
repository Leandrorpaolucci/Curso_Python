class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando is True:
            print(f'{self.nome}, Você JÁ está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome}, NÃO está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')



camera1 = Camera('Canon')
camera2 = Camera('Sony')

camera1.filmar()
camera1.filmar()
camera1.fotografar()
camera1.parar_filmar()
camera1.fotografar()

camera2.fotografar()