import sys
from smokeobserver.Listener import Listener
from smokeobserver.VoltageReader import VoltageReader
from smokeobserver.Observable import Observable


class SmokeObserver(Observable):

    def __init__(self, mq2_voltage_reader: VoltageReader):
        self.observers = []
        self.mq2 = mq2_voltage_reader

    def register(self, observer: Listener):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def observe_smoke(self):
        while True:
            # sys.stdout.write("\r")
            # sys.stdout.write("\033[K")
            voltage = self.mq2.read_voltage()
            # sys.stdout.write('ADC Voltage: ' + str(voltage) + 'V')
            if voltage > 1:
                self.notify()

