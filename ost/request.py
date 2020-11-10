class RemoteControlBase(object):
    """Абстрактный пульт управления"""
    def __init__(self):
        self._tv = self.get_tv()

    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    """Пульт управления"""
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0  # текущий канал

    def get_tv(self):
        return SharpTV()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


remote_control = RemoteControl()
remote_control.tune_channel(5)  # Sharp TV: выбран 5 канал
remote_control.next_channel()
