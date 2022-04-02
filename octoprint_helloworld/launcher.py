import adafruit_mcp3xxx.mcp3008 as MCP
import busio
import digitalio

from MQ2VoltageReader import MQ2VoltageReader
from SignalFireAlarmSender import SignalFireAlarmSender
from SmokeAlarm import SmokeAlarmState
from SmokeObserver import SmokeObserver


class SignalAlarmNotifier:

    def run(self):
        smoke_observer = SmokeObserver(MQ2VoltageReader(busio, digitalio, MCP))
        sas = SmokeAlarmState(SignalFireAlarmSender().send_fire_alarm,
                              SignalFireAlarmSender().clear_fire_alarm)
        smoke_observer.register(sas)
        smoke_observer.observe_smoke()


if __name__ == '__main__':
    SignalAlarmNotifier().run()
