class Mother:
    @staticmethod
    def take_screenshot():
        print('I can make a screenshot')

    @staticmethod
    def receive_email():
        print('I can receive email')


class Father:
    @staticmethod
    def drive_car():
        print('I can drive a car ')

    @staticmethod
    def play_music():
        print(f'Play music while driving')


class Grandfather:
    @staticmethod
    def smoke():
        print('I can drive a car ')

    @staticmethod
    def sing():
        print(f'Play music while driving')


class Kid(Mother, Father, Grandfather):

    def behave(self):
        self.take_screenshot()
        self.drive_car()
        self.smoke()


kid = Kid()
kid.behave()
kid.drive_car()
print(Kid.mro())