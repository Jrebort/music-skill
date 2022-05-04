from mycroft import MycroftSkill, intent_file_handler


class Music(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.intent')
    def handle_music(self, message):
        self.speak_dialog('music')


def create_skill():
    return Music()

