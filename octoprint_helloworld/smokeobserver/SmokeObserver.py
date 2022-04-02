from time import sleep

from smokeobserver.Listener import Listener
from smokeobserver.Observable import Observable
from smokeobserver.VoltageReader import VoltageReader


class SmokeObserver(Observable):

    def __init__(self, mq2_voltage_reader: VoltageReader):
        self.observers = []
        self.mq2 = mq2_voltage_reader

    def register(self, observer: Listener):
        self.observers.append(observer)

    def notify(self, is_alarm):
        for observer in self.observers:
            observer.update(is_alarm)

    def observe_smoke(self):
        while True:
            # sys.stdout.write("\r")
            # sys.stdout.write("\033[K")
            voltage = self.mq2.read_voltage()
            # sys.stdout.write('ADC Voltage: ' + str(voltage) + 'V')
            is_fire_alarm = voltage > 1
            self.notify(is_fire_alarm)
            sleep(1)

