from smokeobserver.Listener import Listener
from smokeobserver.Observable import Observable


class TestObservable(Observable):

    def __init__(self):
        self.observers = []

    def register(self, observer: Listener):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()
