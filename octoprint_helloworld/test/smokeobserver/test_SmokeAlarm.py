import unittest

from smokeobserver.SmokeAlarm import SmokeAlarmState, SmokeAlarmNotActive, SmokeAlarmActive
from test.smokeobserver.TestObservable import TestObservable


class Callbacks:

    def __init__(self):
        self.a = 0
        self.b = 0

    def empty_callback(self):
        pass

    def callback_a(self):
        self.a = 1

    def callback_b(self):
        self.b = 1


class TestSmokeAlarm(unittest.TestCase):

    def test_smoke_alarm_state_initialization(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.empty_callback, c.empty_callback)
        assert isinstance(sas.get_current_state(), SmokeAlarmNotActive)

    def test_smoke_alarm_changes_state_when_raised(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.empty_callback, c.empty_callback)
        sas.raise_alarm()
        assert isinstance(sas.get_current_state(), SmokeAlarmActive)

    def test_smoke_alarm_changes_state_when_cleared(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.empty_callback, c.empty_callback)
        sas.raise_alarm()
        sas.clear_alarm()
        assert isinstance(sas.get_current_state(), SmokeAlarmNotActive)

    def test_alarm_is_raised_when_observable_notifies_true(self):
        c = Callbacks()
        observable = TestObservable()
        sas = SmokeAlarmState(c.empty_callback, c.empty_callback)
        observable.register(sas)
        observable.notify(True)
        assert isinstance(sas.get_current_state(), SmokeAlarmActive)

    def test_alarm_is_cleared_when_observable_notifies_false(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.empty_callback, c.empty_callback)
        observable = TestObservable()
        observable.register(sas)
        observable.notify(True)
        observable.notify(False)
        assert isinstance(sas.get_current_state(), SmokeAlarmNotActive)

    def test_callback_not_called_without_changing_state(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.callback_a, c.callback_b)
        assert c.a == 0
        assert c.b == 0

    def test_callback_raise_is_called(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.callback_a, c.callback_b)
        sas.raise_alarm()
        assert c.a == 1
        assert c.b == 0

    def test_callback_clear_is_called(self):
        c = Callbacks()
        sas = SmokeAlarmState(c.callback_a, c.callback_b)
        sas.raise_alarm()
        sas.clear_alarm()
        assert c.a == 1
        assert c.b == 1

