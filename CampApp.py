import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

_DEBUG = 0
if _DEBUG:
    from kivy.config import Config
    from kivy.lang.builder import Builder
    __scale = 45
    Config.set('graphics', 'width', str(9 *__scale))
    Config.set('graphics', 'height', str(16 * __scale))


class LoginScreen(Screen):
    pass


class AuthorScreen(Screen):
    pass


class Attention(Popup):
    pass


class CampApp(App):
    def graphical_init(self):
        self.attention = Attention()
        self.manager = ScreenManager()
        self.manager.add_widget(LoginScreen(name='login'))
        self.manager.add_widget(AuthorScreen(name='auth'))

    def build(self):
        self.graphical_init()
        return self.manager 

    def redirect(self, screen):
        self.manager.current = screen

if __name__ == '__main__':
    app = CampApp()
    app.run()
