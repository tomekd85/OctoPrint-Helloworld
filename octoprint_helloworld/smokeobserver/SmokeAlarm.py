from smokeobserver.Observable import Observable


class SmokeAlarm:

    def raise_alarm(self):
        raise NotImplementedError

    def clear_alarm(self):
        raise NotImplementedError


class SmokeAlarmState(SmokeAlarm):

    def __init__(self, observer: Observable):
        self.__current_state = SmokeAlarmNotActive(self)
        self.smoke_observer = observer
        self.is_alarm_active = False

    def raise_alarm(self):
        self.__current_state.raise_alarm()

    def clear_alarm(self):
        self.__current_state.clear_alarm()

    def get_current_state(self):
        return self.__current_state

    def set_current_state(self, state: SmokeAlarm):
        self.__current_state = state

    def notify(self):
        self.smoke_observer.notify()


class SmokeAlarmActive(SmokeAlarm):

    def __init__(self, smoke_alarm: SmokeAlarmState):
        self.alarm_state = smoke_alarm

    def raise_alarm(self):
        pass

    def clear_alarm(self):
        self.alarm_state.set_current_state(SmokeAlarmNotActive(self.alarm_state))
        self.alarm_state.is_alarm_active = False


class SmokeAlarmNotActive(SmokeAlarm):

    def __init__(self, smoke_alarm: SmokeAlarmState):
        self.alarm_state = smoke_alarm

    def raise_alarm(self):
        self.alarm_state.set_current_state(SmokeAlarmActive(self.alarm_state))
        self.alarm_state.is_alarm_active = True
        self.alarm_state.notify()

    def clear_alarm(self):
        pass


