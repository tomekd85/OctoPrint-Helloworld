from smokeobserver.Observable import Observable
from smokeobserver.SmokeAlarm import SmokeAlarmState, SmokeAlarmNotActive, SmokeAlarmActive
from test.smokeobserver.TestListner import TestListener
from test.smokeobserver.TestObservable import TestObservable


class TestSmokeAlarm:

    def test_smoke_alarm_state_initialization(self):
        sas = SmokeAlarmState(Observable())
        assert isinstance(sas.get_current_state(), SmokeAlarmNotActive)

    def test_smoke_alarm_changes_state_when_raised(self):
        sas = SmokeAlarmState(TestObservable())
        sas.raise_alarm()
        assert isinstance(sas.get_current_state(), SmokeAlarmActive)

    def test_smoke_alarm_changes_state_when_cleared(self):
        sas = SmokeAlarmState(TestObservable())
        sas.raise_alarm()
        sas.clear_alarm()
        assert isinstance(sas.get_current_state(), SmokeAlarmNotActive)

    def test_notification_sent_when_alarm_is_raised(self):
        observable = TestObservable()
        listener = TestListener()
        observable.register(listener)
        sas = SmokeAlarmState(observable)
        sas.raise_alarm()
        assert listener.is_called is True


