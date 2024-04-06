from random import randint

class Jogador():
    def __init__(self, nome="Player 01", xo=None, id=None):
        self.nome__ = nome
        self.xo__ = xo
        self.pontos__ = 0
        self.id__ = id

    def get_nome(self):
        return self.nome__
    def set_nome(self, nome):
        self.nome__ = nome
    def get_pontos(self):
        return self.pontos__
    def set_pontos(self):
        self.pontos__ += 1
    def get_xo(self):
        return self.xo__
    def get_id(self):
        return self.id__


class Tabuleiro():
    def __init__(self, player_01='Player 01', player_02='Player 02'):
        self.tabuleiro__ = None
        self.player_01__ = Jogador(nome=player_01, xo="X", id=1)
        self.player_02__ = Jogador(nome=player_02, xo="O", id=2)
        self.vez__ = self.player_01__
        self.pontos_player_01__ = self.player_01__.get_pontos()
        self.pontos_player_02__ = self.player_02__.get_pontos()
        self.pontos_velha__ = 0
        self.sortear__ = randint(1, 2)
        self.jogadas__ = 9
        self.status__ = None

    def reiniciar(self):
        self.tabuleiro__ = {}
        self.status__ = None
        self.jogadas__ = 9
        if self.sortear__ == 1:
            self.set_vez()
        for linha in range(3):
            for coluna in range(3):
                aux = f'{linha}{coluna}'
                self.tabuleiro__[aux] = " "

    def jogar(self, jogador, id_casa):
        if self.get_tabuleiro()[id_casa] == " ":
            self.get_tabuleiro()[id_casa] = jogador.get_xo()
            return True
        else:
            return False

    def cpu_jogar(self):
        aux = ['00', '01', '02',
               '10', '11', '12',
               '20', '21', '22']
        if self.get_jogadas() >= 1:
            while True:
                x = randint(0, 8)
                if self.get_tabuleiro()[aux[x]] == " ":
                    self.get_tabuleiro()[aux[x]] = self.get_player_02().get_xo()
                    break

    def atualizar_status(self):
        game = self.get_tabuleiro()
        ganhador = [self.player_01__, self.player_02__]
        aux = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22'],['00', '10', '20'], ['01', '11', '21'], ['02', '12', '22'], ['00', '11', '22'], ['02', '11', '20']]
        for i in ganhador:
            for l in aux:
                if game[l[0]] == i.get_xo() and game[l[1]] == i.get_xo() and game[l[2]] == i.get_xo():
                    self.set_status(i)
                    i.set_pontos()
                    return i

    def get_pontos_velha(self):
        return self.pontos_velha__
    def set_pontos_velha(self):
        self.pontos_velha__ += 1
    def get_player_01(self):
        return self.player_01__
    def get_player_02(self):
        return self.player_02__
    def get_tabuleiro(self):
        return self.tabuleiro__
    def get_vez(self):
        return self.vez__
    def set_vez(self):
        if self.vez__ == self.player_01__:
            self.vez__ = self.player_02__
        else:
            self.vez__ = self.player_01__

    def get_sortear(self):
        return self.sortear__

    def get_jogadas(self):
        return self.jogadas__

    def set_jogadas(self):
        self.jogadas__ -= 1

    def get_status(self):
        return self.status__

    def set_status(self,status):
        self.status__ = status
