from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

loginn= ['admin123','ramon123']

usuario = ['Ramon']

class Camisa_002(FloatLayout):
    pass

class Camisa_001(FloatLayout):

    def voltar(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Lista_de_Camisa())

    def inicio(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Lista())

    def proximo(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Camisa_002())

class Lista_de_Camisa(FloatLayout):

    def voltar(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Lista())

    def proximo(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Camisa_001())


class Tela_de_Lista(FloatLayout):

    def camisa(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Lista_de_Camisa())

class Tela_de_Cadastro(FloatLayout):

    def registrar(self):

        #RETORNA TODA INFORMÇÃO DOS TEXTINPUT EM STRING
        rs_email = self.ids.rs_email.text
        rs_usuario = self.ids.rs_usuario.text
        rs_senha = self.ids.rs_senha.text

        #ADICIONA AS INFORMAÇÕES EM UMA LISTA
        loginn.append(rs_email)
        usuario.append(rs_usuario)
        loginn.append(rs_senha)

        #info_usuario = self.id.usuario.text = ''
        #self.ids.usuario.text = usuario

        #ABRE A TELA DE LOGIN
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Login())

    def voltar(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Login())

class Tela_de_Login(FloatLayout):


    def login(self):
        login = self.ids.login.text
        senha = self.ids.senha.text

        if login in loginn and senha in loginn:
            Base.root_window.remove_widget(Base.root)
            Base.root_window.add_widget(Tela_de_Lista())

    def voltar(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Cadastro())


class MainTela(App):
    def build(self):
        return Tela_de_Login()

Window.size = 300,600
Base = MainTela()
Base.run()
