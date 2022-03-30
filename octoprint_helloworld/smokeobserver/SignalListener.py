from Listener import Listener
from singalmessage.Sender import SignalMessageSender


class SignalListener(Listener):
    def update(self):
        SignalMessageSender().send_message("Fire Alarm !!!")
