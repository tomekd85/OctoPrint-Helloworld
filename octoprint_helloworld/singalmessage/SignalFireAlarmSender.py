from singalmessage.SignalMessageSender import SignalMessageSender


class SignalFireAlarmSender:

    def __init__(self):
        self.signal_message_sender = SignalMessageSender()

    def send_fire_alarm(self):
        self.signal_message_sender.send_message("Fire Alarm")

    def clear_fire_alarm(self):
        self.signal_message_sender.send_message("Fire Alarm no longer detected")
