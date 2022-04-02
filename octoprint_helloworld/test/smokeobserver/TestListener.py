from smokeobserver.Listener import Listener


class TestListener(Listener):
    def __init__(self):
        self.nr_of_alarms_raise_received = 0
        self.nr_of_alarms_clear_received = 0

    def update(self, is_alarm: bool):
        if is_alarm:
            self.nr_of_alarms_raise_received += 1
        elif not is_alarm:
            self.nr_of_alarms_clear_received += 1
