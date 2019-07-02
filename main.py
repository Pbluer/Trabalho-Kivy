from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#LISTA PARA SALVAR OS CADASTRO
login = ['admin123','admin']
user = []

kv =Builder.load_file('maintela.kv')

'''================ TELAS ==================='''

class TelaLogin(Screen):

    def cadastroBT(self):
        sm.current = 'cadastro'

    def loginBT(self):
        email = self.ids.email.text
        senha = self.ids.senha.text

        if email in login and senha in login:
            sm.current = 'escolha'

class TelaCadastro(Screen):

    def finalizarBT(self):
        email = self.ids.email.text
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text

        login.append(email)
        login.append(senha)
        user.append(usuario)

        sm.current = 'login'

    def voltarBT(self):
        self.ids.email.text = ''
        self.ids.usuario = ''
        self.ids.senha.text = ''
        sm.current = 'login'

class TelaEscolha(Screen):
    pass

'''============= SCREEN MANAGER ============'''

class ControleTela(ScreenManager):
    pass

sm = ControleTela()

janela = [TelaLogin(name='login'),
          TelaCadastro(name='cadastro'),
          TelaEscolha(name='escolha')]

for janela in janela:
    sm.add_widget(janela)
#DEFINE A TELA QUE IRÁ APARECER QUADNO O APP ABRE
sm.current = "login"

'''=============== CLASSE BASE ==============='''
Window.size = 300,600
class MainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()
