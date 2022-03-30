from MQ2VoltageReader import MQ2VoltageReader
from SignalListener import SignalListener
from SmokeAlarm import SmokeAlarmState
from SmokeObserver import SmokeObserver
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP



class SignalAlarmNotifier:
    def run(self):
        observable = SmokeObserver(MQ2VoltageReader(busio, digitalio, MCP))
        listener = SignalListener()
        observable.register(listener)
        sas = SmokeAlarmState(observable)

