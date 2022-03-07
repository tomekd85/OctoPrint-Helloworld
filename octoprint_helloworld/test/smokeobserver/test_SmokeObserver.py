import threading
import time

from smokeobserver.SmokeObserver import SmokeObserver
from smokeobserver.VoltageReader import VoltageReader
from test.smokeobserver.TestListner import TestListener


class TestVoltageReader(VoltageReader):

    def __init__(self):
        self.value = 0

    def read_voltage(self) -> float:
        return self.value

    def set_value(self, value: float):
        self.value = value


class TestSmokeObserver:

    def setup_method(self, test_method):
        self.voltage_reader = TestVoltageReader()
        observer = SmokeObserver(self.voltage_reader)
        self.listener = TestListener()
        observer.register(self.listener)
        thread = threading.Thread(target=observer.observe_smoke, daemon=True)
        thread.start()

    def test_observe_smoke_without_alarm(self):
        self.voltage_reader.set_value(0.3)
        time.sleep(0.1)
        assert self.listener.is_called is not True

    def test_observe_smoke_with_alarm_notification_is_sent(self):
        self.voltage_reader.set_value(1.3)
        time.sleep(0.1)
        assert self.listener.is_called is True



