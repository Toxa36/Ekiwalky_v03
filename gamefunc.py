from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen


def team_list(team_num):
    KV = """MDScreen:
    id: teams1
    name: 'teams1'
    Image:
        source: 'D:\Python\Game_kivyMD\ekywalky1.jpeg'
        pos_hint: {'center_x': .5, "center_y": .9}
        size_hint_x: .8
    MDLabel:
        pos_hint: {'center_x': .5, "center_y": .75}
        text: 'ИМЕНА КОМАНД:'
        halign: 'center'
    MDFloatLayout:     
        """
    colors_list = ('1, 1, 0, .7', '0, 0, 1, .5', '0, 1, 0, .5', '1, 0, 0, .5', '1, .25, 0, .5')
    center_y = ('.65', '.55', '.45', '.35', '.25')
    text = ('ЖЕЛТЫЕ', 'СИНИЕ', 'ЗЕЛЕНЫЕ', 'КРАСНЫЕ', 'ОРАНЖЕВЫЕ')

    for i in range (team_num):
        new_text_field = f"""\r\t\tTextInput:
                         \r\t\t\tid: team{i+1}
                         \r\t\t\tbackground_color: {colors_list[i]}
                         \r\t\t\tpos_hint: {{'center_x': .5, 'center_y': {center_y[i]}}}
                         \r\t\t\ttext: \"{text[i]}\"
                         \r\t\t\thint_text: \"Команда 1\"
                         \r\t\t\tsize_hint: .8, None
                         \r\t\t\theight: \"30dp\"\n"""
        KV = KV + new_text_field
    print(KV)
    return KV

