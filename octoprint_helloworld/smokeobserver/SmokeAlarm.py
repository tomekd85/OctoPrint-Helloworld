from typing import Callable

from smokeobserver.Listener import Listener


class SmokeAlarm:

    def raise_alarm(self):
        raise NotImplementedError

    def clear_alarm(self):
        raise NotImplementedError


class SmokeAlarmState(SmokeAlarm, Listener):

    def __init__(self, raise_callback: Callable, clear_callback: Callable):
        self.__current_state = SmokeAlarmNotActive(self)
        self.is_alarm_active = False
        self.raise_callback = raise_callback
        self.clear_callback = clear_callback

    def clear_alarm(self):
        self.__current_state.clear_alarm()

    def get_current_state(self):
        return self.__current_state

    def raise_alarm(self):
        self.__current_state.raise_alarm()

    def set_current_state(self, state: SmokeAlarm):
        self.__current_state = state

    def update(self, is_alarm: bool):
        if is_alarm:
            self.raise_alarm()
        elif not is_alarm:
            self.clear_alarm()


class SmokeAlarmActive(SmokeAlarm):

    def __init__(self, smoke_alarm: SmokeAlarmState):
        self.alarm_state = smoke_alarm

    def raise_alarm(self):
        pass

    def clear_alarm(self):
        self.alarm_state.set_current_state(SmokeAlarmNotActive(self.alarm_state))
        self.alarm_state.is_alarm_active = False
        self.alarm_state.clear_callback()


class SmokeAlarmNotActive(SmokeAlarm):

    def __init__(self, smoke_alarm: SmokeAlarmState):
        self.alarm_state = smoke_alarm

    def raise_alarm(self):
        self.alarm_state.set_current_state(SmokeAlarmActive(self.alarm_state))
        self.alarm_state.is_alarm_active = True
        self.alarm_state.raise_callback()

    def clear_alarm(self):
        pass


