
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, CardTransition, FallOutTransition
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

import func
from time import sleep
from temp import *
import random


Window.size = (310, 580)

class Card:
    dice = 0
    theme = 'theme'
    word = 'word'



class MainApp(MDApp):
    new_card = Card()
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("media.kv"))
        screen_manager.add_widget(Builder.load_file("second.kv"))
        #screen_manager.add_widget(Builder.load_file("third.kv"))
        self.theme_cls.primary_palette = "BlueGray"
        return screen_manager

    def create_card(self, word):
        self.new_card.word = word
        print('OK new card')

    def dice(self):
        """Моделируем бросок кубика"""
        res = random.randint(1, 5)
        self.new_card.dice = res
        sleep(3)
        self.get_data_for_card(res)
        #return res

    def get_data_for_card(self, dice_res):
        """Вызываем метод формирования текста карты"""
        num = random.randint(1, 8)
        res = func.return_base(dice_res, num)
        print ("Выпало ", dice_res, "Карта №", num)
        print('res =', res)
        self.create_card(res)
        """Переключение экрана"""
        screen_manager.add_widget(Builder.load_file("third.kv"))

        screen_manager.current = 'third'
        return res

    # def set_word(self):

    def theme_name(self):
        theme_name = "Спойте песню, в которой есть загаданное слово (или однокоренное). Само слово во время пения произносить нельзя. 1 минута, 2 клетки вперед за каждое отгаданное слово."
        return theme_name

    def test(self, name):
        """Вызов функции из третьего файла"""
        func.test(name)

    def quit(self):
        exit()



if __name__ == '__main__':
    MainApp().run()
"""
font_style are: ‘H1’, ‘H2’, ‘H3’, ‘H4’, ‘H5’, ‘H6’, 
‘Subtitle1’, ‘Subtitle2’, ‘Body1’, ‘Body2’, ‘Button’, 
‘Caption’, ‘Overline’, ‘Icon’."""