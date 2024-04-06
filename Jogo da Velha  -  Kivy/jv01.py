from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from jv01Controlador import Tabuleiro
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from time import sleep

# Costumização da Tela.
Window.size = (700, 700)
Window.clearcolor = (46/255, 46/255, 51/255, 0.2)

# Controle de Tela.
class Telas(ScreenManager):
    pass

# Core da Tela INICIO.
class Inicio(Screen):
    pass

# Core da Tela de 1 jogador.
class Modo_jogo_01(Screen):
    def start(self):
        self.nome_players1()
        self.game = Tabuleiro()
        self.jogar_novamente()
        self.quem_joga()

    def jogar_novamente(self):
        self.game.reiniciar()
        self.mostrar()

    def nome_ganhou(self, ganhador):
        self.mostrar()
        if ganhador == None:
            x = f"DEU VELHA, NINGUÉM GANHOU!"
        else:
            x = f'PARABÉNS {ganhador.get_nome()} VOCÊ GANHOU A PARTIDA!'
        popup = BoxLayout(orientation='vertical', padding=15, spacing=15)
        self.pop = Popup(title=x, content=popup, size_hint=(None, None), size=(400, 300), title_size=30)
        popup.add_widget(Button(text='CONTINUAR', on_release=self.continuar_ganhou))
        popup.add_widget(Button(text='SAIR', on_release=self.fechar_ganhou))
        self.pop.open()

    def nome_players1(self):
        popup01 = BoxLayout(orientation='vertical', padding=15, spacing=15)
        self.pop1 = Popup(title='Insira o nome do PLAYER 01:',
                          content=popup01, size_hint=(None, None), size=(300, 200), title_size=18)
        self.pl01 = TextInput(multiline=False, font_size=24)
        popup01.add_widget(self.pl01)
        popup01.add_widget(Button(text='OK', on_release=self.fechar_popup1))
        self.pop1.open()

    def continuar_ganhou(self, *args):
        self.jogar_novamente()
        self.pop.dismiss()

    def fechar_ganhou(self, *args):
        app = App.get_running_app()
        app.root.current = 'tela_inicio'
        self.pop.dismiss()

    def fechar_popup1(self, *args):
        self.game.get_player_01().set_nome(nome=self.pl01.text)
        self.game.get_player_02().set_nome(nome='CPU')
        self.mostrar()
        self.pop1.dismiss()

    def clicar(self, id):
        # Se ainda tem jogadas.
        if self.game.get_jogadas() >= 1:
            id = self.transformar_id(id=id)
            if self.game.jogar(jogador=self.game.get_vez(), id_casa=id) == True:
                self.game.set_vez()
                self.game.set_jogadas()
                self.mostrar()
                self.quem_joga()
                # Se alguém ganhou.
                x = self.game.atualizar_status()
                if x != None:
                    self.game.set_vez()
                    self.nome_ganhou(ganhador=x)
        # Se deu velha.
        if self.game.get_jogadas() < 1 and self.game.get_status() == None:
            self.game.set_pontos_velha()
            self.game.set_vez()
            self.nome_ganhou(ganhador=self.game.atualizar_status())
            self.jogar_novamente()
            self.quem_joga()

    def quem_joga(self):
        if self.game.get_vez() == self.game.get_player_02():
            self.game.cpu_jogar()
            self.game.set_vez()
            self.game.set_jogadas()
            self.mostrar()
            sleep(1.5)

    def transformar_id(self, id):
        if id == 'aa':
            id = '00'
        elif id == 'ab':
            id = '01'
        elif id == 'ac':
            id = '02'
        elif id == 'ba':
            id = '10'
        elif id == 'bb':
            id = '11'
        elif id == 'bc':
            id = '12'
        elif id == 'ca':
            id = '20'
        elif id == 'cb':
            id = '21'
        elif id == 'cc':
            id = '22'
        return id

    def mostrar(self):
        pontos_j1 = str(self.game.get_player_01().get_pontos())
        pontos_j2 = str(self.game.get_player_02().get_pontos())
        pontos_e0 = str(self.game.get_pontos_velha())
        self.ids.pontos_j1.text = f"{self.game.get_player_01().get_nome()}: {pontos_j1}"
        self.ids.pontos_j2.text = f"{self.game.get_player_02().get_nome()}: {pontos_j2}"
        self.ids.pontos_e0.text = f"Velha: {pontos_e0}"
        self.ids.vez.text = f"É a vez de -=-{self.game.vez__.get_nome()}-=- jogar com ({self.game.vez__.get_xo()})."
        self.ids.aa.text = self.game.get_tabuleiro()['00']
        self.ids.ab.text = self.game.get_tabuleiro()['01']
        self.ids.ac.text = self.game.get_tabuleiro()['02']
        self.ids.ba.text = self.game.get_tabuleiro()['10']
        self.ids.bb.text = self.game.get_tabuleiro()['11']
        self.ids.bc.text = self.game.get_tabuleiro()['12']
        self.ids.ca.text = self.game.get_tabuleiro()['20']
        self.ids.cb.text = self.game.get_tabuleiro()['21']
        self.ids.cc.text = self.game.get_tabuleiro()['22']

# Core da Tela de 2 jogadores.
class Modo_jogo_02(Screen):
    def start(self):
        self.nome_players2()
        self.nome_players1()
        self.game = Tabuleiro()
        self.jogar_novamente()

    def jogar_novamente(self):
        self.game.reiniciar()
        self.mostrar()

    def nome_ganhou(self, ganhador):
        self.mostrar()
        if ganhador == None:
            x = f"DEU VELHA, NINGUÉM GANHOU!"
        else:
            x = f'PARABÉNS {ganhador.get_nome()} VOCÊ GANHOU A PARTIDA!'
        popup = BoxLayout(orientation='vertical', padding=15, spacing=15)
        self.pop = Popup(title=x,
                          content=popup, size_hint=(None, None), size=(400, 300), title_size=30)
        popup.add_widget(Button(text='CONTINUAR', on_release=self.continuar_ganhou))
        popup.add_widget(Button(text='SAIR', on_release=self.fechar_ganhou))
        self.pop.open()

    def nome_players1(self):
        popup01 = BoxLayout(orientation='vertical', padding=15, spacing=15)
        self.pop1 = Popup(title='Insira o nome do PLAYER 01:',
                         content=popup01, size_hint=(None, None), size=(300, 200), title_size=18)
        self.pl01 = TextInput(multiline=False, font_size=24)
        popup01.add_widget(self.pl01)
        popup01.add_widget(Button(text='OK', on_release=self.fechar_popup1))
        self.pop1.open()

    def nome_players2(self):
        popup02 = BoxLayout(orientation='vertical', padding=15, spacing=15)
        self.pop2 = Popup(title='Insira o nome do PLAYER 02:',
                         content=popup02, size_hint=(None, None), size=(300, 200), title_size=18)
        self.pl02 = TextInput(multiline=False, font_size=24)
        popup02.add_widget(self.pl02)
        popup02.add_widget(Button(text='OK', on_release=self.fechar_popup2))
        self.pop2.open()

    def continuar_ganhou(self, *args):
        self.jogar_novamente()
        self.pop.dismiss()

    def fechar_ganhou(self, *args):
        app = App.get_running_app()
        app.root.current = 'tela_inicio'
        self.pop.dismiss()

    def fechar_popup1(self, *args):
        self.game.get_player_01().set_nome(nome=self.pl01.text)
        self.mostrar()
        self.pop1.dismiss()

    def fechar_popup2(self, *args):
        self.game.get_player_02().set_nome(nome=self.pl02.text)
        self.mostrar()
        self.pop2.dismiss()

    def clicar(self, id):
        # Se ainda tem jogadas.
        if self.game.get_jogadas() >= 1:
            id = self.transformar_id(id=id)
            if self.game.jogar(jogador=self.game.get_vez(), id_casa=id) == True:
                self.game.set_vez()
                self.game.set_jogadas()
                self.mostrar()
                # Se alguém ganhou.
                x = self.game.atualizar_status()
                if x != None:
                    self.game.set_vez()
                    self.nome_ganhou(ganhador=x)
            # Se deu velha.
            if self.game.get_jogadas() < 1 and self.game.get_status() == None:
                self.game.set_pontos_velha()
                self.game.set_vez()
                self.nome_ganhou(ganhador=self.game.atualizar_status())
                self.jogar_novamente()

    def transformar_id(self, id):
        if id == 'aa':
            id = '00'
        elif id == 'ab':
            id = '01'
        elif id == 'ac':
            id = '02'
        elif id == 'ba':
            id = '10'
        elif id == 'bb':
            id = '11'
        elif id == 'bc':
            id = '12'
        elif id == 'ca':
            id = '20'
        elif id == 'cb':
            id = '21'
        elif id == 'cc':
            id = '22'
        return id

    def mostrar(self):
        pontos_j1 = str(self.game.get_player_01().get_pontos())
        pontos_j2 = str(self.game.get_player_02().get_pontos())
        pontos_e0 = str(self.game.get_pontos_velha())
        self.ids.pontos_j1.text = f"{self.game.get_player_01().get_nome()}: {pontos_j1}"
        self.ids.pontos_j2.text = f"{self.game.get_player_02().get_nome()}: {pontos_j2}"
        self.ids.pontos_e0.text = f"Velha: {pontos_e0}"
        self.ids.vez.text = f"É a vez de -=-{self.game.vez__.get_nome()}-=- jogar com ({self.game.vez__.get_xo()})."
        self.ids.aa.text = self.game.get_tabuleiro()['00']
        self.ids.ab.text = self.game.get_tabuleiro()['01']
        self.ids.ac.text = self.game.get_tabuleiro()['02']
        self.ids.ba.text = self.game.get_tabuleiro()['10']
        self.ids.bb.text = self.game.get_tabuleiro()['11']
        self.ids.bc.text = self.game.get_tabuleiro()['12']
        self.ids.ca.text = self.game.get_tabuleiro()['20']
        self.ids.cb.text = self.game.get_tabuleiro()['21']
        self.ids.cc.text = self.game.get_tabuleiro()['22']



# Inicializador do Programa.
class jv01(App):
    def build(self):
        return Telas()

jv01().run()
