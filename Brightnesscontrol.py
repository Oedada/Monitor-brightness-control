import kivy
kivy.require("1.0.7")# импортирую kivy 
from kivy.config import Config# импортирую конфиг
Config.set('graphics', 'resizable', False)# делаю размеры окна неизменяимыми
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.config import Config
from kivy.uix.image import Image 
import screen_brightness_control as sbc# импортирую библиотеку для контроля яркостью
Window.size=(450,190)
Window.clearcolor=(1,1,1,1)# задаю размеры окна и его цвет
class Brightness(App):# главный класс
    def build(self):# функция построения
        layout = FloatLayout()# создаю основной лаяут 
        bt = Button(# создаю кнопку 
            markup = True,# включаю метку
            text="[color=#FFFFFF]Start Game[/color]",# задаю текст и с помощью метки редактирую его цвет
            size_hint = (.5,.3),# задаю относительный размер
            on_press = self.send,# задаю функцию при нажатии
            pos_hint = {"x":0.25,"y":0},# задаю относительную позицию(всё относительно размеров окна)
            background_color = [1,1,1,0],# задаю фоновый цвет (прозрачный)
            background_normal = '' # задаю обычный фоновый цвет, чтобы не мешал, на ничего
        )
        self.sl = Slider(
            min=0, # задаю мин значение
            max=100, # задаю макс значение
            value=100,# задаю начальное значение
            value_track_color=[0, 0, 0, 1], # задаю цвет ползунка
            size_hint = (.9,.08),
            pos_hint={'center_x':0.5,'center_y':0.6},
            border_horizontal = (0,1,0,1),# я и сейчас не знаю что это надеюсь ты узнаешь
            opacity=0# задаю прозрачность
            )
        self.warp = Image(# делаю ручку ползунка
            source="Warp.png",
            size_hint=(0.4,0.4),
            pos=(180.5,270)
        )
        hp = Image(# делаю фон
            source="hp.png",
            size_hint=(.9,0.05),
            pos_hint={"x":0.05,"y":0.58},
            allow_stretch = True,# разрешаю растежение
            keep_ratio = False # разрешает изменять соотношение
        )
        background = Image(
            source="background.png",
            pos=(0,0),
            size_hint=(1,1),
            allow_stretch = True,
            keep_ratio = False
        )
        Clock.schedule_interval(self.update, 0.01)# обновляем позунок каждую сотую часть секунды
        layout.add_widget(background)
        layout.add_widget(bt)
        layout.add_widget(self.sl)
        layout.add_widget(hp)
        layout.add_widget(self.warp)# добавляю всё в лайаут
        return layout # возвращаю на построение лайаут
    def update(self, *args):# функция обновлений значений ручки ползунка
        self.warp.pos_hint = {'center_x':self.sl.value/111+0.05,'center_y':0.6}# изменяем значение кастомной ручки с пересчётом на значение относительно окна
        #print(str(self.warp.pos)+"///"+str(self.sl.value/111+0.05)) вывод значений для проверки
    def send(self,*args):# функция изменения яркости
        bright = (self.sl.value)//1# округляем значение до целого числа
        sbc.set_brightness(bright)# изменяем яркость экрана
        #print(self.warp.pos_hint) вывод значений для проверки
if __name__ == '__main__':
    Brightness().run()


