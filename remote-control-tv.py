"""
Simple classes interactions exercise.

Television has volume, channel and on/off functions;
Remote Control has the ability to interact with television functions.
"""


class Television:
    def __init__(self):
        self.current_channel = 0
        self.current_volume = 0
        self.tv_on = False
        self.__max_volume = 50
        self.__max_channel = 999

    def get_max_volume(self):  # returns the Television maximum volume
        return self.__max_volume

    def get_max_channel(self):  # returns the Television maximum channel
        return self.__max_channel

    def tv_turn_on(self):  # turns the Television on
        self.tv_on = True

    def tv_turn_off(self):  # turns TV off and resets channel and volume
        self.tv_on = False
        self.current_channel = 0
        self.current_volume = 0

    def tv_volume_up(self):  # moves TV volume up by one unit if TV is on
        if self.tv_on:
            if self.current_volume < self.__max_volume:
                self.current_volume += 1
            else:
                print(f'TV is at the maximum volume: {self.__max_volume}')

    def tv_volume_down(self):  # moves TV volume down by one unit if TV is on
        if self.tv_on:
            if self.current_volume > 0:
                self.current_volume -= 1
            else:
                print('TV current volume is 0')

    def tv_channel_up(self):  # moves TV channel up by one unit if TV is on
        if self.tv_on:
            if self.current_channel < self.__max_channel:
                self.current_channel += 1
            else:
                print(f'TV is at the maximum channel: {self.__max_channel}')

    def tv_channel_down(self):  # moves TV volume down by one unit if TV is on
        if self.tv_on:
            if self.current_channel > 0:
                self.current_channel -= 1
            else:
                print('TV current channel number is 0')


class RemoteControl:
    def __init__(self, tv_object):  # requires a TV object instance
        self.__tv_object = tv_object

    def rc_turn_tv_on(self):  # interacts with 'turn on' TV method
        self.__tv_object.tv_turn_on()

    def rc_turn_tv_off(self):  # interacts with 'turn off' TV method
        self.__tv_object.tv_turn_off()

    def rc_volume_up(self):  # interacts with 'volume up' TV method if TV's on
        if self.__tv_object.tv_on:
            if self.__tv_object.current_volume < \
                    self.__tv_object.get_max_volume():
                self.__tv_object.tv_volume_up()
            else:
                print(
                    f'TV is at the maximum volume: '
                    f'{self.__tv_object.get_max_volume()}')

    def rc_volume_down(self):  # interacts with 'volume down' TV method
        if self.__tv_object.tv_on:
            if self.__tv_object.current_volume > 0:
                self.__tv_object.tv_volume_down()
            else:
                print('TV current volume is 0')

    def rc_channel_up(self):  # interacts with 'channel up' TV method.
        if self.__tv_object.tv_on:
            if self.__tv_object.current_channel < \
                    self.__tv_object.get_max_channel():
                self.__tv_object.tv_channel_up()
            else:
                print(
                    f'TV is at the maximum channel: '
                    f'{self.__tv_object.get_max_channel()}'
                )

    def rc_channel_down(self):  # interacts with 'channel down' TV method.
        if self.__tv_object.tv_on:
            if self.__tv_object.current_channel > 0:
                self.__tv_object.tv_channel_down()
            else:
                print('TV current channel number is 0')

    def rc_channel_dial(self, channel_number):  # selects TV channel number
        if self.__tv_object.tv_on:
            if 0 <= channel_number <= self.__tv_object.get_max_channel():
                self.__tv_object.current_channel = channel_number
            else:
                print(f'Channel number must be between 0 and '
                      f'{self.__tv_object.get_max_channel()}')

    def rc_channel_display(self):  # shows TV current channel
        if self.__tv_object.tv_on:
            return f'Selected channel: {self.__tv_object.current_channel}'

    def rc_volume_display(self):  # shows TV current volume
        if self.__tv_object.tv_on:
            return f'Selected volume: {self.__tv_object.current_volume}'
