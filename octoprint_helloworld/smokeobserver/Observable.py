from smokeobserver.Listener import Listener


class Observable:

    def register(self, observer: Listener):
        raise NotImplementedError()

    def notify(self):
        raise NotImplementedError()

