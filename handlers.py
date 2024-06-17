import random
from voice import voice
import webbrowser
import requests
import pyautogui


def dollar(text):
    options = [
        'Вот текущий курс доллара',
        'Пурум пум пум',
        'Непхолой курс доллара',
    ]
    webbrowser.open('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+&gs_lcrp=EgZjaHJvbWUqEAgBEAAYgwEYsQMYyQMYgAQyBggAEEUYOTIQCAEQABiDARixAxjJAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDIGCAQQRRg9MgYIBRBFGD0yBggGEEUYPTIGCAcQRRhB0gEIMjk1M2owajmoAgCwAgE&sourceid=chrome&ie=UTF-8')
    sel = random.choice(options)
    voice.text_to_speech(sel)

def euro(text):
    options = [
        'Вот  курс евро на данный момент',
        'Я бы на вашем месте купила бы узбекские сумы',
        'Ничего себе',
    ]
    webbrowser.open('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sca_esv=324d2da6d69578fe&sxsrf=ACQVn08Qw-4Yaje_BEOF7Tkl6SI6mOcrPQ%3A1714147694489&ei=btErZs23HZ62wPAP78KK8AU&ved=0ahUKEwjNprDjoeCFAxUeGxAIHW-hAl4Q4dUDCBA&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiEdC60YPRgNGBINC10LLRgNC-MhMQABiABBixAxiDARjJAxhGGIICMggQABiABBixAzILEAAYgAQYsQMYgwEyDhAAGIAEGLEDGJIDGIMBMgsQABiABBiSAxiKBTIFEAAYgAQyERAuGIAEGLEDGIMBGMcBGK8BMgUQABiABDIFEAAYgAQyCxAAGIAEGLEDGIMBMh8QABiABBixAxiDARjJAxhGGIICGJcFGIwFGN0E2AEBSJoRUKEGWJEOcAN4AZABAJgBO6AB7wOqAQE5uAEDyAEA-AEBmAIMoALRBMICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIKECMYgAQYJxiKBcICChAAGIAEGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgIQEAAYgAQYsQMYgwEYFBiHAsICDRAAGIAEGLEDGEMYigXCAg8QIxiABBgnGIoFGEYYggLCAggQABiABBiSA8ICGRAAGIAEGIoFGEYYggIYlwUYjAUY3QTYAQHCAgQQABgDwgIOEAAYgAQYsQMYgwEYyQOYAwCIBgGQBgq6BgYIARABGBOSBwIxMqAHk2A&sclient=gws-wiz-serp')
    sel = random.choice(options)
    voice.text_to_speech(sel)

def favourite(text):
    webbrowser.open('https://wallpapers.99px.ru/wallpapers/336806/')
    voice.text_to_speech('Вот ваш любимый персонаж из игры')

def car(text):
    webbrowser.open('https://www.reddit.com/r/needforspeed/comments/16gkrnz/rate_the_ride_episode_14_2003_bmw_m3_gtr_the_face/')
    voice.text_to_speech('Вот лучшая машина по вашему мнению')


def stop(text):
    options = [
        'Думаю,на сегодня хватит интернета',
        'Пора в ИТМО !',
        'Сессия зовет, студент вперед!'
    ]
    pyautogui.hotkey('ctrl', 'w')
    sel = random.choice(options)
    voice.text_to_speech(sel)


def randoms(text):
    options = [
        'https://www.youtube-tech.ru/random-pick/random-video/',
        'https://rand.by/image',
        'https://rand.by/geo',
        'https://allrandom.ru/igry/'
    ]
    sel = random.choice(options)
    webbrowser.open(sel)
    voice.text_to_speech('Что-нибудь интересненькое для вас')
