from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, CardTransition, FallOutTransition
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

import func
from time import sleep

from gamefunc import team_list
from temp import *
import random

Window.size = (310, 580)


class Card:
    dice = 0
    theme = 'theme'
    word = 'word'
    icon = ""
    method = 'method'
    desc = 'decs'


class MainApp(MDApp):
    new_card = Card()

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("start.kv"))
        screen_manager.add_widget(Builder.load_file("ready.kv"))
        # screen_manager.add_widget(Builder.load_file("teams.kv"))
        # screen_manager.add_widget(Builder.load_file("teams1.kv"))

        self.theme_cls.primary_palette = "Indigo"
        print(screen_manager.screens[1].ids.dice_res.text)
        return screen_manager

    def dice(self):
        """Моделируем бросок кубика"""
        dice_roll = random.randint(1, 6)
        """Обращаемся к элементу KV по ID"""
        screen_manager.screens[1].ids.dice_res.text = str(dice_roll)
        card_num = random.randint(1, 8)
        self.get_data_for_card(dice_roll, card_num)

    def get_data_for_card(self, dice_roll, card_num):
        """Возвращаем список значений"""
        texts = func.return_base(dice_roll, card_num)
        """Передаем ТЕМУ в text6, если на кубике 6"""
        text6 = texts[4] if texts[1] == 6 else False
        add_text = func.return_add(dice_roll, text6)
        self.create_card(texts, add_text)
        """Переключение экрана"""
        if text6:
            screen_manager.add_widget(Builder.load_file("card6.kv"))
            screen_manager.current = 'card6'
        else:
            screen_manager.add_widget(Builder.load_file("card5.kv"))
            screen_manager.current = 'card5'

    def create_card(self, texts, add_text):
        self.new_card.icon = f'dice-{texts[1]}'
        self.new_card.theme = texts[2]
        self.new_card.word = texts[3]
        self.new_card.method = add_text[2]
        self.new_card.desc = add_text[3]
        print('OK new card')

    def set_teams(self):
        """Формируем лист играющих команд"""
        team_num = int(screen_manager.screens[0].ids.slider.value)
        print('Показания слайдера', team_num)
        screen_manager.add_widget(Builder.load_string(team_list(team_num)))
        screen_manager.current = 'teams1'

    def quit(self):
        exit()


if __name__ == '__main__':
    MainApp().run()
"""
font_style are: ‘H1’, ‘H2’, ‘H3’, ‘H4’, ‘H5’, ‘H6’, 
‘Subtitle1’, ‘Subtitle2’, ‘Body1’, ‘Body2’, ‘Button’, 
‘Caption’, ‘Overline’, ‘Icon’."""
