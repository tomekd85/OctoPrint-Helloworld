import board
from adafruit_mcp3xxx.analog_in import AnalogIn
from smokeobserver.VoltageReader import VoltageReader


class MQ2VoltageReader(VoltageReader):

    def __init__(self, busio, digitalio, MCP):
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        # create the cs (chip select)
        cs = digitalio.DigitalInOut(board.D5)
        # create the mcp object
        mcp = MCP.MCP3008(spi, cs)
        # create an analog input channel on pin 0
        self.chan = AnalogIn(mcp, MCP.P0)

    def read_voltage(self) -> float:
        return self.chan.voltage
