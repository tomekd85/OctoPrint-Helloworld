import unittest
import threading
import time

from smokeobserver.SmokeObserver import SmokeObserver
from smokeobserver.VoltageReader import VoltageReader
from test.smokeobserver.TestListener import TestListener


class TestVoltageReader(VoltageReader):

    def __init__(self):
        self.value = 0

    def read_voltage(self) -> float:
        return self.value

    def set_value(self, value: float):
        self.value = value


class TestSmokeObserver(unittest.TestCase):

    def setUp(self):
        self.voltage_reader = TestVoltageReader()
        observer = SmokeObserver(self.voltage_reader)
        self.listener = TestListener()
        observer.register(self.listener)
        thread = threading.Thread(target=observer.observe_smoke, daemon=True)
        thread.start()

    def test_observe_smoke_without_alarm(self):
        self.voltage_reader.set_value(0.3)
        time.sleep(3)
        assert self.listener.nr_of_alarms_clear_received > 1

    def test_observe_smoke_with_alarm_notification_is_sent(self):
        self.voltage_reader.set_value(1.3)
        time.sleep(3)
        assert self.listener.nr_of_alarms_raise_received > 1
