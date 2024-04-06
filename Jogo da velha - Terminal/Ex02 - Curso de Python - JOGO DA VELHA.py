from random import randint

version = "0.3.5"

class Tabuleiro:
    def __init__(self, player01="Player01", player02="Player02"):
        self.player01_ = player01
        self.player02_ = player02
        self.p_player01 = 0
        self.p_player02 = 0
        self.p_empate = 0
        self.jogadas_ = None
        self.status_ = None
        self.tabuleiro_ = None

    def imprimir(self):
        i = self.tabuleiro_
        def co(l, c):
            if i[l][c] == True:
                return "X"
            elif i[l][c] == False:
                return "O"
            else:
                return " "
        print(f"{'|JOGO DA VELHA|':-^30}")
        print(f"{self.player01_}: {self.p_player01}\n{self.player02_}: {self.p_player02}\nVELHA: {self.p_empate}\n")
        print("    0 | 1 | 2 ")
        print("    v   v   v ")
        print(f"0 > {co(0, 0)} | {co(0, 1)} | {co(0, 2)}")
        print("    ----------")
        print(f"1 > {co(1, 0)} | {co(1, 1)} | {co(1, 2)}")
        print("    ----------")
        print(f"2 > {co(2, 0)} | {co(2, 1)} | {co(2, 2)}")

    def redefinir(self):
        self.tabuleiro_ = [[], [], []]
        self.status_ = None
        self.jogadas_ = 9
        for linha in self.tabuleiro_:
            for n in range(3):
                linha.append(" ")

    def jogar(self, linha, coluna, jogador):
        aux = self.tabuleiro_
        if aux[linha][coluna] == " ":
            aux[linha][coluna] = jogador
            self.set_jogadas()
            self.atualizar_status()
            return True
        else:
            return False

    def resultado(self):
        if self.status_ == True:
            self.p_player01 += 1
            self.imprimir()
            print(f"\n{'Parabéns, o jogador '+ self.player01_ +' ganhou.':>30}\n")
            return True
        elif self.status_ == False:
            self.p_player02 += 1
            self.imprimir()
            print(f"\n{'Parabéns, o jogador '+ self.player02_ +' ganhou.':>30}\n")
            return False
        elif (self.status_ == None) and (self.jogadas_ == 0):
            self.p_empate += 1
            self.imprimir()
            print(f"\n{'DEU VELHA, A PARTIDA EMPATOU.':>30}\n")
            return 999

    def atualizar_status(self):
        x = self.tabuleiro_
        ganhador = [True, False]  # True: "X", False: "O".
        # Se Ganhou nas Linhas
        for i in ganhador:
            for l in range(3):
                cont = 0
                for c in range(3):
                    if i == x[l][c]:
                        cont += 1
                if cont == 3:
                    self.status_ = i
            # Se Ganhou nas Colunas
            for l in range(3):
                cont = 0
                for c in range(3):
                    if i == x[c][l]:
                        cont += 1
                if cont == 3:
                    self.status_ = i
            # Se Ganhou na DIAGONAL CIMA para BAIXO
            cont = 0
            for l in range(3):
                if i == x[l][l]:
                    cont += 1
            if cont == 3:
                self.status_ = i
            # Se Ganhou na DIAGONAL BAIXO para CIMA
            cont = 0
            li = 0
            co = 2
            for n in range(3):
                if i == x[li][co]:
                    cont += 1
                li += 1
                co -= 1
            if cont == 3:
                self.status_ = i

    def get_jogadas(self):
        return self.jogadas_

    def set_jogadas(self):
        self.jogadas_ -= 1

    def get_status(self):
        return self.status_

    def get_jogador01(self):
        return self.player01_

    def set_jogador01(self, nome):
        self.player01_ = str(nome)

    def get_jogador02(self):
        return self.player02_

    def set_jogador02(self, nome):
        self.player02_ = str(nome)

    def get_p_player01(self):
        return self.p_player01

    def get_p_player02(self):
        return self.p_player02

    def get_p_empate(self):
        return self.p_empate

    def get_player01(self):
        return self.player01_

    def get_player02(self):
        return self.player02_

def vez_jogador(jogo, jogador=True):
    while True:
        jogo.imprimir()
        try:
            l = int(input("Linha:_ "))
            c = int(input("Coluna:_ "))
        except (ValueError, TypeError):
            print(f"{'OPÇÃO INVÁLIDA!':>30}")
        else:
            try:
                aux = jogo.jogar(linha=l, coluna=c, jogador=jogador)
            except:
                print(f"{'OPÇÃO INVÁLIDA!':>30}")
            else:
                if aux:
                    return True
                else:
                    print(f"{'Essa casa já foi preenchida.':>30}")

def vez_cpu(jogo):
    while jogo.get_jogadas() >= 1:
        l = randint(0, 2)
        c = randint(0, 2)
        if jogo.jogar(linha=l, coluna=c, jogador=False):
            return

def modo1():
    nome = str(input("Digite o nome do jogador:_"))
    vez = randint(1, 2)
    jogo = Tabuleiro(player01=nome, player02="CPU")
    while True:
        jogo.redefinir()
        vez = vez + 1
        if (vez % 2) == 0:
            while True:
                vez_jogador(jogo)
                aux = jogo.resultado()
                if aux == True:
                    break
                elif aux == 999:
                    break
                vez_cpu(jogo)
                if jogo.resultado() == False:
                    break
        else:
            while True:
                vez_cpu(jogo)
                aux = jogo.resultado()
                if aux == False:
                    break
                elif aux == 999:
                    break
                vez_jogador(jogo)
                if jogo.resultado() == True:
                    break
        escolha = str(input("Deseja jogar novamente? (S/N):_")).upper()
        if escolha != "S":
            return
        elif escolha == "N":
            return

def modo2():
    nome1 = str(input("Digite o nome do Jogador que vai jogar com X:_"))
    nome2 = str(input("Digite o nome do Jogador que vai jogar com O:_"))
    vez = randint(0, 3)
    jogo = Tabuleiro(player01=nome1, player02=nome2)
    while True:
        jogo.redefinir()
        vez += 1
        if (vez % 2) == 0:
            while True:
                print(f"{jogo.get_player01()} é a sua vez de jogar com X.")
                vez_jogador(jogo=jogo, jogador=True)
                aux = jogo.resultado()
                if aux == True:
                    break
                elif aux == 999:
                    break
                print(f"{jogo.get_player02()} é a sua vez de jogar com O.")
                vez_jogador(jogo=jogo, jogador=False)
                if jogo.resultado() == False:
                    break
        else:
            while True:
                print(f"{jogo.get_player02()} é a sua vez de jogar com O.")
                vez_jogador(jogo=jogo, jogador=False)
                aux = jogo.resultado()
                if aux == False:
                    break
                elif aux == 999:
                    break
                print(f"{jogo.get_player01()} é a sua vez de jogar com X.")
                vez_jogador(jogo=jogo, jogador=True)
                if jogo.resultado() == True:
                    break
        escolha = str(input("Deseja jogar novamente? (S/N):_")).upper()
        if escolha != "S":
            return
        elif escolha == "N":
            return

def menu():
    print(f"{'|JOGO DA VELHA|':-^30}\n")
    print("1 - Jogador:")
    print("2 - Jogadores:")
    print("\n0 - SAIR")
    print('-' * 30)
    opcao = input("Digite uma opção do menu:_ ")
    return opcao

def iniciar():
    while True:
        op = menu()
        if op == '1':
            modo1()
        elif op == '2':
            modo2()
        elif op == '0':
            print(f"\n{'PROGRAMA ENCERRADO.':>30}\n")
            print(f"Buid-{version}")
            print("(By Matheo Henrique M Silva)")
            return
        else:
            print(f"{'OPÇÃO INVÁLIDA!':>30}")

iniciar()
