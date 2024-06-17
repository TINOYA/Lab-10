from handlers import dollar, euro, favourite, car, stop, randoms
from voice import voice


COMMANDS = [
    {'id': 0, 'text': 'доллар', 'handler': dollar},
    {'id': 1, 'text': 'евро', 'handler': euro},
    {'id': 3, 'text': 'любимчик', 'handler': favourite},
    {'id': 4, 'text': 'лучшая машина', 'handler': car},
    {'id': 5, 'text': 'стоп', 'handler': stop},
    {'id': 6, 'text': 'рандом', 'handler': randoms},


]

ACTIVATION = 'саша'
class Command:

    def __init__(self, text):
        self.text = text 
        self.map()

    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Извините, я не поняла вас')

    def run(self, cmd):
        handler = cmd['handler']
        handler(self.text)