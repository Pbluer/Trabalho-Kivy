from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
import os

usuer = ['admin','admin123']

class Lista_de_Camisa(FloatLayout):
    '''
    ESTOU TENTANDO ABRIR UM LAYOUT DE OUTRA PASTA KV
    '''
    pass

class Tela_de_Lista(FloatLayout):
    def camisa(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Lista_de_Camisa())

class Tela_de_Cadastro(FloatLayout):

    def registrar(self):
        rs_nome = self.ids.rs_nome.text
        rs_email = self.ids.rs_email.text
        rs_usuario = self.ids.rs_usuario.text
        rs_senha = self.ids.rs_senha.text
        usuer.append(rs_nome)
        usuer.append(rs_email)
        usuer.append(rs_usuario)
        usuer.append(rs_senha)
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Cadastro())

    def voltar(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_1())

class Tela_de_Login(FloatLayout):
    def login(self):
        login = self.ids.login.text
        senha = self.ids.senha.text

        if login in usuer and senha in usuer:
            Base.root_window.remove_widget(Base.root)
            Base.root_window.add_widget(Tela_de_Lista())

    def voltar(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_1())

class Tela_1(FloatLayout):

    def login(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Login())

    def registro(self):
        Base.root_window.remove_widget(Base.root)
        Base.root_window.add_widget(Tela_de_Cadastro())

class MainTela(App):
    def build(self):
        return Tela_1()

Window.size = 300,600
Base = MainTela()
Base.run()
